#!/usr/bin/env python3
"""Compare member-level contents of named NARC files from two NDS targets."""
from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path


def parse_narc(raw: bytes) -> dict:
    if raw[:4] != b"NARC":
        raise ValueError("input is not a NARC archive")
    bom, version, file_size, header_size, block_count = struct.unpack_from("<HHIHH", raw, 4)
    pos = header_size
    blocks = {}
    for _ in range(block_count):
        magic = raw[pos:pos + 4].decode("ascii", "replace")
        size = struct.unpack_from("<I", raw, pos + 4)[0]
        blocks[magic] = raw[pos:pos + size]
        pos += size
    btaf = blocks["BTAF"]
    member_count = struct.unpack_from("<H", btaf, 8)[0]
    ranges = [struct.unpack_from("<II", btaf, 12 + i * 8) for i in range(member_count)]
    gmif_data = blocks["GMIF"][8:]
    members = []
    for index, (start, end) in enumerate(ranges):
        payload = gmif_data[start:end]
        members.append({
            "index": index,
            "size": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest(),
        })
    return {
        "bom": f"0x{bom:04X}",
        "version": f"0x{version:04X}",
        "file_size_field": file_size,
        "header_size": header_size,
        "block_count": block_count,
        "member_count": member_count,
        "members": members,
    }


def compare(left: bytes, right: bytes) -> dict:
    l = parse_narc(left)
    r = parse_narc(right)
    lm, rm = l.pop("members"), r.pop("members")
    diffs = []
    identical = 0
    for index in range(max(len(lm), len(rm))):
        if index >= len(lm):
            diffs.append({"index": index, "status": "right_only", "right": rm[index]})
        elif index >= len(rm):
            diffs.append({"index": index, "status": "left_only", "left": lm[index]})
        elif lm[index]["sha256"] == rm[index]["sha256"]:
            identical += 1
        else:
            diffs.append({"index": index, "status": "different", "left": lm[index], "right": rm[index]})
    return {
        "left": l,
        "right": r,
        "identical_member_count": identical,
        "different_or_unpaired_member_count": len(diffs),
        "differences": diffs,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("left", type=Path)
    parser.add_argument("right", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    result = compare(args.left.read_bytes(), args.right.read_bytes())
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
