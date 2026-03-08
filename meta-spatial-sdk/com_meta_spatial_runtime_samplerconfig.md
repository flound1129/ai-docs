# SamplerConfig Class

*Modifiers:
final*

Data class representing a sampler configuration.

This class holds various parameters that control how a texture is sampled in a shader. Visualizations of these functions can be found [here](https://vulkan-tutorial.com/Texture_mapping/Image_view_and_sampler) .

## Signature

```kotlin
data class SamplerConfig(val minFilter: Filter = Filter.LINEAR, val magFilter: Filter = Filter.LINEAR, val mipmapMode: Filter = Filter.LINEAR, val addressModeU: AddressMode = AddressMode.REPEAT, val addressModeV: AddressMode = AddressMode.REPEAT, val lodBias: Float = 0.0f)
```

## Constructors

| **SamplerConfig** ( minFilter , magFilter , mipmapMode , addressModeU , addressModeV , lodBias ) | Signature ```kotlin constructor(minFilter: Filter = Filter.LINEAR, magFilter: Filter = Filter.LINEAR, mipmapMode: Filter = Filter.LINEAR, addressModeU: AddressMode = AddressMode.REPEAT, addressModeV: AddressMode = AddressMode.REPEAT, lodBias: Float = 0.0f) ``` Parameters minFilter: [Filter](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_filter) magFilter: [Filter](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_filter) mipmapMode: [Filter](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_filter) addressModeU: [AddressMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_addressmode) addressModeV: [AddressMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_addressmode) lodBias: Float Returns [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) |
| --- | --- |

## Properties

| **addressModeU** : [AddressMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_addressmode) [Get] | Addressing mode for U texture coordinates outside the range of 0, 1. Signature ```kotlin val addressModeU: AddressMode ``` |
| --- | --- |
| **addressModeV** : [AddressMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_addressmode) [Get] | Addressing mode for V texture coordinates outside the range of 0, 1. Signature ```kotlin val addressModeV: AddressMode ``` |
| **lodBias** : Float [Get] | Bias value added to the LOD (Level of Detail) calculation in the shader. Negative values result in a slightly sharper image. Positive values will allow detail to be lowered when far away. Signature ```kotlin val lodBias: Float = 0.0f ``` |
| **magFilter** : [Filter](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_filter) [Get] | Filter mode for magnification (when texel coverage is finer than pixel coverage). Signature ```kotlin val magFilter: Filter ``` |
| **minFilter** : [Filter](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_filter) [Get] | Filter mode for minification (when texel coverage is coarser than pixel coverage). Signature ```kotlin val minFilter: Filter ``` |
| **mipmapMode** : [Filter](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_filter) [Get] | Filter mode for mipmapping (when texel coverage is between mipmap levels). Signature ```kotlin val mipmapMode: Filter ``` |