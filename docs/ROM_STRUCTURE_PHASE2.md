# Pokémon Black EUR raw-input structure census — Phase 2

This phase directly inventories the immutable local raw input without exporting
or committing any ROM bytes.

## Evidence scope

- Input role: observed raw input, not canonical-clean verification
- Internal title: `POKEMON B`
- Game code: `IRBO`
- Maker code: `01`
- Unit code: `0x02` (NDSi Enhanced)
- Revision: `0`
- Size: `268435456` bytes
- SHA-1: `a68b3bedf5c1e53556e41e59cdf396c20b331896`
- SHA-256: `2e40416b8e8183d936084c7be0adeaab4fa3f786a68f90d7291ab77d340f0c1d`

The input does not match the repository's separately registered canonical-clean
USA/Europe v1.0 hash. Results in this phase therefore remain classified as
direct observations of the raw input until reproduced against the clean target.

## Container and executable census

| Structure | Count |
| --- | ---: |
| FAT entries | 484 |
| FNT directories | 31 |
| Named NitroFS files | 247 |
| ARM9 overlays | 237 |
| ARM9 overlays marked compressed | 229 |
| NARC archives | 237 |
| NARC members | 54,054 |

The FAT entries with IDs `0` through `236` are the 237 ARM9 overlay files.
They are intentionally absent from the named FNT tree. The named NitroFS range
begins at file ID `237`; this is not evidence of missing filenames.

## DSi executable regions

| Region | ROM offset | RAM address | Size |
| --- | ---: | ---: | ---: |
| ARM9i | `0x0C403000` | `0x02400000` | 77,604 bytes |
| ARM7i | `0x0C416000` | `0x02E80000` | 291,064 bytes |

The NTR used-ROM-size field must not be treated as the end of all meaningful
content because the DSi-enhanced executable and digest regions occur later in
the cartridge image.

## Recognized NARC member signatures

| Format | Members |
| --- | ---: |
| Unknown/unresolved | 29,116 |
| LZ11 | 10,799 |
| NCLR | 4,232 |
| NCER | 3,274 |
| NCGR | 1,880 |
| LZ10 | 1,523 |
| BTX0 | 1,341 |
| NSCR | 503 |
| BMD0 | 413 |
| NANR | 314 |
| BCA0 | 258 |
| BTA0 | 187 |
| BTP0 | 112 |
| BMA0 | 69 |
| BVA0 | 31 |
| SDAT | 2 |

`Unknown/unresolved` is a format-identification state, not an unused-content
classification. These members require archive-path semantics and record-level
parsers before any gameplay-use conclusion is made.

## Reproducible outputs

- `manifests/black-structure-summary.json`
- `manifests/black-arm9-overlays.csv`
- `manifests/black-narc-census.csv`
- `manifests/black-narc-inner-formats.csv`
- `tools/build_black_structure_census.py`

The overlay and NARC manifests include offsets, sizes and cryptographic hashes
but contain no retail ROM payload bytes.

## Next phase

1. Resolve every `a/x/y/z` archive path to a subsystem and confidence level.
2. Add recursive classification for LZ10/LZ11 members after decompression.
3. Split graphics, text, scripts, maps, encounters, battle data and audio into
   reversible extraction/rebuild pipelines.
4. Compare each promoted result against the canonical-clean target and the
   independently maintained White workspace.
