# Version Coverage

Use this document as the authoritative inventory of game versions targeted by this decompilation project.

The project has no local retail ROM baseline. Entries below therefore distinguish **release/product identity documented from public sources** from byte-level verification. A public catalogue hash is a research lead, not a project-level `Matched` result.

## Japanese baseline

| Status | Region / territory | Language | Revision / update | Product / build identifier | Release | Hashes | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Planned | Japan | Japanese | Public catalogues report version 0; project verification pending | `TWL-IRBJ-JPN` / game code `IRBJ` | 2010-09-18 | Public reference: CRC32 `7dc488b6`, MD5 `76a3c13e58b22e1bd434d596c33ea2da`, SHA-1 `f63a498dea7569207fe7dab702808e69f16d928d` | **Canonical survey baseline.** Release date is confirmed by Nintendo/Pokémon official material. Hashes come from GameTDB and are not yet independently verified by this project. |

## Regional / language targets

| Status | Region / territory | Language | Revision / update | Product / build identifier | Release | Hashes | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Planned | Europe | English | TBD | `TWL-IRBO-EUR` / `IRBO` | 2011-03-04 | TBD | Nintendo Europe confirms Europe-wide launch date. |
| Planned | France / Europe | French | TBD | `TWL-IRBF-FRA` / `IRBF` | 2011-03-04 | TBD | Distinct French software identifier; do not merge with English build. |
| Planned | Germany / Europe | German | TBD | `TWL-IRBD-NOE` / `IRBD` | 2011-03-04 | TBD | Distinct German software identifier. |
| Planned | Italy / Europe | Italian | TBD | `TWL-IRBI-ITA` / `IRBI` | 2011-03-04 | TBD | Distinct Italian software identifier. |
| Planned | Spain / Europe | Spanish | TBD | `TWL-IRBS-ESP` / `IRBS` | 2011-03-04 | TBD | Distinct Spanish software identifier. |
| Planned | United States | English | TBD | `TWL-IRBO-USA` / `IRBO` | 2011-03-06 | TBD | North American launch date confirmed by Nintendo of America press material preserved by third parties. Compare against EUR English despite shared game code. |
| Planned | Canada | English | TBD | `TWL-IRBO-USA` packaging/catalogue record | 2011-03-06 | TBD | Separate Canadian retail/barcode record exists; software-byte identity with US build still to verify. French-Canadian packaging/build relationship remains a research target. |
| Planned | Australia | English | TBD | `TWL-IRBO-AUS` / `IRBO` | 2011-03-10 | TBD | Separate Australian retail identifier; compare against US/EUR English. |
| Planned | South Korea | Korean | Public catalogues report version 0; project verification pending | `TWL-IRBK-KOR` / `IRBK` | 2011-04-21 | Public reference: CRC32 `20c84d02`, MD5 `2c762942b4b39f4adca40a6cc8e6de57`, SHA-1 `6be0d2e4fa8ed04724849f6d492d3847f66e5adc` | Korean release date/product identity is independently catalogued; hashes from GameTDB remain public-reference evidence only. |
| Planned | Hong Kong | Japanese / TBD | TBD | TBD | TBD | TBD | Nintendo Hong Kong later lists Black among supported DS software. Determine whether retail distribution used the Japanese build unchanged and document packaging/manual differences. |
| Planned | Taiwan | Japanese / TBD | TBD | TBD | TBD | TBD | Territory/build identity requires dedicated archival research; do not assume a separate executable build. |
| Planned | New Zealand | English / TBD | TBD | TBD | TBD | TBD | Determine whether Australian or another English build was officially distributed. |
| Planned | Singapore / other officially served Asian markets | English/Japanese / TBD | TBD | TBD | TBD | TBD | Research target; require official or preservation evidence before defining a build. |

## Current source anchors

- Nintendo Japan product page: https://www.nintendo.co.jp/ds/irbj/index.html
- Pokémon official BW site: https://www.pokemon.co.jp/series/bw/
- Nintendo Europe launch notice: https://www.nintendo.com/en-gb/News/2011/Pokemon-Black-Version-and-Pokemon-White-Version-arrive-in-Europe-March-4th--253463.html
- GameFAQs release/product catalogue: https://gamefaqs.gamespot.com/ds/989552-pokemon-black-version/data
- GameTDB Japanese entry: https://www.gametdb.com/DS/IRBJ
- GameTDB Korean entry: https://www.gametdb.com/DS/IRBK
- Nintendo Hong Kong NWC service list: https://www.nintendo.com/hk/pressrelease/wifi_20140227.html

## Status vocabulary

- **Planned** — target is in scope; identity may be partly documented, but project-level build verification is not complete.
- **Verified** — exact target identity and hashes have been independently confirmed under the repository verification rules.
- **Mapped** — executable/data layout documented for that exact target.
- **In progress** — active source reconstruction.
- **Matched** — reconstruction verified against the exact target using a defined matching criterion.
- **Reference only** — used for comparison but not a reconstruction target.

## Recording rules

1. The Japanese release is the starting comparison baseline, not an assumption that later regional revisions are inferior.
2. Record exact revision/update information whenever known; use `TBD` when it is not.
3. Prefer cryptographic hashes over filenames as identity evidence, but distinguish public-reference hashes from project-verified hashes.
4. Do not commit retail game images, decrypted game images, console keys, or ROM binaries.
5. Record regional, territory, packaging, language, and revision differences instead of assuming releases are identical.
6. If two territories appear to share a game code, byte identity still requires verification.
7. Link version-specific findings to relevant documentation, manifests, or verification records.