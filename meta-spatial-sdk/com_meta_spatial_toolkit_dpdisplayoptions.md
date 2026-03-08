# DpDisplayOptions Class

Implements
[PanelConfigOptionsModifier](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelconfigoptionsmodifier)
,
[UIPanelDisplayOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_uipaneldisplayoptions)
*Modifiers:
final*

Configuration for a display with density-independent pixel (dp) dimensions.

## Signature

```kotlin
data class DpDisplayOptions(val width: Float, val height: Float, val dpi: Int = DpDisplayOptions.DEFAULT_DPI) : PanelConfigOptionsModifier, UIPanelDisplayOptions
```

## Constructors

| **DpDisplayOptions** ( width , height , dpi ) | Signature ```kotlin constructor(width: Float, height: Float, dpi: Int = DpDisplayOptions.DEFAULT_DPI) ``` Parameters width: Float The width of the panel in dp height: Float The height of the panel in dp dpi: Int The dots per inch to use for the display Returns [DpDisplayOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_dpdisplayoptions) |
| --- | --- |

## Properties

| **dpi** : Int [Get] | The dots per inch to use for the display Signature ```kotlin val dpi: Int ``` |
| --- | --- |
| **height** : Float [Get] | The height of the panel in dp Signature ```kotlin val height: Float ``` |
| **width** : Float [Get] | The width of the panel in dp Signature ```kotlin val width: Float ``` |

## Functions

| **applyTo** ( options ) | Signature ```kotlin open override fun applyTo(options: PanelConfigOptions) ``` Parameters options: [PanelConfigOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelconfigoptions) |
| --- | --- |

## Companion Object

### Companion Object Properties

| **DEFAULT_DPI** : Int [Get] | The default DPI used for DpDisplaySettings. Signature ```kotlin const val DEFAULT_DPI: Int ``` |
| --- | --- |