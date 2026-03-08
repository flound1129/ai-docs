# Filter Enum

Enum class representing the filtering modes for texture sampling.

This enum defines how to calculate the final color value when sampling a texture at a specific address.

## Signature

```kotlin
enum Filter : Enum<Filter>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| NEAREST | Nearest-neighbor filtering. This mode takes the value of the pixel closest to the address being sampled. It does not perform any interpolation, resulting in a more pixelated appearance. |
| LINEAR | Linear filtering. This mode linearly interpolates the values of the pixels closest to the address being sampled. It provides a smoother appearance than nearest-neighbor filtering. |

## Properties

| **filter** : Int [Get] | Signature ```kotlin val filter: Int ``` |
| --- | --- |