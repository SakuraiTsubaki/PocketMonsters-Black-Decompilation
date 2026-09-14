# Project Status

**Current stage:** Public-source survey and reconstruction baseline

This project assumes no local retail ROM is available. Work therefore begins from publicly accessible official material, technical implementations, preservation archives, reverse-engineering research, historical web captures, and independently maintained references.

## Baseline policy

- Japanese retail release is the canonical starting comparison point.
- Every official regional/language/territory/revision target remains independent until evidence proves identity.
- Public-reference hashes and archive counts are not project-level `Matched` evidence.
- Unknown values remain `TBD`/`Unknown`.
- GitHub is the authoritative project record; retail ROM binaries remain excluded.

## Progress

- [x] Establish public-source-first research methodology.
- [x] Create initial public source inventory (`docs/PUBLIC_SOURCE_SURVEY.md`).
- [x] Seed Japanese baseline and major regional/language targets in `docs/VERSIONS.md`.
- [x] Create Japanese-baseline regional comparison ledger (`docs/REGIONAL_SURVEY_MATRIX.md`).
- [x] Seed evidence-backed NitroFS/NARC path catalog (`docs/NARC_PATH_CATALOG.md`).
- [x] Add machine-readable NARC path inventory (`manifests/narc-paths.csv`).
- [x] Record first BW ↔ B2W2 path-movement findings and public-source conflicts.
- [ ] Complete every official territory, packaging, language, and revision target.
- [ ] Identify the exact region/revision represented by the public Black Raw DB tree.
- [ ] Import the complete Raw DB archive census while preserving unknown roles.
- [ ] Document executable and overlay layout from public technical evidence.
- [ ] Map symbols, functions, and major subsystems where public evidence permits.
- [ ] Document game-data formats and resource containers at record/field level.
- [ ] Reconstruct scripts, events, flags, variables, and behavior.
- [ ] Reconstruct asset pipelines and metadata.
- [ ] Reconstruct save, communication, online, and distribution structures.
- [ ] Catalog unused, dummy, debug, and development material.
- [ ] Add reproducible tooling that does not redistribute retail ROM binaries.
- [ ] Add automated verification where practical.

## Current technical baseline

Public sources currently corroborate key Black paths for text, personal data, learnsets, evolutions, moves, items, scripts, trainers, overworld/event data, and encounters. Project Pokémon Raw DB enumerates a large Black NARC census, but its exact source build must be established before it is treated as the Japanese baseline.

The first structural comparison already proves important subsystem relocation between BW and B2W2: scripts, trainer metadata/parties, overworld events, and encounters move to different archive paths in the sequels.

## Validation handling

Repository-standard verification remains `Unverified` → `Observed` → `Reproduced` → `Matched`. Research documents may additionally describe public evidence as corroborated, direct technical, single-source, preserved, or conflicted, but these labels do not replace project-level target verification.

## Next milestones

1. Complete the Black archive census and identify the Raw DB source build.
2. Expand each known NARC from path-level identity into file/record format documentation.
3. Start with high-value data families: personal data, moves, evolutions/learnsets, trainers, encounters, text, and scripts.
4. Continue regional comparison from product identity into actual localization/technical differences.
5. Keep `VERSIONS.md`, regional matrix, NARC catalog, manifests, and this status synchronized.