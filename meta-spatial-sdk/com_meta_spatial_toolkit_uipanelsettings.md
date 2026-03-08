# UIPanelSettings Class

Implements
[PanelSettings](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelsettings)
*Modifiers:
final*

## Signature

```kotlin
class UIPanelSettings(val shape: UIPanelShapeOptions = QuadShapeOptions(), val display: UIPanelDisplayOptions = ScreenFractionDisplayOptions(), val rendering: UIPanelRenderOptions = UIPanelRenderOptions(), val style: PanelStyleOptions = PanelStyleOptions(), val input: PanelInputOptions = PanelInputOptions()) : PanelSettings
```

## Constructors

| **UIPanelSettings** ( shape , display , rendering , style , input ) | Signature ```kotlin constructor(shape: UIPanelShapeOptions = QuadShapeOptions(), display: UIPanelDisplayOptions = ScreenFractionDisplayOptions(), rendering: UIPanelRenderOptions = UIPanelRenderOptions(), style: PanelStyleOptions = PanelStyleOptions(), input: PanelInputOptions = PanelInputOptions()) ``` Parameters shape: [UIPanelShapeOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_uipanelshapeoptions) display: [UIPanelDisplayOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_uipaneldisplayoptions) rendering: [UIPanelRenderOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_uipanelrenderoptions) style: [PanelStyleOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelstyleoptions) input: [PanelInputOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelinputoptions) Returns [UIPanelSettings](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_uipanelsettings) |
| --- | --- |

## Properties

| **display** : [UIPanelDisplayOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_uipaneldisplayoptions) [Get] | Signature ```kotlin val display: UIPanelDisplayOptions ``` |
| --- | --- |
| **input** : [PanelInputOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelinputoptions) [Get] | Signature ```kotlin val input: PanelInputOptions ``` |
| **rendering** : [UIPanelRenderOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_uipanelrenderoptions) [Get] | Signature ```kotlin val rendering: UIPanelRenderOptions ``` |
| **shape** : [UIPanelShapeOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_uipanelshapeoptions) [Get] | Signature ```kotlin val shape: UIPanelShapeOptions ``` |
| **style** : [PanelStyleOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelstyleoptions) [Get] | Signature ```kotlin val style: PanelStyleOptions ``` |

## Functions

| **toPanelConfigOptions** () | Converts these settings to a PanelConfigOptions object. Signature ```kotlin open override fun toPanelConfigOptions(): PanelConfigOptions ``` Returns [PanelConfigOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelconfigoptions) A PanelConfigOptions object |
| --- | --- |