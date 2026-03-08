# PanelSurface Class

*Modifiers:
final*

Manages the rendering surface for panels in 3D space.

PanelSurface creates and manages the underlying Android Surface, texture, and swapchain resources needed to render panel content. It serves as the bridge between Android's 2D rendering system and the 3D scene.

## Signature

```kotlin
class PanelSurface(scene: Scene, val widthInPx: Int, val heightInPx: Int, val mips: Int, val samplerConfig: SamplerConfig = PanelConfigOptions.DEFAULT_PANEL_SAMPLER, val useSwapchain: Boolean, val useTexture: Boolean, val fragmentShader: String = "", val isProtected: Boolean = false)
```

## Constructors

| **PanelSurface** ( scene , widthInPx , heightInPx , mips , samplerConfig , useSwapchain , useTexture , fragmentShader , isProtected ) | Signature ```kotlin constructor(scene: Scene, widthInPx: Int, heightInPx: Int, mips: Int, samplerConfig: SamplerConfig = PanelConfigOptions.DEFAULT_PANEL_SAMPLER, useSwapchain: Boolean, useTexture: Boolean, fragmentShader: String = "", isProtected: Boolean = false) ``` Parameters scene: [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) widthInPx: Int Width of the surface in pixels heightInPx: Int Height of the surface in pixels mips: Int samplerConfig: [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) useSwapchain: Boolean useTexture: Boolean fragmentShader: String isProtected: Boolean Whether the surface is protected (for DRM content) Returns [PanelSurface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelsurface) |
| --- | --- |

## Properties

| **fragmentShader** : String [Get] | Signature ```kotlin val fragmentShader: String ``` |
| --- | --- |
| **heightInPx** : Int [Get] | Height of the surface in pixels Signature ```kotlin val heightInPx: Int ``` |
| **isProtected** : Boolean [Get] | Whether the surface is protected (for DRM content) Signature ```kotlin val isProtected: Boolean = false ``` |
| **mips** : Int [Get] | Signature ```kotlin val mips: Int ``` |
| **samplerConfig** : [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) [Get] | Signature ```kotlin val samplerConfig: SamplerConfig ``` |
| **surface** : Surface? [Get][Set] | The Android Surface object for rendering Signature ```kotlin var surface: Surface ``` |
| **swapchain** : [SceneSwapchain?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sceneswapchain) [Get][Set] | The SceneSwapchain for efficient rendering (if enabled) Signature ```kotlin var swapchain: SceneSwapchain? ``` |
| **texture** : [SceneTexture?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) [Get][Set] | The SceneTexture for texture-based rendering (if enabled) Signature ```kotlin var texture: SceneTexture? ``` |
| **useSwapchain** : Boolean [Get] | Signature ```kotlin val useSwapchain: Boolean ``` |
| **useTexture** : Boolean [Get] | Signature ```kotlin val useTexture: Boolean ``` |
| **widthInPx** : Int [Get] | Width of the surface in pixels Signature ```kotlin val widthInPx: Int ``` |

## Functions

| **destroy** () | Signature ```kotlin fun destroy() ``` |
| --- | --- |