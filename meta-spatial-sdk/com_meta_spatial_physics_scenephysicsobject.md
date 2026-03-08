# ScenePhysicsObject Class

*Modifiers:
open*

Represents a physics-enabled object in a 3D scene. Can be used to create custom physics implementations using the ECS.

Needs the [PhysicsFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_physicsfeature) to be enabled to work. Consider using the [Physics](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_physics) component before implementing a custom physics system.

Example of a Custom Physics System, which creates a Physics box with initial linear velocity specified by the CustomPhysics component.

Component:

```kotlin <?xml version="1.0" ?>
<ComponentSchema packageName="com.meta.aether.apps.experiments.physics">
 <Component name="CustomPhysics">
   <Vector3Attribute
     name="initialLinearVelocity"
     defaultValue="0.0f, 0.0f, 0.0f"
   />
 </Component>
</ComponentSchema> ```

System:

```kotlin class CustomPhysicsSystem() : SystemBase() {
private val physicsObjects_ = HashMap<Entity, ScenePhysicsObject>()
override fun execute() {
  val q = Query.where { changed(CustomPhysics.id) and has(Transform.id) }
  for (ent in q.eval()) {
    if (physicsObjects_.containsKey(ent)) {
      continue
    }
    val physics = ScenePhysicsObject.createBox(getScene(), ent, 0.25f, 0.25f, 0.25f, 0.5f)
    physicsObjects_.put(ent, physics)
    physics.setPose(ent.getComponent<Transform>().transform)
    physics.setLinearVelocity(ent.getComponent<CustomPhysics>().initialLinearVelocity)
    Log.i("Physics", "Created physics object for entity $ent $physics")
  }
}
override fun delete(entity: Entity) {
  if (physicsObjects_.containsKey(entity)) {
    physicsObjects_[entity]?.destroy()
    physicsObjects_.remove(entity)
  }
} ```

## Signature

```kotlin
open class ScenePhysicsObject
```

## Properties

| **entity** : [Entity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) [Get] | Signature ```kotlin val entity: Entity? ``` |
| --- | --- |
| **handle** : Long [Get] | Native handle to the physics object. Signature ```kotlin var handle: Long ``` |

## Functions

| **applyForce** ( force ) | Applies a force to this physics object Signature ```kotlin fun applyForce(force: Vector3) ``` Parameters force: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The force vector to apply (in newtons) |
| --- | --- |
| **applyForceAtRelativePosition** ( force , relativePos ) | Applies a force to this physics object at a specified position relative to its center. This can create both linear and angular acceleration depending on the force and position. Signature ```kotlin fun applyForceAtRelativePosition(force: Vector3, relativePos: Vector3) ``` Parameters force: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The force vector to apply (in newtons) relativePos: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The position relative to the center of mass where the force is applied |
| **applyTorque** ( torqueX , torqueY , torqueZ ) | Applies a torque (rotational force) to this physics object. Signature ```kotlin fun applyTorque(torqueX: Float, torqueY: Float, torqueZ: Float) ``` Parameters torqueX: Float The X component of the torque vector torqueY: Float The Y component of the torque vector torqueZ: Float The Z component of the torque vector |
| **destroy** () | Signature ```kotlin fun destroy() ``` |
| **getPose** () | Gets the current position and rotation of this physics object. Signature ```kotlin fun getPose(): Pose ``` Returns [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) The current pose |
| **setAngularVelocity** ( angularVelocity ) | Sets the angular velocity of this physics object. Signature ```kotlin fun setAngularVelocity(angularVelocity: Vector3) ``` Parameters angularVelocity: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The angular velocity vector (in radians per second) |
| **setFriction** ( friction , rolling , spinning ) | Sets the friction properties of this physics object. Signature ```kotlin fun setFriction(friction: Float, rolling: Float = friction, spinning: Float) ``` Parameters friction: Float The surface friction coefficient rolling: Float The rolling friction coefficient (defaults to the same as surface friction) spinning: Float The spinning friction coefficient |
| **setLinearVelocity** ( velocity ) | Sets the linear velocity of this physics object. Signature ```kotlin fun setLinearVelocity(velocity: Vector3) ``` Parameters velocity: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The linear velocity vector (in meters per second) |
| **setPose** ( pose ) | Sets the position and rotation of this physics object. Signature ```kotlin fun setPose(pose: Pose) ``` Parameters pose: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) The position and rotation to set |
| **setRestitution** ( restitution ) | Sets the restitution (bounciness) of this physics object. Signature ```kotlin fun setRestitution(restitution: Float) ``` Parameters restitution: Float The restitution value (0.0 = no bounce) |

## Companion Object

### Companion Object Functions

| **createBox** ( scene , entity , width , height , depth , mass ) | Creates a box-shaped physics object. Signature ```kotlin fun createBox(scene: Scene, entity: Entity?, width: Float, height: Float, depth: Float, mass: Float): ScenePhysicsObject ``` Parameters scene: [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene in which to create the physics object entity: [Entity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) Optional entity to associate with this physics object width: Float Width of the box in meters height: Float Height of the box in meters depth: Float Depth of the box in meters mass: Float Mass of the box in kilograms (0 for static objects) Returns [ScenePhysicsObject](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_scenephysicsobject) A new box-shaped physics object |
| --- | --- |
| **createGLTF** ( scene , entity , filename , mass ) | Creates a physics object from a GLTF model file. The collision shape will be generated from the model's geometry. Signature ```kotlin fun createGLTF(scene: Scene, entity: Entity?, filename: String, mass: Float): ScenePhysicsObject ``` Parameters scene: [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene in which to create the physics object entity: [Entity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) Optional entity to associate with this physics object filename: String Path to the GLTF model file mass: Float Mass of the object in kilograms (0 for static objects) Returns [ScenePhysicsObject](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_scenephysicsobject) A new physics object based on the GLTF model |
| **createSphere** ( scene , entity , radius , mass ) | Creates a sphere-shaped physics object. Signature ```kotlin fun createSphere(scene: Scene, entity: Entity?, radius: Float, mass: Float): ScenePhysicsObject ``` Parameters scene: [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene in which to create the physics object entity: [Entity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) Optional entity to associate with this physics object radius: Float Radius of the sphere in meters mass: Float Mass of the sphere in kilograms (0 for static objects) Returns [ScenePhysicsObject](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_scenephysicsobject) A new sphere-shaped physics object |
| **setCallbackEntities** ( scene , entities ) | Sets the entities that will receive physics callbacks. Signature ```kotlin fun setCallbackEntities(scene: Long, entities: LongArray) ``` Parameters scene: Long The scene handle entities: LongArray Array of entity IDs that will receive physics callbacks |