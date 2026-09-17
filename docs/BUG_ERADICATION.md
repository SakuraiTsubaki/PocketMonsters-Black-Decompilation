# Bug / Glitch / Error Eradication Program

## Goal

Eliminate reproducible defects in the Generation V Black/White implementation while preserving intentional mechanics, version differences, unused/dummy assets, historical behavior records, and all non-ROM research artifacts.

## Non-negotiable rules

1. Never treat an emulator-only fault as a retail-game bug without hardware-equivalent confirmation.
2. Never treat a faulty dump, anti-piracy behavior, missing DSi payload, or external-server failure as an engine bug without separating the layers first.
3. Never delete unused/dummy/placeholder content merely because it is unreachable. Preserve it, classify it, and later restore or repurpose it through normal game paths when the project calls for that.
4. Black and White remain separate products. Shared fixes may be implemented from one common diagnosis, but version-exclusive data and behavior are verified independently.
5. Region/language-specific defects stay separate from all-language defects.
6. A defect is not closed until a deterministic reproduction and a regression test exist.

## Status pipeline

`candidate -> reproduced -> localized -> patched -> regression-tested -> fixed`

Additional states: `not-applicable`, `intentional`, `external-service`, `dump-defect`, `emulator-only`, `needs-clean-baseline`.

## Priority order

1. Input and build integrity: clean canonical Version 1.0 baseline, deterministic extraction/rebuild, overlay/file hashes.
2. Crashes and softlocks: Triple Battle, Sky Drop/Gravity, HP/fainted state, GTS null/empty result, invalid party state.
3. Save/data corruption and persistent state contamination.
4. Battle-rule correctness: damage, item/Ability state, AI move selection, Trick Room arithmetic.
5. Event/script progression and collision errors.
6. Network/UI state errors.
7. Audio/graphics/text/metadata oversights.
8. Defensive hardening for corrupted/modded states without removing preserved unused data.

## Reproduction record required for every defect

- game/version/region/language/revision;
- clean-base hash and patched-base hash;
- exact preconditions and save state requirements;
- minimal input sequence;
- expected behavior and observed behavior;
- ARM9/overlay/script/archive/file ownership;
- code/data addresses or symbolic identifiers;
- root cause;
- patch description;
- before/after test result;
- Black/White cross-version result;
- DS/DSi mode and emulator/hardware-equivalent result where relevant.

## Current binary facts from supplied inputs

- Both supplied images are 256 MiB, revision byte 0, DSi-enhanced (`unit_code = 2`).
- Black code: `IRBO`; White code: `IRAO`.
- ARM9 overlay table: 237 entries in each image.
- FAT: 484 files in each image.
- ARM7 payload is identical between supplied Black and White.
- Of 237 overlay payloads, 57 are byte-identical and 180 differ.
- Of 247 non-overlay FAT files, 242 are byte-identical and 5 differ (`a/0/2/6`, `a/0/8/6`, `a/1/2/6`, `a/1/7/8`, `a/2/3/1`).
- The supplied SweeTnDs images are noncanonical faulty dumps missing DSi-specific data. They are valid research inputs but are not the clean matching baseline.

## Canonical matching reference

Black English USA/EUR Version 1.0 matching reference:

- CRC32 `4F6E5580`
- SHA-1 `26ad0b9967aa279c4a266ee69f52b9b2332399a5`

The ROM itself must remain outside Git.

## Regression test families to build

- battle state-machine tests;
- damage/modifier arithmetic vectors;
- move legality and AI targetability vectors;
- held-item/Ability transition tests;
- party/box/menu invalid-state tests;
- map collision and warp validation;
- event flag/script transition tests;
- save/load/RTC/season state tests;
- BGM dynamic-layer state tests;
- graphics/tile/occlusion snapshots;
- network result-list parser/state tests with captured or reconstructed protocol fixtures;
- full Black-vs-White differential tests that explicitly whitelist intentional version differences.

The authoritative working list is `analysis/bug_registry.csv`. Every discovered defect, including newly found ROM-only defects not documented publicly, must be added there before closure.
