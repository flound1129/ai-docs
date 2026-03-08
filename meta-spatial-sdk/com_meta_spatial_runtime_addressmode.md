# AddressMode Enum

Enum class representing the addressing mode for texture coordinates outside an image.

This enum defines how to handle texture coordinates that fall outside the range of 0, 1 for U and V axes. Visualizations of these functions can be found [here](https://vulkan-tutorial.com/Texture_mapping/Image_view_and_sampler) .

## Signature

```kotlin
enum AddressMode : Enum<AddressMode>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| REPEAT | Repeat the texture. When the texture coordinate is outside the range of 0, 1, this mode will use pixels from the opposite edge of the texture. |
| MIRRORED_REPEAT | Mirrored repeat of the texture. Similar to [AddressMode.REPEAT](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_addressmode#repeat) , but mirrors the repeated texture outside the range of 0, 1. This ensures the use of pixels on the same side of the texture as the edge. |
| CLAMP_TO_EDGE | Clamp the texture coordinates to the edge of the texture. When the texture coordinate is outside the range of 0, 1, this mode will take the value of the pixel closest to the edge of the texture. |

## Properties

| **mode** : Int [Get] | Signature ```kotlin val mode: Int ``` |
| --- | --- |