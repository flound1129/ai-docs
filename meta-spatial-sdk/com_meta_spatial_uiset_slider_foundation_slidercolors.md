# SliderColors Class

*Modifiers:
final*

Represents the colors used by a [null.SpatialSlider](/reference/spatial-sdk/v0.10.1/null#spatialslider) in different states

## Constructors

| **SliderColors** ( iconColor , activeTrackColor , inactiveTrackColor ) | create an instance with arbitrary colors. See [SliderDefaults.colors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_slider_foundation_sliderdefaults#colors) for the default implementation. Signature ```kotlin constructor(iconColor: Color, activeTrackColor: Color, inactiveTrackColor: Color) ``` Parameters iconColor: Color activeTrackColor: Color inactiveTrackColor: Color Returns [SliderColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_slider_foundation_slidercolors) |
| --- | --- |

## Properties

| **activeTrackColor** : Color [Get] | Signature ```kotlin val activeTrackColor: Color ``` |
| --- | --- |
| **iconColor** : Color [Get] | Signature ```kotlin val iconColor: Color ``` |
| **inactiveTrackColor** : Color [Get] | Signature ```kotlin val inactiveTrackColor: Color ``` |

## Functions

| **copy** ( iconColor , activeTrackColor , inactiveTrackColor ) | Returns a copy of this SliderColors, optionally overriding some of the values. This uses the Color.Unspecified to mean “use the value from the source” Signature ```kotlin fun copy(iconColor: Color, activeTrackColor: Color, inactiveTrackColor: Color): SliderColors ``` Parameters iconColor: Color activeTrackColor: Color inactiveTrackColor: Color Returns [SliderColors](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_slider_foundation_slidercolors) |
| --- | --- |
| **equals** ( other ) | Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? Returns Boolean |
| **hashCode** () | Signature ```kotlin open override fun hashCode(): Int ``` Returns Int |