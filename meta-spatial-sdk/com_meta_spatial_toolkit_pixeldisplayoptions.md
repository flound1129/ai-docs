# PixelDisplayOptions Class

Implements
[PanelConfigOptionsModifier](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelconfigoptionsmodifier)
,
[MediaPanelDisplayOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mediapaneldisplayoptions)
*Modifiers:
final*

Configuration for a display with pixel-based dimensions.

## Signature

```kotlin
data class PixelDisplayOptions(val width: Int, val height: Int) : PanelConfigOptionsModifier, MediaPanelDisplayOptions
```

## Constructors

| **PixelDisplayOptions** ( width , height ) | Signature ```kotlin constructor(width: Int, height: Int) ``` Parameters width: Int The width of the panel in pixels height: Int The height of the panel in pixels Returns [PixelDisplayOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_pixeldisplayoptions) |
| --- | --- |

## Properties

| **height** : Int [Get] | The height of the panel in pixels Signature ```kotlin val height: Int ``` |
| --- | --- |
| **width** : Int [Get] | The width of the panel in pixels Signature ```kotlin val width: Int ``` |

## Functions

| **applyTo** ( options ) | Signature ```kotlin open override fun applyTo(options: PanelConfigOptions) ``` Parameters options: [PanelConfigOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelconfigoptions) |
| --- | --- |