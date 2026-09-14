# NARC / NitroFS Path Catalog — Pokémon Black

## Purpose

This document records publicly documented NitroFS/NARC paths for Pokémon Black without pretending that a local retail ROM has been inspected. It is an evidence map: path identity, reported role, public archive member count where available, source provenance, and unresolved conflicts.

The machine-readable companion is `../manifests/narc-paths.csv`.

## Verification policy

- No entry in this document is `Observed` merely because an external tool or forum post names the path.
- `Corroborated` means multiple independent public sources agree on the path/role.
- `Direct technical` means public source code or a tool implementation directly targets the path.
- `Single-source` means a credible technical/preservation source exists but independent confirmation is pending.
- File counts from Project Pokémon Raw DB are preservation metadata, not counts independently reproduced by this project.

## Initial path catalog

| Path | Reported role | Public member count | Evidence | Notes |
| --- | --- | ---: | --- | --- |
| `/a/0/0/2` | Main/system text | 288 | Corroborated | Project Pokémon Raw DB labels it Text/Message Files; PPRE and the BW translation project independently use it as main text. |
| `/a/0/0/3` | Story text | 472 | Corroborated | Raw DB, PPRE, and translation work agree. |
| `/a/0/0/8` | Map resources | 649 | Single-source for semantic role | Archive/count exists in Raw DB; mapping to maps is preserved in public ROM-hacking documentation. Needs stronger format-level identification. |
| `/a/0/1/6` | Pokémon personal data | 669 | Corroborated | Raw DB labels Pokémon data; PPRE targets the same path. |
| `/a/0/1/7` | Experience/growth table | 8 | Corroborated | Raw DB + PPRE. |
| `/a/0/1/8` | Level-up learnsets | 668 | Corroborated | Raw DB + PPRE. |
| `/a/0/1/9` | Evolution data | 668 | Corroborated | Raw DB + PPRE. |
| `/a/0/2/0` | Base-evolution / baby-Pokémon lookup (PPRE terminology) | 650 | Direct technical | PPRE targets this path; Raw DB confirms archive/member count. Exact semantic/record format still needs dedicated documentation. |
| `/a/0/2/1` | Move data | 560 | Corroborated | Raw DB + PPRE. |
| `/a/0/2/3` | Font set | 8 | Direct technical | Public Japanese BW text/font reconstruction work extracts this path as the font set. Raw DB confirms an 8-member archive. |
| `/a/0/2/4` | Item data | 627 | Direct technical | PPRE targets this path as item data; Raw DB supplies count. |
| `/a/0/2/6` | Logo/title graphics used by translation work | 15 | Single-source | BW translation project records this NARC among modified logo resources; exact contents still need asset-level indexing. |
| `/a/0/4/9` | Overworld sprites | 764 | Single-source | Public Gen IV/V ROM-content documentation identifies this path; Raw DB confirms archive/count. |
| `/a/0/5/7` | In-game scripts | 899 | Corroborated | Project Pokémon script/overworld research and independent ROM-content documentation agree. |
| `/a/0/9/2` | Trainer metadata (`trdata`) | 616 | Corroborated | Project Pokémon B/W Trainer Editor, TrainerTyrant, and Raw DB agree. |
| `/a/0/9/3` | Trainer parties (`trpoke`) | 616 | Corroborated | Project Pokémon B/W Trainer Editor and TrainerTyrant agree; Raw DB confirms archive/count. |
| `/a/1/2/5` | Overworld/map-event data | 428 | Corroborated | Project Pokémon overworld/script research identifies it directly; Raw DB confirms archive/count. |
| `/a/1/2/6` | Wild encounter tables | 112 | Corroborated | PPRE and B/W wild-editor research use this path; Raw DB confirms 112 members. |
| `/skb.narc` | Role not yet assigned | 6 | Structural only | Raw DB confirms archive and count. Do not infer function from filename alone. |
| `/soundstatus.narc` | Role not yet assigned | 4 | Structural only | Raw DB confirms archive and count; semantic role remains TBD. |
| `/titledemo.narc` | Role not yet assigned | 20 | Structural only | Raw DB confirms archive and count; semantic role remains TBD. |
| `/wb_sound_data.sdat` | Nintendo DS sound archive/container; internal Gen V audio mapping TBD | not NARC | Structural only | Raw DB records this root file as non-NARC. SDAT internals require a separate audio survey. |
| `/gfl_font.dat` | Role TBD | not NARC | Structural only | Raw DB records the root file. Do not equate it with `/a/0/2/3` without format evidence. |

## Archive census baseline

Project Pokémon Raw DB currently enumerates **237 NARC entries** for its Pokémon Black reference tree (link indices 0–236), plus several explicitly non-NARC files. This is a valuable preservation census, but it is not yet a project-verified Japanese-baseline file tree. The source region/revision behind that Raw DB tree must be identified before its complete census can be used as a regional baseline.

The full census will therefore be imported incrementally with these fields: path, member count, known file magic where published, role, target evidence, source, and confidence. Unknown roles remain unknown.

## Cross-game structural differences already established

The first public-source comparison shows that several logical subsystems move between BW and B2W2:

| Subsystem | Black / White | Black 2 / White 2 |
| --- | --- | --- |
| In-game scripts | `/a/0/5/7` | `/a/0/5/6` |
| Trainer metadata | `/a/0/9/2` | `/a/0/9/1` |
| Trainer parties | `/a/0/9/3` | `/a/0/9/2` |
| Overworld/events | `/a/1/2/5` | `/a/1/2/6` |
| Wild encounters | `/a/1/2/6` | `/a/1/2/7` |

This is why B2W2 must not be treated as a data-compatible "expanded BW" without per-subsystem verification.

## Known source conflict

PPRE's legacy `nds/files.py` maps Black 2 trainer and encounter paths as if they matched Black (`/a/0/9/2`, `/a/0/9/3`, `/a/1/2/6`). Later B2W2 research and tools instead identify trainer metadata/parties as `/a/0/9/1` and `/a/0/9/2`, and encounters as `/a/1/2/7`, with `/a/1/2/6` used for overworld data.

Do not silently resolve this conflict. The B2W2 repositories record the corrected/corroborated mapping while preserving PPRE as evidence of an older implementation mismatch.

## Source anchors

- Project Pokémon Black Raw DB: https://projectpokemon.org/rawdb/black/narc.php
- Project Pokémon Black Raw DB index: https://projectpokemon.org/rawdb/black/
- PPRE `nds/files.py`: https://github.com/projectpokemon/PPRE/blob/master/nds/files.py
- PPRE `pokeversion.py`: https://github.com/projectpokemon/PPRE/blob/master/pokeversion.py
- B/W Trainer Editor research: https://projectpokemon.org/home/forums/topic/12078-bw-trainer-editor/
- B/W overworld/script research: https://projectpokemon.org/home/forums/topic/21641-pok%C3%A9mon-black-and-white-overworlds-and-scripts/
- BW translation project: https://projectpokemon.org/home/forums/topic/10741-pok%C3%A9mon-black-and-white-translation-project-v3-project-is-complete/
- TrainerTyrant: https://github.com/ThirdLemon/TrainerTyrant
- B2W2 General ROM Info (comparison source): https://projectpokemon.org/home/forums/topic/22629-b2w2-general-rom-info/
- ROM-content cross-reference: https://whackahack.com/foro/threads/guia-nds-informacion-sobre-el-contenido-de-cada-rom-proceso.32504/

## Next work

1. Identify the exact region/revision represented by Project Pokémon's Black Raw DB tree.
2. Import the complete archive census without inventing semantic roles.
3. Cross-check each named path against at least one independent implementation or format analysis.
4. Split text, script, trainer, encounter, map, graphics, and audio formats into dedicated documents only when concrete research material exists.
5. Compare the Japanese baseline against every regional build once region-specific file-tree evidence is available.