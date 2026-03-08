# BlendFactor Enum

These coefficients are used to calculate the final color and alpha values of a blended layer. "Source" refers to the layer you are currently compositing. "Destination" refers to whatever is already in the buffer.

## Signature

```kotlin
enum BlendFactor : Enum<BlendFactor>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| ZERO | This coefficient will result in a value of 0. |
| ONE | This coefficient will leave the value unchanged. |
| SOURCE_ALPHA | Will multiply value with the source alpha |
| ONE_MINUS_SOURCE_ALPHA | Will multiply the value with the inverse of source alpha |
| DESTINATION_ALPHA | Will multiply value with destination alpha |
| ONE_MINUS_DESTINATION_ALPHA | Will multiply value with 1 minus the destination alpha |

## Properties

| **factor** : Int [Get] | Signature ```kotlin val factor: Int ``` |
| --- | --- |

## Companion Object

### Companion Object Functions

| **fromInt** ( factor ) | Returns the blend factor corresponding to the given integer value. Signature ```kotlin fun fromInt(factor: Int): BlendFactor ``` Parameters factor: Int the integer value of the blend factor Returns [BlendFactor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_blendfactor) the blend factor corresponding to the given integer value Throws IllegalArgumentException if the given integer value does not correspond to a valid blend factor |
| --- | --- |