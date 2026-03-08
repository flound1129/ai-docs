# TriggerNativeCallbackOnDatamodel Object

Bridge object called by native code to trigger physics collision callbacks on the data model. This object is accessed via JNI from the native physics engine when collisions occur.

## Signature

```kotlin
object TriggerNativeCallbackOnDatamodel
```

## Functions

| **triggerCallback** ( collider , collided , collisionPos , normal , impulse ) | Triggers a physics collision callback event on the data model. Signature ```kotlin fun triggerCallback(collider: Long, collided: Long, collisionPos: Vector3, normal: Vector3, impulse: Float) ``` Parameters collider: Long The entity ID that initiated the collision collided: Long The entity ID that was collided with collisionPos: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The 3D position where the collision occurred normal: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The collision normal vector impulse: Float The force of the collision impulse |
| --- | --- |