# ReadableMediaPanelRenderOptions Class

Implements
[PanelConfigOptionsModifier](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelconfigoptionsmodifier)
*Modifiers:
final*

Rendering configuration specific to post-processing supported media panels. These are useful for panels that can have shaders and supports transparency.

## Signature

```kotlin
data class ReadableMediaPanelRenderOptions(val mips: Int = 1, val stereoMode: StereoMode = StereoMode.None, val samplerConfig: SamplerConfig = PanelConfigOptions.DEFAULT_PANEL_SAMPLER, val renderMode: PanelRenderMode = PanelRenderMode.Layer(), val zIndex: Int = 0) : PanelConfigOptionsModifier
```

## Constructors

| **ReadableMediaPanelRenderOptions** ( mips , stereoMode , samplerConfig , renderMode , zIndex ) | Signature ```kotlin constructor(mips: Int = 1, stereoMode: StereoMode = StereoMode.None, samplerConfig: SamplerConfig = PanelConfigOptions.DEFAULT_PANEL_SAMPLER, renderMode: PanelRenderMode = PanelRenderMode.Layer(), zIndex: Int = 0) ``` Parameters mips: Int Number of mip levels to use for panel texture. Mipmapping is the process of generating lower resolution versions of a texture to display on panels when they are far away. stereoMode: [StereoMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_stereomode) The [StereoMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_stereomode) to use for the panel. samplerConfig: [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) The [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) to set the panel texture/layer. renderMode: [PanelRenderMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelrendermode) Control how the panel will render in the scene. Use layers to make panels appear crisp and high resolution, or mesh for basic rendering without compositor layers. zIndex: Int The zIndex to set the panel layer. Returns [ReadableMediaPanelRenderOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_readablemediapanelrenderoptions) |
| --- | --- |

## Properties

| **mips** : Int [Get] | Number of mip levels to use for panel texture. Mipmapping is the process of generating lower resolution versions of a texture to display on panels when they are far away. Signature ```kotlin val mips: Int = 1 ``` |
| --- | --- |
| **renderMode** : [PanelRenderMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelrendermode) [Get] | Control how the panel will render in the scene. Use layers to make panels appear crisp and high resolution, or mesh for basic rendering without compositor layers. Signature ```kotlin val renderMode: PanelRenderMode ``` |
| **samplerConfig** : [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) [Get] | The [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) to set the panel texture/layer. Signature ```kotlin val samplerConfig: SamplerConfig ``` |
| **stereoMode** : [StereoMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_stereomode) [Get] | The [StereoMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_stereomode) to use for the panel. Signature ```kotlin val stereoMode: StereoMode ``` |
| **zIndex** : Int [Get] | The zIndex to set the panel layer. Signature ```kotlin val zIndex: Int = 0 ``` |

## Functions

| **applyTo** ( options ) | Signature ```kotlin open override fun applyTo(options: PanelConfigOptions) ``` Parameters options: [PanelConfigOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelconfigoptions) |
| --- | --- |