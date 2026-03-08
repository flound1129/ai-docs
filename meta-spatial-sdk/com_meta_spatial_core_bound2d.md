# Bound2D Class

*Modifiers:
final*

A data class representing a 2D bounding box.

## Signature

```kotlin
data class Bound2D(var min: Vector2 = Vector2(0f, 0f), var max: Vector2 = Vector2(0f, 0f))
```

## Constructors

| **Bound2D** ( min , max ) | Signature ```kotlin constructor(min: Vector2 = Vector2(0f, 0f), max: Vector2 = Vector2(0f, 0f)) ``` Parameters min: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The minimum coordinates of the bounding box. max: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The maximum coordinates of the bounding box. Returns [Bound2D](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bound2d) |
| --- | --- |

## Properties

| **max** : [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) [Get][Set] | The maximum coordinates of the bounding box. Signature ```kotlin var max: Vector2 ``` |
| --- | --- |
| **min** : [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) [Get][Set] | The minimum coordinates of the bounding box. Signature ```kotlin var min: Vector2 ``` |

## Functions

| **toString** () | Returns a string representation of the bounding box. Signature ```kotlin open override fun toString(): String ``` Returns String A string in the format "(min, max)". |
| --- | --- |