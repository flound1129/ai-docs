# Color4 Class

*Modifiers:
open*

Color4 is a class that represents a color in RGBA space. It has four properties: red, green, blue, and alpha. These properties are floats that range from 0 to 1.

## Signature

```kotlin
open class Color4
```

## Constructors

| **Color4** ( red , green , blue , alpha ) | Signature ```kotlin constructor(red: Float = 0.0f, green: Float = 0.0f, blue: Float = 0.0f, alpha: Float = 1.0f) ``` Parameters red: Float green: Float blue: Float alpha: Float Returns [Color4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_color4) |
| --- | --- |
| **Color4** () | Creates a new Color4 object with default values of 0 rgb and alpha = 1.0f. Signature ```kotlin constructor() ``` Returns [Color4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_color4) |

## Properties

| **alpha** : Float [Get][Set] | The alpha component of the color, as a float between 0 and 1. Signature ```kotlin open var alpha: Float ``` |
| --- | --- |
| **blue** : Float [Get][Set] | The blue component of the color, as a float between 0 and 1. Signature ```kotlin open var blue: Float ``` |
| **green** : Float [Get][Set] | The green component of the color, as a float between 0 and 1. Signature ```kotlin open var green: Float ``` |
| **red** : Float [Get][Set] | The red component of the color, as a float between 0 and 1. Signature ```kotlin open var red: Float ``` |

## Functions

| **copy** () | Signature ```kotlin fun copy(): Color4 ``` Returns [Color4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_color4) |
| --- | --- |
| **equals** ( other ) | Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? Returns Boolean |
| **hashCode** () | Signature ```kotlin open override fun hashCode(): Int ``` Returns Int |