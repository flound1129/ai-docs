# PhysicsWorldBounds Class

*Modifiers:
final*

Defines boundaries for the physics world. Entities that move outside these bounds can be automatically destroyed.

## Signature

```kotlin
class PhysicsWorldBounds(var minX: Float? = null, var maxX: Float? = null, var minY: Float? = null, var maxY: Float? = null, var minZ: Float? = null, var maxZ: Float? = null)
```

## Constructors

| **PhysicsWorldBounds** ( minX , maxX , minY , maxY , minZ , maxZ ) | Signature ```kotlin constructor(minX: Float? = null, maxX: Float? = null, minY: Float? = null, maxY: Float? = null, minZ: Float? = null, maxZ: Float? = null) ``` Parameters minX: Float? Minimum X coordinate boundary (null means no limit) maxX: Float? Maximum X coordinate boundary (null means no limit) minY: Float? Minimum Y coordinate boundary (null means no limit) maxY: Float? Maximum Y coordinate boundary (null means no limit) minZ: Float? Minimum Z coordinate boundary (null means no limit) maxZ: Float? Maximum Z coordinate boundary (null means no limit) Returns [PhysicsWorldBounds](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_physicsworldbounds) |
| --- | --- |

## Properties

| **maxX** : Float? [Get][Set] | Maximum X coordinate boundary (null means no limit) Signature ```kotlin var maxX: Float? ``` |
| --- | --- |
| **maxY** : Float? [Get][Set] | Maximum Y coordinate boundary (null means no limit) Signature ```kotlin var maxY: Float? ``` |
| **maxZ** : Float? [Get][Set] | Maximum Z coordinate boundary (null means no limit) Signature ```kotlin var maxZ: Float? ``` |
| **minX** : Float? [Get][Set] | Minimum X coordinate boundary (null means no limit) Signature ```kotlin var minX: Float? ``` |
| **minY** : Float? [Get][Set] | Minimum Y coordinate boundary (null means no limit) Signature ```kotlin var minY: Float? ``` |
| **minZ** : Float? [Get][Set] | Minimum Z coordinate boundary (null means no limit) Signature ```kotlin var minZ: Float? ``` |