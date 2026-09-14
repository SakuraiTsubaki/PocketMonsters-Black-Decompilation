# Clean Reference — Pokémon Black Version EUR

This repository treats the exact analyzed ROM identified below as the **project clean reference** for EUR Black work. The ROM binary itself is never committed. All decompilation, extraction, comparison, reconstruction, and verification artifacts must remain traceable to this exact reference.

## Identity

- Internal title: `POKEMON B`
- Game code: `IRBO`
- Revision: `0`
- Unit code: `0x02`
- Size: `268435456` bytes
- CRC32: `E2BEE619`
- MD5: `F45FD94BB761721E30BD3A0A4FDE124A`
- SHA-1: `A68B3BEDF5C1E53556E41E59CDF396C20B331896`
- SHA-256: `2E40416B8E8183D936084C7BE0ADEAAB4FA3F786A68F90D7291AB77D340F0C1D`

## Reference rules

1. The retail `.nds` binary is read-only input and is not committed to GitHub.
2. Extracted/reconstructed source, metadata, manifests, conversion tools, documentation, and reviewable assets may be committed.
3. Derived files should remain reproducible from this exact reference whenever practical.
4. Any later regional/revision ROM is a separate reference, not a replacement for this one.
5. “Clean reference” here means the project's immutable binary baseline; it does not independently certify archival dump provenance.
6. Black/White differences are preserved rather than normalized away.

## Structural baseline

- FAT entries: **484**
- Named NitroFS files: **247**
- NARC archives: **237**
- ARM9 overlays: **237**

The next layer is the complete NitroFS/NARC census and member-level Black/White comparison.
