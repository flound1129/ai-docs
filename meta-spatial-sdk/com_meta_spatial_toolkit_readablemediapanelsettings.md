# ReadableMediaPanelSettings Class

Implements
[PanelSettings](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelsettings)
*Modifiers:
final*

## Signature

```kotlin
class ReadableMediaPanelSettings(val shape: MediaPanelShapeOptions = QuadShapeOptions(), val display: MediaPanelDisplayOptions, val rendering: ReadableMediaPanelRenderOptions = ReadableMediaPanelRenderOptions(), val style: PanelStyleOptions = PanelStyleOptions(), val input: PanelInputOptions = PanelInputOptions()) : PanelSettings
```

## Constructors

| **ReadableMediaPanelSettings** ( shape , display , rendering , style , input ) | Signature ```kotlin constructor(shape: MediaPanelShapeOptions = QuadShapeOptions(), display: MediaPanelDisplayOptions, rendering: ReadableMediaPanelRenderOptions = ReadableMediaPanelRenderOptions(), style: PanelStyleOptions = PanelStyleOptions(), input: PanelInputOptions = PanelInputOptions()) ``` Parameters shape: [MediaPanelShapeOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mediapanelshapeoptions) display: [MediaPanelDisplayOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mediapaneldisplayoptions) rendering: [ReadableMediaPanelRenderOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_readablemediapanelrenderoptions) style: [PanelStyleOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelstyleoptions) input: [PanelInputOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelinputoptions) Returns [ReadableMediaPanelSettings](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_readablemediapanelsettings) |
| --- | --- |

## Properties

| **display** : [MediaPanelDisplayOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mediapaneldisplayoptions) [Get] | Signature ```kotlin val display: MediaPanelDisplayOptions ``` |
| --- | --- |
| **input** : [PanelInputOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelinputoptions) [Get] | Signature ```kotlin val input: PanelInputOptions ``` |
| **rendering** : [ReadableMediaPanelRenderOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_readablemediapanelrenderoptions) [Get] | Signature ```kotlin val rendering: ReadableMediaPanelRenderOptions ``` |
| **shape** : [MediaPanelShapeOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mediapanelshapeoptions) [Get] | Signature ```kotlin val shape: MediaPanelShapeOptions ``` |
| **style** : [PanelStyleOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelstyleoptions) [Get] | Signature ```kotlin val style: PanelStyleOptions ``` |

## Functions

| **toPanelConfigOptions** () | Converts these settings to a PanelConfigOptions object. Signature ```kotlin open override fun toPanelConfigOptions(): PanelConfigOptions ``` Returns [PanelConfigOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelconfigoptions) A PanelConfigOptions object |
| --- | --- |