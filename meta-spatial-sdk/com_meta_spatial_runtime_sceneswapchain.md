# SceneSwapchain Class

*Modifiers:
final*

Represents a swapchain for rendering Layers. Multiple [SceneLayer](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenelayer) s can sample from a single SceneSwapchain

A swapchain is a collection of buffers used for rendering in graphics APIs. It manages the presentation of rendered content to the display and provides surfaces that can be used for drawing.

## Signature

```kotlin
class SceneSwapchain
```

## Constructors

| **SceneSwapchain** ( handle ) | Signature ```kotlin constructor(handle: Long) ``` Parameters handle: Long Returns [SceneSwapchain](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sceneswapchain) |
| --- | --- |

## Properties

| **handle** : Long [Get] | Signature ```kotlin var handle: Long ``` |
| --- | --- |

## Functions

| **destroy** () | Signature ```kotlin fun destroy() ``` |
| --- | --- |
| **getSurface** () | Gets the Android Surface associated with this swapchain. The returned Surface can be used for drawing content that will be displayed through this swapchain. Signature ```kotlin fun getSurface(): Surface? ``` Returns Surface? The Android Surface for drawing, or null if no surface is available |
| **nativeHandle** () | Signature ```kotlin fun nativeHandle(): Long ``` Returns Long |
| **platformHandle** () | Signature ```kotlin fun platformHandle(): Long ``` Returns Long |
| **updateSampler** ( sampler ) | Updates the sampler configuration for this swapchain. The sampler controls how textures are filtered and addressed when rendered. Signature ```kotlin fun updateSampler(sampler: SamplerConfig) ``` Parameters sampler: [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) The sampler configuration to apply |

## Companion Object

### Companion Object Functions

| **create** ( width , height , numberOfMips ) | Creates a standard swapchain for rendering. This type of swapchain is suitable for general rendering purposes and can be used with SceneLayer objects. Signature ```kotlin fun create(width: Int, height: Int, numberOfMips: Int): SceneSwapchain ``` Parameters width: Int Width of the swapchain in pixels height: Int Height of the swapchain in pixels numberOfMips: Int Number of mipmap levels to generate (1 for no mipmaps) Returns [SceneSwapchain](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sceneswapchain) A new standard swapchain |
| --- | --- |
| **createAsAndroid** ( width , height , isProtected ) | Creates a swapchain that is automatically updated when the associated Android `Surface` is updated. This is what is used in "direct-to-compositor" layer Panels and will be used when you do not require a [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) . It is generally a more performant option and optionally allows for secure/DRM content to be played. Signature ```kotlin fun createAsAndroid(width: Int, height: Int, isProtected: Boolean = false): SceneSwapchain ``` Parameters width: Int Width of the swapchain in pixels height: Int Height of the swapchain in pixels isProtected: Boolean Whether the swapchain should use protected content. This is a requirement for DRM. Returns [SceneSwapchain](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sceneswapchain) A new Android-compatible swapchain |