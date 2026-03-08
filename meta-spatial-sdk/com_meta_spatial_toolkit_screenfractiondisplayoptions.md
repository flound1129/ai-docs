# ScreenFractionDisplayOptions Class

Implements
[PanelConfigOptionsModifier](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelconfigoptionsmodifier)
,
[UIPanelDisplayOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_uipaneldisplayoptions)
*Modifiers:
final*

Configuration for a display that occupies a fraction of the screen. This is useful if you do not know an exact size but want a panel that you estimate will take up X% of the screen. Defaults to an assumption that 50% of the screen will be occupied.

## Signature

```kotlin
data class ScreenFractionDisplayOptions(val fraction: Float = 0.5f) : PanelConfigOptionsModifier, UIPanelDisplayOptions
```

## Constructors

| **ScreenFractionDisplayOptions** ( fraction ) | Signature ```kotlin constructor(fraction: Float = 0.5f) ``` Parameters fraction: Float The fraction of the screen that the panel should occupy (0.0-1.0) Returns [ScreenFractionDisplayOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_screenfractiondisplayoptions) |
| --- | --- |

## Properties

| **fraction** : Float [Get] | The fraction of the screen that the panel should occupy (0.0-1.0) Signature ```kotlin val fraction: Float = 0.5f ``` |
| --- | --- |

## Functions

| **applyTo** ( options ) | Signature ```kotlin open override fun applyTo(options: PanelConfigOptions) ``` Parameters options: [PanelConfigOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelconfigoptions) |
| --- | --- |