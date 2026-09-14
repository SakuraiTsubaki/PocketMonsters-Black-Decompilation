# Canonical Alignment — Phase 1

This phase distinguishes whole-ROM identity from component identity.

## References

- Canonical Black USA/Europe v1.0 SHA-1: `26AD0B9967AA279C4A266EE69F52B9B2332399A5`
- Local raw-input SHA-1: `A68B3BEDF5C1E53556E41E59CDF396C20B331896`
- Canonical build/source reference: `squiddonaut/pokeblack`

The whole-ROM hashes differ, so the local input is **not** the canonical clean ROM. However, direct component checks show that substantial core content is byte-identical to the canonical decompilation reference.

## Executable components checked

| Component | Local raw-input SHA-1 | Canonical reference SHA-1 | Result |
|---|---|---|---|
| ARM9 | `b1d62c124b481f22040a36781ae3ed0f3c622379` | `b1d62c124b481f22040a36781ae3ed0f3c622379` | exact |
| ARM7 | `364259352fffdcd15b75c2d9e997d2ed0d877190` | `364259352fffdcd15b75c2d9e997d2ed0d877190` | exact |
| ARM9 overlay table (`y9`) | `8cae26fb9868f389b33559ac22957d34cb64c281` | `8cae26fb9868f389b33559ac22957d34cb64c281` | exact |

## Core NitroFS files checked

| Path | Local SHA-1 | Canonical SHA-1 | Result |
|---|---|---|---|
| `a/0/0/2` | `2c1eb5a7733ea6e6ae92a13fe5ed29b9bb83a4d3` | same | exact |
| `a/0/0/3` | `d1856c43b55f23d8612959fa82e98f8e86329ca4` | same | exact |
| `a/0/1/6` | `0cc77c1d0d649c1c3daa7ad4d1aeeab2c63ce94b` | same | exact |
| `a/0/1/8` | `f1d190627b1e64e35fe82cee9633b33db0ee9b08` | same | exact |
| `a/0/1/9` | `5e20bbfe6d178b1372844dea6f5016d2b7e87b14` | same | exact |
| `a/0/2/1` | `8247cba4a422c66caa1f71d54775db09f742c5fd` | same | exact |
| `a/0/2/4` | `a6492550716ab4ed71f87224cb10eb8f7fe9fc9c` | same | exact |
| `a/0/5/7` | `dac45c1d751706e66237ee4fbd569b6bbf817802` | same | exact |
| `a/0/9/2` | `4f4b1251427a522e31acb24c72bacf5319bc2a2e` | same | exact |
| `a/0/9/3` | `296bd091f64065a3ae83b3d028b026a22e9d6979` | same | exact |

## All five Black/White-version-different NARCs checked

Every one of the five NARCs that differs between the supplied Black and White inputs matches the canonical Black file hash:

| Path | Canonical/local Black SHA-1 |
|---|---|
| `a/0/2/6` | `7c9bb86d8c84185afaef35238d6977cd308b869b` |
| `a/0/8/6` | `ae8eeffe2ab7961fe6ccf24440e1703637209b83` |
| `a/1/2/6` | `523858b7935f517bd4e06d36cbd9cfd14eb76b03` |
| `a/1/7/8` | `eb20c73d966edf4240cfedce618c6368a0536a11` |
| `a/2/3/1` | `1eb16bec8ababe007e531afc8b700f5ee4c77ce8` |

This means the first Black/White NARC-difference census is not merely an artifact of a modified Black NitroFS for these archives: the Black side is confirmed against the canonical Black decompilation file manifest.

## Overlay caveat

Do not compare every raw overlay FAT blob directly to the upstream `OVY_*.sbin` hash and label a mismatch as modification without first respecting the upstream overlay compression/decompression pipeline. Some raw overlay hashes match directly while others do not, so overlay normalization must be handled by the build rules before classification.

## Next promotion criteria

A subsystem is promoted from `Observed raw input` to `Canonical verified` when one of the following is satisfied:

1. Its extracted file hash matches the canonical Black manifest.
2. Its reconstructed source builds to the canonical component hash.
3. A format-specific reversible extraction/repack test reproduces the canonical file.

The next work proceeds archive-by-archive and source-module-by-source-module using these criteria.
