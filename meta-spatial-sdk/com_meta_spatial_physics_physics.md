# Physics Class

Extends
[ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase)
*Modifiers:
final*

Physics component adds physics simulation to an entity. It enables collision detection, gravity, forces, and realistic object interactions.

Example:

```kotlin val ball = Entity.create()
ball.setComponent(
  Physics(
    shape = "sphere",
    state = PhysicsState.DYNAMIC,
    density = 1.0f,
    restitution = 0.8f
  )
) ```

## Signature

```kotlin
class Physics(linearVelocity: Vector3 = Vector3(0.0f, 0.0f, 0.0f), angularVelocity: Vector3 = Vector3(0.0f, 0.0f, 0.0f), dimensions: Vector3 = Vector3(0.5f, 0.5f, 0.5f), shape: String = "box", densityInternal: Float = 1.0f, applyForce: Vector3 = Vector3(0.0f, 0.0f, 0.0f), restitution: Float = 0.2f, frictionInternal: Vector3 = Vector3(0.5f, 0.0f, 0.0f), state: PhysicsState = PhysicsState.DYNAMIC) : ComponentBase
```

## Constructors

| **Physics** ( linearVelocity , angularVelocity , dimensions , shape , densityInternal , applyForce , restitution , frictionInternal , state ) | Signature ```kotlin constructor(linearVelocity: Vector3 = Vector3(0.0f, 0.0f, 0.0f), angularVelocity: Vector3 = Vector3(0.0f, 0.0f, 0.0f), dimensions: Vector3 = Vector3(0.5f, 0.5f, 0.5f), shape: String = "box", densityInternal: Float = 1.0f, applyForce: Vector3 = Vector3(0.0f, 0.0f, 0.0f), restitution: Float = 0.2f, frictionInternal: Vector3 = Vector3(0.5f, 0.0f, 0.0f), state: PhysicsState = PhysicsState.DYNAMIC) ``` Parameters linearVelocity: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) : Initial linear velocity of the object in m/s (x, y, z) angularVelocity: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) : Initial angular velocity of the object in rad/s (x, y, z) dimensions: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) : Size of the collision shape for primitive shapes (width, height, depth) shape: String : URL or path to the collision shape file (GLTF/GLB format) or primitive name ("box", "sphere") densityInternal: Float applyForce: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) : Force vector to apply to the object in Newtons (x, y, z) restitution: Float : Bounciness coefficient (0.0 = no bounce, 1.0 = perfect bounce) frictionInternal: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) state: [PhysicsState](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_physicsstate) : Physics simulation state (STATIC, DYNAMIC, or KINEMATIC) Returns [Physics](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_physics) |
| --- | --- |

## Properties

| **angularVelocity** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get][Set] | Initial angular velocity of the object in rad/s (x, y, z) Signature ```kotlin var angularVelocity: Vector3 ``` |
| --- | --- |
| **applyForce** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get][Set] | Force vector to apply to the object in Newtons (x, y, z) Signature ```kotlin var applyForce: Vector3 ``` |
| **cachable** : BuildConfig.COMPONENTCACHE_LEVEL >= 1 [Get][Set] | Signature ```kotlin open override var cachable: BuildConfig.COMPONENTCACHE_LEVEL >= 1 ``` |
| **density** : Float [Get][Set] | Signature ```kotlin var density: Float ``` |
| **densityInternal** : Float [Get][Set] | Internal storage for mass density (use density property instead) Signature ```kotlin var densityInternal: Float ``` |
| **dimensions** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get][Set] | Size of the collision shape for primitive shapes (width, height, depth) Signature ```kotlin var dimensions: Vector3 ``` |
| **entID** : Long [Get][Set] | Signature ```kotlin var entID: Long ``` |
| **friction** : [FrictionObject](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_frictionobject) [Get][Set] | Signature ```kotlin var friction: FrictionObject ``` |
| **frictionInternal** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get][Set] | Internal storage for friction values (sliding, rolling, spinning). Use friction property instead. Signature ```kotlin var frictionInternal: Vector3 ``` |
| **isDirty** : Boolean [Get][Set] | Signature ```kotlin var isDirty: Boolean ``` |
| **linearVelocity** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get][Set] | Initial linear velocity of the object in m/s (x, y, z) Signature ```kotlin var linearVelocity: Vector3 ``` |
| **recycled** : Boolean [Get][Set] | Signature ```kotlin var recycled: Boolean ``` |
| **restitution** : Float [Get][Set] | Bounciness coefficient (0.0 = no bounce, 1.0 = perfect bounce) Signature ```kotlin var restitution: Float ``` |
| **shape** : String [Get][Set] | URL or path to the collision shape file (GLTF/GLB format) or primitive name ('box', 'sphere') Signature ```kotlin var shape: String ``` |
| **state** : [PhysicsState](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_physicsstate) [Get][Set] | Physics simulation state (STATIC, DYNAMIC, or KINEMATIC) Signature ```kotlin var state: PhysicsState ``` |
| **timeStamp** : Long [Get][Set] | Signature ```kotlin var timeStamp: Long ``` |

## Functions

| **applyMaterial** ( material ) | Signature ```kotlin fun applyMaterial(material: PhysicsMaterial): Physics ``` Parameters material: [PhysicsMaterial](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_physicsmaterial) Returns [Physics](/reference/spatial-sdk/v0.10.1/com_meta_spatial_physics_physics) |
| --- | --- |
| **companion** () | Gets the companion object for this component. The companion object provides metadata about the component. Signature ```kotlin open override fun companion(): ComponentCompanion ``` Returns [ComponentCompanion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentcompanion) The component's companion object Throws RuntimeException If the companion is not implemented |
| **getComponentDataAttributeType** ( key ) | Gets the attribute type for the specified key. Signature ```kotlin fun getComponentDataAttributeType(key: Int): AttributePrimitive? ``` Parameters key: Int The integer key to look up Returns [AttributePrimitive?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_attributeprimitive) The attribute primitive type, or null if the key doesn't exist |
| **getComponentDataAttributeType** ( keyString ) | Gets the attribute type for the specified string key. Signature ```kotlin fun getComponentDataAttributeType(keyString: String): AttributePrimitive? ``` Parameters keyString: String The string key to look up Returns [AttributePrimitive?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_attributeprimitive) The attribute primitive type Throws IllegalArgumentException If the key doesn't exist |
| **getComponentDataKey** ( key ) | Gets the integer key associated with the specified string key. Signature ```kotlin fun getComponentDataKey(key: String): Int? ``` Parameters key: String The string key to look up Returns Int? The integer key, or null if the string key doesn't exist |
| **getComponentDataValue** ( key ) | Gets the value for the specified key. Signature ```kotlin fun getComponentDataValue(key: Int): Any? ``` Parameters key: Int The integer key to look up Returns Any? The value associated with the key, or null if the key doesn't exist |
| **getComponentDataValue** ( keyString ) | Gets the value for the specified string key. Signature ```kotlin fun getComponentDataValue(keyString: String): Any? ``` Parameters keyString: String The string key to look up Returns Any? The value associated with the key, or null if the key doesn't exist Throws IllegalArgumentException If the key doesn't exist |
| **getEnumClass** ( key ) | Gets the enum class associated with the specified string key. Signature ```kotlin fun getEnumClass(key: String): Class<out Enum<*>>? ``` Parameters key: String The string key to look up Returns Class? The enum class, or null if the key doesn't exist or is not an enum |
| **hasComponentData** ( key ) | Checks if this component has data for the specified key. Signature ```kotlin fun hasComponentData(key: Int): Boolean ``` Parameters key: Int The integer key to check Returns Boolean True if the component has data for the key, false otherwise |
| **hasComponentData** ( keyString ) | Checks if this component has data for the specified string key. Signature ```kotlin fun hasComponentData(keyString: String): Boolean ``` Parameters keyString: String The string key to check Returns Boolean True if the component has data for the key, false otherwise |
| **read** ( e , cachable ) | Reads component data from the specified entity. Signature ```kotlin fun read(e: Entity, cachable: Boolean) ``` Parameters e: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity to read data from cachable: Boolean Whether the component's data should be cached |
| **recycle** () | Recycles this component by returning it to its pool. If the component has a pool assigned, it will be returned to that pool for reuse. Signature ```kotlin fun recycle() ``` |
| **reset** () | Resets the component to its default state. This method is called when a component is recycled to clear any state. Subclasses should override this method to reset their specific state. Signature ```kotlin open fun reset() ``` |
| **setComponentDataValue** ( key , value ) | Sets the value for the specified key. Signature ```kotlin fun setComponentDataValue(key: Int, value: Any): Boolean ``` Parameters key: Int The integer key to set value: Any The value to set Returns Boolean True if the value was set successfully, false otherwise |
| **setComponentDataValue** ( keyString , value ) | Sets the value for the specified string key. Signature ```kotlin fun setComponentDataValue(keyString: String, value: Any): Boolean ``` Parameters keyString: String The string key to set value: Any The value to set Returns Boolean True if the key exists and the value was set, false otherwise |
| **setPool** ( pool , entID ) | Sets the component pool and entity ID for this component. This is used for component recycling to track which pool the component belongs to and which entity it was associated with. Signature ```kotlin fun setPool(pool: ComponentPool<*>, entID: Long) ``` Parameters pool: ComponentPool The component pool this component belongs to entID: Long The ID of the entity this component is associated with |
| **toString** () | Signature ```kotlin open override fun toString(): String ``` Returns String |
| **typeID** () | Returns the unique type ID of this component. Each component type must have a unique ID for identification in the entity-component system. Signature ```kotlin open override fun typeID(): Int ``` Returns Int The unique type ID for this component |
| **write** ( e ) | Writes this component's data to the specified entity. Signature ```kotlin fun write(e: Entity) ``` Parameters e: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity to write this component's data to |

## Companion Object

### Companion Object Properties

| **angularVelocityData** : [Vector3AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3attributedata) [Get] | Signature ```kotlin val angularVelocityData: Vector3AttributeData ``` |
| --- | --- |
| **angularVelocityId** [Get] | Signature ```kotlin val angularVelocityId: ``` |
| **applyForceData** : [Vector3AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3attributedata) [Get] | Signature ```kotlin val applyForceData: Vector3AttributeData ``` |
| **applyForceId** [Get] | Signature ```kotlin val applyForceId: ``` |
| **attributeKeys_** : IntArray [Get] | Signature ```kotlin val attributeKeys_: IntArray ``` |
| **attributeTypeCounts_** : IntArray [Get] | Signature ```kotlin val attributeTypeCounts_: IntArray ``` |
| **attributeTypes_** : IntArray [Get] | Signature ```kotlin val attributeTypes_: IntArray ``` |
| **attrMetaData_** : Map [Get] | Signature ```kotlin val attrMetaData_: Map ``` |
| **createDefaultInstance** : Function0 [Get] | Signature ```kotlin open override val createDefaultInstance: () -> Physics ``` |
| **densityInternalData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val densityInternalData: FloatAttributeData ``` |
| **densityInternalId** [Get] | Signature ```kotlin val densityInternalId: ``` |
| **dimensionsData** : [Vector3AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3attributedata) [Get] | Signature ```kotlin val dimensionsData: Vector3AttributeData ``` |
| **dimensionsId** [Get] | Signature ```kotlin val dimensionsId: ``` |
| **enumClassesMap_** : Map [Get] | Signature ```kotlin val enumClassesMap_: Map<Int, Class<out Enum<*>>> ``` |
| **frictionInternalData** : [Vector3AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3attributedata) [Get] | Signature ```kotlin val frictionInternalData: Vector3AttributeData ``` |
| **frictionInternalId** [Get] | Signature ```kotlin val frictionInternalId: ``` |
| **id** [Get] | Signature ```kotlin open override val id: ``` |
| **keyStringToKeyIntMap_** : Map [Get] | Signature ```kotlin val keyStringToKeyIntMap_: Map<String, Int> ``` |
| **linearVelocityData** : [Vector3AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3attributedata) [Get] | Signature ```kotlin val linearVelocityData: Vector3AttributeData ``` |
| **linearVelocityId** [Get] | Signature ```kotlin val linearVelocityId: ``` |
| **restitutionData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val restitutionData: FloatAttributeData ``` |
| **restitutionId** [Get] | Signature ```kotlin val restitutionId: ``` |
| **shapeData** : [StringAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_stringattributedata) [Get] | Signature ```kotlin val shapeData: StringAttributeData ``` |
| **shapeId** [Get] | Signature ```kotlin val shapeId: ``` |
| **stateData** : [EnumAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_enumattributedata) [Get] | Signature ```kotlin val stateData: EnumAttributeData ``` |
| **stateId** [Get] | Signature ```kotlin val stateId: ``` |

### Companion Object Functions

| **attributeKeys** () | Signature ```kotlin open override fun attributeKeys(): IntArray ``` Returns IntArray |
| --- | --- |
| **attributeMetaData** () | Returns Map |
| **attributeTypeCountAvailable** () | Signature ```kotlin open override fun attributeTypeCountAvailable(): Boolean ``` Returns Boolean |
| **attributeTypeCounts** () | Signature ```kotlin open override fun attributeTypeCounts(): IntArray ``` Returns IntArray |
| **attributeTypes** () | Signature ```kotlin open override fun attributeTypes(): IntArray ``` Returns IntArray |
| **dependents** () | Signature ```kotlin open fun dependents(): IntArray ``` Returns IntArray |
| **enumClassesMap** () | Signature ```kotlin open override fun enumClassesMap(): Map<Int, Class<out Enum<*>>> ``` Returns Map |
| **keyStringToKeyIntMap** ( keyString ) | Signature ```kotlin open override fun keyStringToKeyIntMap(keyString: String): Int? ``` Parameters keyString: String Returns Int? |