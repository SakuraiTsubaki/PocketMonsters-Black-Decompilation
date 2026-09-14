# Regional Survey Matrix — Pokémon Black

## Purpose

Track every officially released regional, territorial, language, packaging, and revision target of Pokémon Black against the original Japanese release baseline.

The matrix is intentionally evidence-first. Do not fill unknown fields from memory or assumption. Use `Unknown` until a source is found.

## Baseline policy

- Baseline axis: original Japanese retail release.
- Every non-Japanese build is compared directly against the Japanese baseline.
- Non-Japanese builds are also cross-compared where necessary.
- Revisions are separate records.
- Language, territory, cartridge identity, release date, revision, packaging, and technical differences must not be conflated.
- "International" is not a valid substitute for enumerating individual official builds.

## Build inventory

| Record ID | Version | Territory / market | Language | Release date | Revision | Product / cart code | Known hashes | Evidence status | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BLACK-JP-BASE | Black | Japan | Japanese | 2010-09-18 | Public catalogue: v0; project verification pending | `TWL-IRBJ-JPN` / `IRBJ` | Public reference: CRC32 `7dc488b6`; MD5 `76a3c13e58b22e1bd434d596c33ea2da`; SHA-1 `f63a498dea7569207fe7dab702808e69f16d928d` | Release/product identity corroborated; bytes not project-verified | Nintendo JP; GameFAQs; GameTDB |
| BLACK-EU-EN | Black | Europe | English | 2011-03-04 | Unknown | `TWL-IRBO-EUR` / `IRBO` | Unknown | Product/release catalogued | Nintendo Europe; GameFAQs |
| BLACK-EU-FR | Black | France / Europe | French | 2011-03-04 | Unknown | `TWL-IRBF-FRA` / `IRBF` | Unknown | Product/release catalogued | GameFAQs; French catalogue/manual records |
| BLACK-EU-DE | Black | Germany / Europe | German | 2011-03-04 | Unknown | `TWL-IRBD-NOE` / `IRBD` | Unknown | Product/release catalogued | GameFAQs |
| BLACK-EU-IT | Black | Italy / Europe | Italian | 2011-03-04 | Unknown | `TWL-IRBI-ITA` / `IRBI` | Unknown | Product/release catalogued | GameFAQs; collector catalogue |
| BLACK-EU-ES | Black | Spain / Europe | Spanish | 2011-03-04 | Unknown | `TWL-IRBS-ESP` / `IRBS` | Unknown | Product/release catalogued | GameFAQs |
| BLACK-US-EN | Black | United States | English | 2011-03-06 | Unknown | `TWL-IRBO-USA` / `IRBO` | Unknown | Release corroborated; exact bytes pending | Nintendo of America press material; GameFAQs |
| BLACK-CA-EN | Black | Canada | English | 2011-03-06 | Unknown | `TWL-IRBO-USA` retail record | Unknown | Packaging/catalogue record; byte identity pending | GameFAQs |
| BLACK-AU-EN | Black | Australia | English | 2011-03-10 | Unknown | `TWL-IRBO-AUS` / `IRBO` | Unknown | Product/release catalogued | GameFAQs |
| BLACK-KR | Black | South Korea | Korean | 2011-04-21 | Public catalogue: v0; project verification pending | `TWL-IRBK-KOR` / `IRBK` | Public reference: CRC32 `20c84d02`; MD5 `2c762942b4b39f4adca40a6cc8e6de57`; SHA-1 `6be0d2e4fa8ed04724849f6d492d3847f66e5adc` | Product/release corroborated; bytes not project-verified | Korean release coverage; GameFAQs; GameTDB |
| BLACK-HK | Black | Hong Kong | Japanese / TBD | Unknown | Unknown | Unknown | Unknown | Official territory support confirmed later; retail build identity unresolved | Nintendo Hong Kong NWC service list |
| BLACK-TW | Black | Taiwan | Japanese / TBD | Unknown | Unknown | Unknown | Unknown | Research target | Pending primary/preservation evidence |
| BLACK-NZ | Black | New Zealand | English / TBD | Unknown | Unknown | Unknown | Unknown | Research target | Pending primary/preservation evidence |
| BLACK-SG | Black | Singapore / officially served Asian markets | English/Japanese / TBD | Unknown | Unknown | Unknown | Unknown | Research target | Pending primary/preservation evidence |

### Immediate unresolved territory/build questions

- Determine whether Hong Kong and Taiwan retail distribution used the Japanese `IRBJ` build unchanged or had territory-specific packaging/manual material only.
- Determine whether New Zealand used the Australian `IRBO` build unchanged.
- Determine Canadian French packaging/manual/cart relationships; do not assume FRA cartridge identity from packaging alone.
- Enumerate any additional officially served Asian markets with primary or preservation evidence.
- Enumerate every known revision for each row before declaring a build inventory complete.

## Difference matrix

| Build ID | Category | Japanese baseline state | Regional state | Difference class | Evidence level | Source(s) | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BLACK-EU-FR / DE / IT / ES | language/build identity | Japanese `IRBJ` | Separate language-specific game codes (`IRBF`, `IRBD`, `IRBI`, `IRBS`) | text / localization / encoding; potentially other technical differences | Corroborated for product identity; technical diff pending | GameFAQs and independent retail/catalogue records | Separate game codes establish distinct targets, but do not by themselves enumerate byte-level differences. |
| BLACK-KR | language/build identity | Japanese `IRBJ` | Korean `IRBK` | text / localization / encoding; fonts/glyphs; potentially other technical differences | Corroborated for product identity; technical diff pending | GameFAQs; GameTDB | Korean target must be analyzed independently rather than folded into an international build. |
| BLACK-US-EN / BLACK-EU-EN / BLACK-AU-EN | territory/build identity | Japanese `IRBJ` | Shared `IRBO` game-code family with different retail suffixes | unclassified until byte comparison evidence exists | Corroborated for retail identity | Nintendo/secondary catalogues | Shared game code does not prove byte identity across USA/EUR/AUS. |

### Difference classes

- executable / ARM9 / ARM7
- overlay
- filesystem / NitroFS
- NARC membership / ordering / format
- Pokémon / personal data
- moves / abilities / items
- encounters
- trainers / AI / battle rules
- maps / matrices / warps / objects
- scripts / flags / variables / events
- text / localization / encoding
- fonts / glyphs
- graphics / sprites / UI / models
- audio / music / SFX
- save structure / checksums
- wireless / infrared / Wi-Fi
- C-Gear / Entralink / Game Sync / Global Link
- Mystery Gift / external distribution
- unused / dummy / debug content
- bug / glitch / revision fix
- legal / ratings / censorship / localization adaptation
- packaging / manual / non-ROM material
- unclassified

## Evidence levels

- **Official** — official first-party material directly supports the claim.
- **Direct technical** — public code, extracted data, disassembly, or format implementation directly demonstrates the claim.
- **Corroborated** — two or more independent reliable sources agree.
- **Single-source** — one credible source exists but independent confirmation is pending.
- **Reported** — claim exists but technical verification is insufficient.
- **Unknown** — no adequate evidence yet.

## Source anchors

- https://www.nintendo.co.jp/ds/irbj/index.html
- https://www.pokemon.co.jp/series/bw/
- https://www.nintendo.com/en-gb/News/2011/Pokemon-Black-Version-and-Pokemon-White-Version-arrive-in-Europe-March-4th--253463.html
- https://gamefaqs.gamespot.com/ds/989552-pokemon-black-version/data
- https://www.gametdb.com/DS/IRBJ
- https://www.gametdb.com/DS/IRBK
- https://www.nintendo.com/hk/pressrelease/wifi_20140227.html

## Comparison rule

A localized text difference is not automatically a complete technical-ROM difference description; record the text difference, then separately record any encoding, font, archive-layout, script, executable, or resource change that makes it technically distinct.

Likewise, a regional bug fix must be recorded as a regional/revision implementation difference rather than generalized as a Generation V rule unless evidence shows it applies to all builds.