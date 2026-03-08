# MRUKWallTexCoordModeU Enum

The texture coordinate mode for walls U channel.

## Signature

```kotlin
enum MRUKWallTexCoordModeU : Enum<MRUKWallTexCoordModeU>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| METRIC | The texture coordinates start at 0 and increase by 1 unit every meter. |
| METRIC_SEAMLESS | The texture coordinates start at 0 and increase by 1 unit every meter but are adjusted to end on a whole number to avoid seams. |
| MAINTAIN_ASPECT_RATIO | The texture coordinates are adjusted to the other dimensions to ensure the aspect ratio is maintained. |
| MAINTAIN_ASPECT_RATIO_SEAMLESS | The texture coordinates are adjusted to the other dimensions to ensure the aspect ratio is maintained but are adjusted to end on a whole number to avoid seams. |
| STRETCH | The texture coordinates range from 0 to 1. |
| STRETCH_SECTION | The texture coordinates start at 0 and increase to 1 for each individual wall section. |