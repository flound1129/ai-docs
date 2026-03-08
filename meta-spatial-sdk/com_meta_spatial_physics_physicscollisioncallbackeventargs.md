# PhysicsCollisionCallbackEventArgs Class

Extends
[EventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_eventargs)
*Modifiers:
final*

Event arguments for physics collision callbacks. Contains information about the collision including the entity involved, position, normal vector, and impulse force.

## Signature

```kotlin
class PhysicsCollisionCallbackEventArgs(val collidedEntity: Entity, val collisionPosition: Vector3, val collisionNormal: Vector3, val impulse: Float, datamodel: DataModel) : EventArgs
```

## Constructors

| **PhysicsCollisionCallbackEventArgs** ( collidedEntity , collisionPosition , collisionNormal , impulse , datamodel ) | Signature ```kotlin constructor(collidedEntity: Entity, collisionPosition: Vector3, collisionNormal: Vector3, impulse: Float, datamodel: DataModel) ``` Parameters collidedEntity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity that was involved in the collision collisionPosition: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The 3D position where the collision occurred collisionNormal: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The normal vector at the point of collision impulse: Float The force of the collision impulse datamodel: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) The data model instance for event propagation Returns [PhysicsCollisionCallbackEventArgs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_physicscollisioncallbackeventargs) |
| --- | --- |

## Properties

| **collidedEntity** : [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) [Get] | The entity that was involved in the collision Signature ```kotlin val collidedEntity: Entity ``` |
| --- | --- |
| **collisionNormal** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get] | The normal vector at the point of collision Signature ```kotlin val collisionNormal: Vector3 ``` |
| **collisionPosition** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get] | The 3D position where the collision occurred Signature ```kotlin val collisionPosition: Vector3 ``` |
| **dataModel** : [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) [Get] | Signature ```kotlin val dataModel: DataModel ``` |
| **eventName** : String [Get] | Signature ```kotlin val eventName: String ``` |
| **handled** : Boolean [Get][Set] | Signature ```kotlin var handled: Boolean ``` |
| **impulse** : Float [Get] | The force of the collision impulse Signature ```kotlin val impulse: Float ``` |
| **throttleTime** : Int? [Get][Set] | Signature ```kotlin var throttleTime: Int? ``` |

## Companion Object

### Companion Object Properties

| **EVENT_NAME** : String [Get] | Signature ```kotlin val EVENT_NAME: String ``` |
| --- | --- |