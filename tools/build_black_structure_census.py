#!/usr/bin/env python3
"""Build reviewable Pokémon Black NDS structure manifests without exporting ROM bytes."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import struct
from collections import Counter
from pathlib import Path


def u16(data: bytes, offset: int) -> int:
    return struct.unpack_from("<H", data, offset)[0]


def u32(data: bytes, offset: int) -> int:
    return struct.unpack_from("<I", data, offset)[0]


def parse_fnt(data: bytes) -> tuple[dict[int, str], int]:
    count = u16(data, 6)
    directories = [struct.unpack_from("<IHH", data, i * 8) for i in range(count)]
    paths: dict[int, str] = {}

    def walk(directory_id: int, prefix: str) -> None:
        subtable, file_id, _parent = directories[directory_id - 0xF000]
        pos = subtable
        while True:
            control = data[pos]
            pos += 1
            if control == 0:
                return
            is_directory = bool(control & 0x80)
            length = control & 0x7F
            name = data[pos : pos + length].decode("ascii", "replace")
            pos += length
            if is_directory:
                child = u16(data, pos)
                pos += 2
                walk(child, f"{prefix}{name}/")
            else:
                paths[file_id] = f"{prefix}{name}"
                file_id += 1

    walk(0xF000, "")
    return paths, count


def member_kind(data: bytes) -> str:
    signatures = {
        b"NARC": "NARC", b"RGCN": "NCGR", b"RLCN": "NCLR",
        b"RCSN": "NSCR", b"RECN": "NCER", b"RNAN": "NANR",
        b"BMD0": "BMD0", b"BTX0": "BTX0", b"BCA0": "BCA0",
        b"BTA0": "BTA0", b"BTP0": "BTP0", b"BMA0": "BMA0",
        b"BVA0": "BVA0", b"SDAT": "SDAT",
    }
    if data[:4] in signatures:
        return signatures[data[:4]]
    if data[:1] == b"\x10":
        return "LZ10"
    if data[:1] == b"\x11":
        return "LZ11"
    return "unknown"


def parse_narc(data: bytes) -> tuple[int, int, list[str], Counter[str]]:
    header_size = u16(data, 12)
    section_count = u16(data, 14)
    pos = header_size
    sections: dict[bytes, tuple[int, int]] = {}
    order: list[str] = []
    for _ in range(section_count):
        tag = data[pos : pos + 4]
        size = u32(data, pos + 4)
        sections[tag] = (pos, size)
        order.append(tag.decode("ascii", "replace"))
        pos += size
    fat = sections.get(b"BTAF") or sections[b"FATB"]
    image = sections.get(b"GMIF") or sections[b"FIMG"]
    count = u16(data, fat[0] + 8)
    table = fat[0] + 12
    base = image[0] + 8
    kinds: Counter[str] = Counter()
    member_bytes = 0
    for index in range(count):
        start, end = struct.unpack_from("<II", data, table + index * 8)
        member = data[base + start : base + end]
        member_bytes += len(member)
        kinds[member_kind(member)] += 1
    return count, member_bytes, order, kinds


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("rom", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    rom = args.rom.read_bytes()
    header = rom[:0x4000]
    fnt_offset, fnt_size = u32(header, 0x40), u32(header, 0x44)
    fat_offset, fat_size = u32(header, 0x48), u32(header, 0x4C)
    overlay_offset, overlay_size = u32(header, 0x50), u32(header, 0x54)
    names, directory_count = parse_fnt(rom[fnt_offset : fnt_offset + fnt_size])
    fat = [struct.unpack_from("<II", rom, fat_offset + i * 8) for i in range(fat_size // 8)]

    overlay_rows = []
    for index in range(overlay_size // 32):
        values = struct.unpack_from("<8I", rom, overlay_offset + index * 32)
        overlay_id, ram, ram_size, bss, init_start, init_end, file_id, packed = values
        start, end = fat[file_id]
        blob = rom[start:end]
        overlay_rows.append({
            "overlay_id": overlay_id, "file_id": file_id, "rom_offset": start,
            "stored_size": len(blob), "ram_address": f"0x{ram:08X}",
            "ram_size": ram_size, "bss_size": bss,
            "static_init_start": f"0x{init_start:08X}",
            "static_init_end": f"0x{init_end:08X}",
            "compressed_size": packed & 0x00FFFFFF,
            "compressed_flag": bool(packed & 0x01000000),
            "sha1": hashlib.sha1(blob).hexdigest(),
            "sha256": hashlib.sha256(blob).hexdigest(),
        })

    narc_rows = []
    inner_types: Counter[str] = Counter()
    for file_id, name in sorted(names.items()):
        start, end = fat[file_id]
        blob = rom[start:end]
        if blob[:4] != b"NARC":
            continue
        count, member_bytes, sections, kinds = parse_narc(blob)
        inner_types.update(kinds)
        narc_rows.append({
            "file_id": file_id, "path": name, "rom_offset": start, "size": len(blob),
            "member_count": count, "member_bytes": member_bytes,
            "sections": ";".join(sections), "member_kinds": json.dumps(kinds, sort_keys=True),
            "sha1": hashlib.sha1(blob).hexdigest(),
            "sha256": hashlib.sha256(blob).hexdigest(),
        })

    summary = {
        "schema_version": 1,
        "evidence": "direct observation of immutable raw input",
        "rom_binary_exported": False,
        "identity": {
            "internal_title": header[:12].rstrip(b"\0 ").decode("ascii"),
            "game_code": header[12:16].decode("ascii"),
            "maker_code": header[16:18].decode("ascii"),
            "unit_code": header[18], "revision": header[30], "size_bytes": len(rom),
            "sha1": hashlib.sha1(rom).hexdigest(), "sha256": hashlib.sha256(rom).hexdigest(),
        },
        "counts": {
            "fat_entries": len(fat), "directories": directory_count,
            "named_nitrofs_files": len(names), "arm9_overlays": len(overlay_rows),
            "compressed_arm9_overlays": sum(row["compressed_flag"] for row in overlay_rows),
            "narc_archives": len(narc_rows),
            "narc_members": sum(row["member_count"] for row in narc_rows),
        },
        "narc_inner_format_counts": dict(inner_types.most_common()),
        "dsi_executables": {
            "arm9i_rom_offset": u32(header, 0x1C0), "arm9i_ram_address": u32(header, 0x1C8),
            "arm9i_size": u32(header, 0x1CC), "arm7i_rom_offset": u32(header, 0x1D0),
            "arm7i_ram_address": u32(header, 0x1D8), "arm7i_size": u32(header, 0x1DC),
        },
    }
    (args.output / "black-structure-summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    write_csv(args.output / "black-arm9-overlays.csv", list(overlay_rows[0]), overlay_rows)
    write_csv(args.output / "black-narc-census.csv", list(narc_rows[0]), narc_rows)
    write_csv(
        args.output / "black-narc-inner-formats.csv", ["format", "count"],
        [{"format": key, "count": value} for key, value in inner_types.most_common()],
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
