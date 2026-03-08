# MRUKWallTexCoordModeV Enum

The texture coordinate mode for walls V channel.

## Signature

```kotlin
enum MRUKWallTexCoordModeV : Enum<MRUKWallTexCoordModeV>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| METRIC | The texture coordinates start at 0 and increase by 1 unit every meter. |
| MAINTAIN_ASPECT_RATIO | The texture coordinates are adjusted to the other dimensions to ensure the aspect ratio is maintained. |
| STRETCH | The texture coordinates range from 0 to 1. |