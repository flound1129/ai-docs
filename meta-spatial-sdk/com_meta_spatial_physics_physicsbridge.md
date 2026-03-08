# PhysicsBridge Class

*Modifiers:
final*

Bridge class providing access to native physics functionality. This class owns all the native methods for physics simulation that were previously in SpatialInterface.

This class is used internally by the physics feature systems and should not be instantiated directly by application code.

## Signature

```kotlin
class PhysicsBridge(val spatial: SpatialInterface)
```

## Constructors

| **PhysicsBridge** ( spatial ) | Signature ```kotlin constructor(spatial: SpatialInterface) ``` Parameters spatial: [SpatialInterface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialinterface) Returns [PhysicsBridge](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_physicsbridge) |
| --- | --- |

## Properties

| **spatial** : [SpatialInterface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialinterface) [Get] | Signature ```kotlin val spatial: SpatialInterface ``` |
| --- | --- |

## Functions

| **createPhysicsObject** ( entity , shape ) | Creates a physics object for the specified entity with the given shape. This method adds physics simulation capabilities to an entity, allowing it to participate in the physics world with collisions and dynamics. Signature ```kotlin fun createPhysicsObject(entity: Entity, shape: String) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity for which to create a physics object. shape: String The shape of the physics object (e.g., "box", "sphere", "capsule"), or the path to the glb file. |
| --- | --- |
| **deletePhysics** ( entity ) | Removes physics components from the specified entity. This method should be called when an entity with physics components is being deleted or when physics simulation is no longer needed for that entity. Signature ```kotlin fun deletePhysics(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity from which to remove physics components. |
| **enablePhysicsDebugLines** ( enabled ) | Toggles debug lines for visualization of the physics simulation. The color of the lines correspond to the state of the physics objects. This is useful for debugging physics interactions and understanding how physics bodies are behaving in the scene. Signature ```kotlin fun enablePhysicsDebugLines(enabled: Boolean) ``` Parameters enabled: Boolean Whether to enable or disable physics debug lines. |
| **potentiallyActivatePhysicsBodies** () | Potentially activates physics bodies that were deactivated due to deleted objects. When a physics object is deleted, nearby physics bodies may need to be re-enabled to properly respond to the change in the physics world. Signature ```kotlin fun potentiallyActivatePhysicsBodies() ``` |
| **setGravity** ( x , y , z ) | Sets the gravity vector for the physics simulation. This method allows customizing the direction and strength of gravity in the physics world, which affects how objects fall and interact. Signature ```kotlin fun setGravity(x: Float, y: Float, z: Float) ``` Parameters x: Float The x-component of the gravity vector. y: Float The y-component of the gravity vector. z: Float The z-component of the gravity vector. |
| **tickPhysics** () | Advances the physics simulation for a single frame. This method performs collision detection, constraint solving, and integration of physics bodies, updating their positions and orientations. Signature ```kotlin fun tickPhysics() ``` |
| **tickUpdatePhysicsState** () | Updates the physics state before simulation. This method prepares the physics system for simulation by updating the state of all physics bodies based on their associated entities. Signature ```kotlin fun tickUpdatePhysicsState() ``` |