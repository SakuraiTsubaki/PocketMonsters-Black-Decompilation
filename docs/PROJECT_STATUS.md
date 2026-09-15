# Project Status

**Current stage:** ROM-observed executable/NitroFS baseline and full ARM9-overlay inventory

The project is now actively working from the supplied Pokémon Black USA/Europe English revision-0 image in addition to public-source cross-checking. The supplied image is the known SweeTnDs-era underdump, so observations from it are recorded as **Observed** and kept distinct from canonical clean-dump **Matched** claims.

## Version inventory

| Target | Region | Language | Revision / update | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| Pokémon Black | USA/Europe | English | Rev 0 / game code `IRBO` | Observed | Supplied SweeTnDs-era underdump; canonical clean hashes remain reference-only |

## Supplied input identity

- Size: `268435456` bytes
- MD5: `f45fd94bb761721e30bd3a0a4fde124a`
- SHA-1: `a68b3bedf5c1e53556e41e59cdf396c20b331896`
- SHA-256: `2e40416b8e8183d936084c7be0adeaab4fa3f786a68f90d7291ab77d340f0c1d`
- Preservation status: known underdump; do not treat this full-ROM identity as the canonical clean target

## Executable / filesystem baseline

- ARM9 ROM offset: `0x00004000`
- ARM9 size: `456856` bytes
- ARM7 ROM offset: `0x002C7E00`
- ARM7 size: `167812` bytes
- FNT offset / size: `0x002F0E00` / `1040` bytes
- FAT offset / size: `0x002F1400` / `3872` bytes
- FAT entries: `484`
- Named FNT files: `247`
- ARM9 overlays: `237`
- ARM7 overlays: `0`
- Backwards-compressed ARM9 overlays: `229`
- Uncompressed ARM9 overlays: `8`
- Overlay decompression size mismatches: `0`

## Black / White comparison baseline

Across all 484 FAT entries:

- Byte-identical entries: `299`
- Different entries: `185`
- Different named entries: `5`
- Different overlay entries: `180`
- Byte-identical overlays after expansion: `57`
- Different overlays after expansion: `180`
- Overlay load-address differences: `232 / 237`
- Compression-status difference: overlay `3`
- ARM7: byte-identical between supplied Black and White inputs
- ARM9: different

The five different named NitroFS paths are:

- `a/0/2/6`
- `a/0/8/6`
- `a/1/2/6`
- `a/1/7/8`
- `a/2/3/1`

## Progress

- [x] Establish public-source research methodology
- [x] Record supplied IRBO Rev-0 ROM identity and preservation caveat
- [x] Parse NDS header, ARM9, ARM7, FNT, FAT and overlay-table layout
- [x] Inventory all `484` FAT entries
- [x] Inventory all `237` ARM9 overlays
- [x] Decompress every compressed ARM9 overlay and verify expanded size against the overlay table
- [x] Compare every FAT entry and every expanded ARM9 overlay against the supplied White input
- [x] Reconstruct and byte-match ARM9 overlay 74 as the first verified executable unit
- [ ] Reconstruct ARM9 overlays `0..236` into readable source units
- [ ] Reconstruct the ARM9 main executable
- [ ] Identify functions, data tables, relocations, callbacks and static initializers per executable unit
- [ ] Decode and document all NitroFS/NARC resource formats
- [ ] Map scripts, events, flags, variables and game subsystems
- [ ] Reconstruct graphics, maps, audio and other resource pipelines
- [ ] Reconstruct save, communication, online and distribution structures
- [ ] Catalog unused, dummy, debug and development material
- [ ] Add reproducible unit-level build/match verification across the executable set
- [ ] Cross-check observed units against canonical clean-target evidence before promoting them to Matched

## Validation levels

- **Unverified** — proposed, repeated, or recorded but not independently checked.
- **Corroborated** — supported by multiple independent sources.
- **Implemented** — represented in working source code or tooling.
- **Preserved** — backed by surviving archival files or historical captures.
- **Observed** — directly demonstrated in the supplied target input or extracted data.
- **Reproduced** — behavior or data can be recreated with documented steps.
- **Matched** — reconstructed output is byte-verified against an identified target executable/data unit.

## Next milestones

1. Generate per-overlay reconstruction work units for ARM9 overlays `0..236` rather than selecting only representative overlays.
2. Start with the smallest executable units, identify code/data boundaries, and add symbols without inventing semantics.
3. Build the ARM9-main executable map in parallel with overlay reconstruction.
4. Fully decode the five named Black/White-different NitroFS resources and classify the version-specific content they contain.
5. Expand unit-level linker/build verification so each reconstructed executable can progress from Observed → Reproduced → Matched independently.

Update this file whenever a new executable unit, data archive, revision, or verification milestone is completed.
