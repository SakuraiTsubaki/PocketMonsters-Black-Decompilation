# ROM Baseline — Pokémon Black (English, IRBO)

This document records the first read-only structural census of the supplied retail ROM image. The ROM image itself is **not** committed to this repository.

## Identity

- Internal title: `POKEMON B`
- Game code: `IRBO`
- Maker code: `01`
- Unit code: `0x02`
- Revision: `0`
- ROM size: `268435456` bytes (256 MiB)
- Used ROM size from header: `0x0C3B8E00`
- CRC32: `E2BEE619`
- MD5: `F45FD94BB761721E30BD3A0A4FDE124A`
- SHA-1: `A68B3BEDF5C1E53556E41E59CDF396C20B331896`
- SHA-256: `2E40416B8E8183D936084C7BE0ADEAAB4FA3F786A68F90D7291AB77D340F0C1D`

## Executable layout

- ARM9 ROM offset: `0x4000`
- ARM9 RAM address: `0x2004000`
- ARM9 entry address: `0x2004800`
- ARM9 size: `0x6F898` (456856 bytes)
- ARM7 ROM offset: `0x2C7E00`
- ARM7 RAM address: `0x2380000`
- ARM7 entry address: `0x2380000`
- ARM7 size: `0x28F84` (167812 bytes)
- ARM9 overlay entries: `237`

## Filesystem census

- FAT entries: `484`
- Named NitroFS files: `247`
- FNT: offset `0x2F0E00`, size `0x410`
- FAT: offset `0x2F1400`, size `0xF20`
- ARM9 overlay table: offset `0x73A00`, size `0x1DA0`

## Black / White binary comparison

Comparing file IDs at the same FAT positions between the supplied Black and White images:

- Total FAT entries: **484**
- Byte-identical entries: **299**
- Different entries: **185**
- ARM9 overlay entries: **237** total, **180** different
- Named NitroFS files: **247** total, **242** identical, **5** different

The five named NitroFS files that differ are:

| File ID | Path | Black bytes | White bytes | NARC members changed |
|---:|---|---:|---:|---:|
| 268 | `a/0/2/6` | 22228 | 22528 | 8 / 15 |
| 328 | `a/0/8/6` | 3356 | 3356 | 1 / 1 |
| 368 | `a/1/2/6` | 35284 | 35284 | 29 / 112 |
| 420 | `a/1/7/8` | 168792 | 168792 | 26 / 649 |
| 473 | `a/2/3/1` | 1208900 | 1210248 | 2 / 73 |

## Preservation rule

The supplied ROM is treated as a read-only reference. Retail ROM images are excluded from GitHub. Derived inventories, hashes, reconstructed source, extraction tooling, documentation, and reviewable assets belong in the repository.
