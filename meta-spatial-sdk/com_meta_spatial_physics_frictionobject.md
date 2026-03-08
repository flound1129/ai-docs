# FrictionObject Class

*Modifiers:
final*

Represents friction properties for physics objects. Manages three types of friction: sliding, rolling, and spinning.

## Signature

```kotlin
class FrictionObject
```

## Constructors

| **FrictionObject** ( friction ) | Signature ```kotlin constructor(friction: Float = 0.1f) ``` Parameters friction: Float Returns [FrictionObject](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_frictionobject) |
| --- | --- |
| **FrictionObject** ( sliding , rolling , spinning ) | Signature ```kotlin constructor(sliding: Float, rolling: Float, spinning: Float) ``` Parameters sliding: Float rolling: Float spinning: Float Returns [FrictionObject](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_frictionobject) |

## Properties

| **rollingFriction** : Float [Get][Set] | Signature ```kotlin var rollingFriction: Float ``` |
| --- | --- |
| **slidingFriction** : Float [Get][Set] | Signature ```kotlin var slidingFriction: Float ``` |
| **spinningFriction** : Float [Get][Set] | Signature ```kotlin var spinningFriction: Float ``` |