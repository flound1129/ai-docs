# DpPerMeterDisplayOptions Class

Implements
[PanelConfigOptionsModifier](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelconfigoptionsmodifier)
,
[UIPanelDisplayOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_uipaneldisplayoptions)
*Modifiers:
final*

Configuration for a display with a specified number of density-independent pixels (dp) per meter. This is useful for reasoning about panels based on their physical size. Changing the size of the panel with ShapeSettings will not require you to also change the DisplaySettings.

The default is 500 dp per meter. This means if you have a 1 meter wide panel, it will be 500 dp wide. If you create a button that is 100 dp wide, it will be 1/5 of the panel and measure 0.2 meters. If you decide later to double the width of the panel to 2 meters wide the button will still be 0.2 wide (this demonstrates the benefit of using dpPerMeter).

This can only be used with UIPanelSettings which is restricted to Quad and Cylinder shapes.

## Signature

```kotlin
data class DpPerMeterDisplayOptions(val dpPerMeter: Float = PanelConstants.DEFAULT_DP_PER_METER, val resolutionScale: Float = 1.0f) : PanelConfigOptionsModifier, UIPanelDisplayOptions
```

## Constructors

| **DpPerMeterDisplayOptions** ( dpPerMeter , resolutionScale ) | Signature ```kotlin constructor(dpPerMeter: Float = PanelConstants.DEFAULT_DP_PER_METER, resolutionScale: Float = 1.0f) ``` Parameters dpPerMeter: Float How many density-independent pixels represent one meter. Defaults to 500. resolutionScale: Float Increase the resolution to improve sharpness, or reduce to improve performance. A setting of 1.2f increase the resolution by 20%. Returns [DpPerMeterDisplayOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_dppermeterdisplayoptions) |
| --- | --- |

## Properties

| **dpPerMeter** : Float [Get] | How many density-independent pixels represent one meter. Defaults to 500. Signature ```kotlin val dpPerMeter: Float ``` |
| --- | --- |
| **resolutionScale** : Float [Get] | Increase the resolution to improve sharpness, or reduce to improve performance. A setting of 1.2f increase the resolution by 20%. Signature ```kotlin val resolutionScale: Float = 1.0f ``` |

## Functions

| **applyTo** ( options ) | Signature ```kotlin open override fun applyTo(options: PanelConfigOptions) ``` Parameters options: [PanelConfigOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelconfigoptions) |
| --- | --- |