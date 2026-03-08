# MediaPanelSettings Class

Implements
[PanelSettings](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelsettings)
*Modifiers:
final*

## Signature

```kotlin
class MediaPanelSettings(val shape: MediaPanelShapeOptions, val display: MediaPanelDisplayOptions, val rendering: MediaPanelRenderOptions = MediaPanelRenderOptions(), val style: PanelStyleOptions = PanelStyleOptions(), val input: PanelInputOptions = PanelInputOptions()) : PanelSettings
```

## Constructors

| **MediaPanelSettings** ( shape , display , rendering , style , input ) | Signature ```kotlin constructor(shape: MediaPanelShapeOptions, display: MediaPanelDisplayOptions, rendering: MediaPanelRenderOptions = MediaPanelRenderOptions(), style: PanelStyleOptions = PanelStyleOptions(), input: PanelInputOptions = PanelInputOptions()) ``` Parameters shape: [MediaPanelShapeOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mediapanelshapeoptions) display: [MediaPanelDisplayOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mediapaneldisplayoptions) rendering: [MediaPanelRenderOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mediapanelrenderoptions) style: [PanelStyleOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelstyleoptions) input: [PanelInputOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelinputoptions) Returns [MediaPanelSettings](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mediapanelsettings) |
| --- | --- |

## Properties

| **display** : [MediaPanelDisplayOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mediapaneldisplayoptions) [Get] | Signature ```kotlin val display: MediaPanelDisplayOptions ``` |
| --- | --- |
| **input** : [PanelInputOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelinputoptions) [Get] | Signature ```kotlin val input: PanelInputOptions ``` |
| **rendering** : [MediaPanelRenderOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mediapanelrenderoptions) [Get] | Signature ```kotlin val rendering: MediaPanelRenderOptions ``` |
| **shape** : [MediaPanelShapeOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mediapanelshapeoptions) [Get] | Signature ```kotlin val shape: MediaPanelShapeOptions ``` |
| **style** : [PanelStyleOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelstyleoptions) [Get] | Signature ```kotlin val style: PanelStyleOptions ``` |

## Functions

| **toPanelConfigOptions** () | Converts these settings to a PanelConfigOptions object. Signature ```kotlin open override fun toPanelConfigOptions(): PanelConfigOptions ``` Returns [PanelConfigOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelconfigoptions) A PanelConfigOptions object |
| --- | --- |