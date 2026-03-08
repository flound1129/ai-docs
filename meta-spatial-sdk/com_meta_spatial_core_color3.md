# Color3 Class

*Modifiers:
final*

Color3 is a class that represents a color in RGB space. It has three properties: red, green, and blue. These properties are floats that range from 0 to 1.

## Signature

```kotlin
class Color3
```

## Constructors

| **Color3** ( red , green , blue ) | Signature ```kotlin constructor(red: Float = 0.0f, green: Float = 0.0f, blue: Float = 0.0f) ``` Parameters red: Float green: Float blue: Float Returns [Color3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_color3) |
| --- | --- |
| **Color3** () | Creates a new Color3 object with default values of 0 for each property. Signature ```kotlin constructor() ``` Returns [Color3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_color3) |

## Properties

| **blue** : Float [Get][Set] | The blue component of the color, as a float between 0 and 1. Signature ```kotlin var blue: Float ``` |
| --- | --- |
| **green** : Float [Get][Set] | The green component of the color, as a float between 0 and 1. Signature ```kotlin var green: Float ``` |
| **red** : Float [Get][Set] | The red component of the color, as a float between 0 and 1. Signature ```kotlin var red: Float ``` |

## Functions

| **equals** ( other ) | Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? Returns Boolean |
| --- | --- |
| **hashCode** () | Signature ```kotlin open override fun hashCode(): Int ``` Returns Int |