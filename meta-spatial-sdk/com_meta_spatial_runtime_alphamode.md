# AlphaMode Enum

Enum class representing the alpha modes for rendering.

This enum defines how the alpha channel of a texture or color is interpreted and applied during rendering.

## Signature

```kotlin
enum AlphaMode : Enum<AlphaMode>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| OPAQUE | The material is completely opaque and doesn't use the alpha channel. This means that the alpha value is ignored, and the material is rendered as fully opaque. |
| TRANSLUCENT | This mode uses the alpha channel to blend the material with the background, but doesn't write to the depth buffer. As a result, it is rendered last to ensure correct blending. |
| MASKED | In this mode, the alpha channel is used to decide whether a pixel is completely opaque or transparent. |
| ADDITIVE | This mode adds the RGBA channels together. Note that additive materials don't write to the depth buffer. |
| NONE | The material is completely transparent and doesn't affect the rendering output. |
| TRANSLUCENT_POST | The material is completely transparent and renders the material late in the render process. |
| HOLE_PUNCH | Full explanation [here](https://developers.meta.com/horizon/documentation/spatial-sdk/spatial-sdk-2dpanel-layers#technical-explanation) . |
| TRANSLUCENT_HOLE_PUNCH | uses the alpha channel to blend and doesn't write to the depth buffer (rendered last), and also reverses alpha to enable the overlay layer |
| MASKED_HOLE_PUNCH | In this mode, alpha to coverage is used for the alpha channel is used to decide whether a sample is completely opaque or transparent. However, the alpha is written to 0 to enable the overlay layer. |

## Properties

| **mode** : Int [Get] | Signature ```kotlin val mode: Int ``` |
| --- | --- |

## Companion Object

### Companion Object Functions

| **fromInt** ( mode ) | Returns the alpha mode corresponding to the given integer value. Signature ```kotlin fun fromInt(mode: Int): AlphaMode ``` Parameters mode: Int the integer value of the alpha mode Returns [AlphaMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_alphamode) the alpha mode corresponding to the given integer value Throws IllegalArgumentException if the given integer value does not correspond to a valid alpha mode |
| --- | --- |