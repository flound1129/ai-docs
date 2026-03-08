# MediaPanelRenderOptions Class

Implements
[PanelConfigOptionsModifier](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelconfigoptionsmodifier)
*Modifiers:
final*

Used for Panels meant to display high quality media. They are highly performant and will enable you to play the highest quality media but have limitations.

This option is also required for direct-to-surface rendering in [VideoSurfacePanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_videosurfacepanelregistration) .

If you need access to the panel's displayed image, then use [ReadableMediaPanelRenderOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_readablemediapanelrenderoptions) . This option is used to support transparent media and custom shader effects based on panel image.

## Signature

```kotlin
data class MediaPanelRenderOptions(val isDRM: Boolean = false, val stereoMode: StereoMode = StereoMode.None, val samplerConfig: SamplerConfig = PanelConfigOptions.DEFAULT_PANEL_SAMPLER, val layerFilters: Int = 0, val zIndex: Int = 0) : PanelConfigOptionsModifier
```

## Constructors

| **MediaPanelRenderOptions** ( isDRM , stereoMode , samplerConfig , layerFilters , zIndex ) | Signature ```kotlin constructor(isDRM: Boolean = false, stereoMode: StereoMode = StereoMode.None, samplerConfig: SamplerConfig = PanelConfigOptions.DEFAULT_PANEL_SAMPLER, layerFilters: Int = 0, zIndex: Int = 0) ``` Parameters isDRM: Boolean stereoMode: [StereoMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_stereomode) samplerConfig: [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) layerFilters: Int zIndex: Int Returns [MediaPanelRenderOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mediapanelrenderoptions) |
| --- | --- |

## Properties

| **isDRM** : Boolean [Get] | Signature ```kotlin val isDRM: Boolean = false ``` |
| --- | --- |
| **layerFilters** : Int [Get] | Signature ```kotlin val layerFilters: Int = 0 ``` |
| **samplerConfig** : [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) [Get] | Signature ```kotlin val samplerConfig: SamplerConfig ``` |
| **stereoMode** : [StereoMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_stereomode) [Get] | Signature ```kotlin val stereoMode: StereoMode ``` |
| **zIndex** : Int [Get] | Signature ```kotlin val zIndex: Int = 0 ``` |

## Functions

| **applyTo** ( options ) | Signature ```kotlin open override fun applyTo(options: PanelConfigOptions) ``` Parameters options: [PanelConfigOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelconfigoptions) |
| --- | --- |