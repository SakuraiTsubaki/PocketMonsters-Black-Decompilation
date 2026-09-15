# Project Status

**Current stage:** Exhaustive public-source census and direct raw-input reconstruction baseline

A local Pokémon Black EUR raw input is available for immutable, read-only structural analysis. It is not the canonical-clean build target and its identity remains separate. Publicly accessible official material, technical implementations, preservation archives, reverse-engineering research, historical web captures, and independently maintained references remain mandatory for Japanese-first and all-region coverage.

## Baseline policy

- Japanese retail release is the canonical starting comparison point.
- Every official regional/language/territory/revision target remains independent until evidence proves identity.
- Public-reference hashes and archive counts are not project-level `Matched` evidence.
- Unknown values remain `TBD`/`Unknown`.
- GitHub is the authoritative project record; retail ROM binaries remain excluded.
- **Subsystem reconstruction does not replace the source census. Source classes must continue to be enumerated until the public-source registry is closed category by category.**

## Source-census priority

- [x] Create exhaustive source-class registry (`docs/SOURCE_REGISTRY.md`).
- [x] Add machine-readable source inventory (`manifests/source-registry.csv`).
- [x] Register official JP/KR/US/EU/AU starting points, manuals and service-history sources.
- [x] Register preservation roots for Gen V events, Dream World, C-Gear, Pokédex skins, Musicals, PWT and server-format DLC.
- [x] Register major public Gen V technical/code projects and Nintendo DS infrastructure tools.
- [x] Register unused/prerelease, secondary-reference, catalog/revision, physical-scan, guide, magazine, soundtrack and bug-research source classes.
- [ ] Enumerate every relevant child page/file/release/record under every registered source root.
- [ ] Enumerate Internet Archive/Wayback captures for dead official and regional sites.
- [ ] Enumerate every official event/distribution/service notice by region and language.
- [ ] Enumerate historical tools/research whose original hosting has disappeared.
- [ ] Resolve blocked TCRF material through indexed or archived evidence without inventing inaccessible content.
- [ ] Do not mark the public-source survey complete while any mandatory class remains `Enumerating`, `Candidate`, `Blocked`, or otherwise unresolved.

## Reconstruction progress

- [x] Establish public-source-first research methodology.
- [x] Create initial public source survey (`docs/PUBLIC_SOURCE_SURVEY.md`).
- [x] Seed Japanese baseline and major regional/language targets in `docs/VERSIONS.md`.
- [x] Create Japanese-baseline regional comparison ledger (`docs/REGIONAL_SURVEY_MATRIX.md`).
- [x] Seed evidence-backed NitroFS/NARC path catalog (`docs/NARC_PATH_CATALOG.md`).
- [x] Add machine-readable NARC path inventory (`manifests/narc-paths.csv`).
- [x] Record first BW ↔ B2W2 path-movement findings and public-source conflicts.
- [ ] Complete every official territory, packaging, language, and revision target.
- [ ] Identify the exact region/revision represented by the public Black Raw DB tree.
- [ ] Import the complete Raw DB archive census while preserving unknown roles.
- [x] Inventory the local raw input's NDS/TWL executable, FAT/FNT, 237 ARM9 overlays, 237 NARCs, and 54,054 NARC members.\n- [ ] Promote executable and overlay semantics through canonical-clean and public technical evidence.
- [ ] Map symbols, functions, and major subsystems where public evidence permits.
- [ ] Document game-data formats and resource containers at record/field level.
- [ ] Reconstruct scripts, events, flags, variables, and behavior.
- [ ] Reconstruct asset pipelines and metadata.
- [ ] Reconstruct save, communication, online, and distribution structures.
- [ ] Catalog unused, dummy, debug, and development material.
- [ ] Add reproducible tooling that does not redistribute retail ROM binaries.
- [ ] Add automated verification where practical.

## Current technical baseline

Direct raw-input inspection now establishes 484 FAT entries, 31 FNT directories, 247 named NitroFS files, 237 ARM9 overlays (229 marked compressed), 237 NARCs, and 54,054 NARC members. These are `Observed raw input` results, not canonical-clean matches. Public sources currently corroborate key Black paths for text, personal data, learnsets, evolutions, moves, items, scripts, trainers, overworld/event data, and encounters. Project Pokémon Raw DB enumerates a large Black NARC census, but its exact source build must be established before it is treated as the Japanese baseline.

The first structural comparison already proves important subsystem relocation between BW and B2W2: scripts, trainer metadata/parties, overworld events, and encounters move to different archive paths in the sequels.

## Validation handling

Repository-standard verification remains `Unverified` → `Observed` → `Reproduced` → `Matched`. Research documents may additionally describe public evidence as corroborated, direct technical, single-source, preserved, or conflicted, but these labels do not replace project-level target verification.

## Next milestones

1. Enumerate the registered public-source universe source-by-source and file/page-by-file/page before narrowing the project to any one subsystem.
2. Expand official Japanese material first, then enumerate every regional/language official and archival branch.
3. Enumerate preservation/event/DLC collections and public code repositories at item/file level.
4. Continue the Black archive census and identify the Raw DB source build in parallel without treating it as the whole survey.
5. Keep `SOURCE_REGISTRY.md`, source manifest, versions, regional matrix, NARC catalog and this status synchronized.
