# Clean Reference — Pokémon Black Version (USA/Europe v1.0)

This repository separates the **canonical clean reference** from the locally supplied ROM used for the first direct structural scan. The retail ROM binary itself is never committed.

## Canonical clean reference

- Region: USA/Europe
- Version: 1.0
- Mode: NDSi Enhanced
- Size: `268435456` bytes
- CRC32: `4F6E5580`
- MD5: `37BFF1431EDA9B3A525737C7F59A432D`
- SHA-1: `26AD0B9967AA279C4A266EE69F52B9B2332399A5`

This is the reconstruction/verification target for USA/Europe v1.0 work. It is independently used as the build target by the public Pokémon Black decompilation project.

## Local raw input used for the initial direct scan

- Filename: `Pokemon.Black.Version.EUR.NDS-SweeTnDs.nds`
- Internal title: `POKEMON B`
- Game code: `IRBO`
- Revision field: `0`
- Unit code: `0x02`
- CRC32: `E2BEE619`
- MD5: `F45FD94BB761721E30BD3A0A4FDE124A`
- SHA-1: `A68B3BEDF5C1E53556E41E59CDF396C20B331896`
- SHA-256: `2E40416B8E8183D936084C7BE0ADEAAB4FA3F786A68F90D7291AB77D340F0C1D`
- Canonical clean match: **No**

The raw input remains useful as an immutable analysis input, but observations obtained from it must not be silently promoted to canonical-clean verification. Canonical-sensitive results must be reverified against the clean reference or a source reconstruction that builds to it.

## Reference rules

1. Never commit retail `.nds` binaries.
2. Keep canonical clean identity and raw-input identity in separate manifests.
3. Preserve Black/White and region/revision differences; do not normalize them away.
4. Mark evidence as `Observed raw input`, `Canonical verified`, or `External corroboration` as appropriate.
5. Extracted/reconstructed source, tools, metadata, manifests, documentation, patches, and reviewable assets may be committed.
6. Prefer reproducible extraction/rebuild paths over opaque binary dumps.

## Initial raw-input structural observation

- FAT entries: **484**
- Named NitroFS files: **247**
- NARC archives: **237**
- ARM9 overlays: **237**

These counts were directly observed from the local raw input. The current next phase is to align those structural findings with the canonical Black decompilation/build reference and promote each subsystem to canonical-verified status.
