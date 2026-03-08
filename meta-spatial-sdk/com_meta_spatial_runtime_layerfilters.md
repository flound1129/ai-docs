# LayerFilters Object

Provides constants for different layer filter configurations used in spatial rendering.

This object defines various bit flags that represent different sampling and sharpening configurations. These constants can be used to configure rendering layers with specific quality settings.

Example:

This example demonstrates how to set the layer filter to use normal super sampling and quality sharpening inside of your panel registration.

```kotlin LayerConfig(filters = layerFilters.NORMAL_SUPER_SAMPLING or layerFilters.QUALITY_SHARPENING) ```

See docs for [mobile OpenXR composition layer filtering](https://developers.meta.com/horizon/documentation/native/android/mobile-openxr-composition-layer-filtering) .

## Signature

```kotlin
object LayerFilters
```

## Properties

| **AUTO_FILTER** : Int [Get] | This bit indicates compositor may automatically toggle a texture filtering mechanism to improve visual quality of layer. This must not be the only bit set. Signature ```kotlin val AUTO_FILTER: Int ``` |
| --- | --- |
| **DEFAULT_QUALITY** : Int [Get] | Represents the default quality setting. This combines quality sharpening, normal super sampling, and automatic filter selection. Signature ```kotlin val DEFAULT_QUALITY: Int ``` |
| **HIGHEST_QUALITY** : Int [Get] | Represents the highest quality setting. This combines quality sharpening and quality super sampling. Signature ```kotlin val HIGHEST_QUALITY: Int ``` |
| **NORMAL_SHARPENING** : Int [Get] | This bit utilizes an efficient three-tap sharpening algorithm, which alters the sampling pattern every other frame to approximate a more computationally expensive five-tap filter. Signature ```kotlin val NORMAL_SHARPENING: Int ``` |
| **NORMAL_SUPER_SAMPLING** : Int [Get] | This bit enables an efficient two-tap filter which alters the sampling pattern every other frame to approximate a more computationally expensive four-tap filter. For most use cases, the quality is indistinguishable from the four-tap filter with reduced computation costs. Signature ```kotlin val NORMAL_SUPER_SAMPLING: Int ``` |
| **QUALITY_SHARPENING** : Int [Get] | This bit utilizes Meta Quest Super Resolution (MQSR) which is a single-pass spatial upscaling and sharpening technique optimized to run on Meta Quest devices. Signature ```kotlin val QUALITY_SHARPENING: Int ``` |
| **QUALITY_SUPER_SAMPLING** : Int [Get] | This bit enables a more expensive four-tap filter which performs conventional supersampling with no temporal component. Signature ```kotlin val QUALITY_SUPER_SAMPLING: Int ``` |