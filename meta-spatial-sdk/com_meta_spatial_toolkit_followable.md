# Followable Class

Extends
[ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase)
*Modifiers:
final*

Followable is a component that enables an entity to stay in front of another entity. Followable will track the orientation of the parent and move itself to stay in front.

## Signature

```kotlin
class Followable(target: Entity = Entity.nullEntity(), offset: Pose = Pose(Vector3(0.0f, 0.0f, 3.0f), Quaternion(0.0f, 0.0f, 1.0f, 0.0f)), minAngle: Float = -90f, maxAngle: Float = 90.0f, type: FollowableType = FollowableType.FACE, tolerance: Float = 0.2f, speed: Float = 1.0f, active: Boolean = true) : ComponentBase
```

## Constructors

| **Followable** ( target , offset , minAngle , maxAngle , type , tolerance , speed , active ) | Signature ```kotlin constructor(target: Entity = Entity.nullEntity(), offset: Pose = Pose(Vector3(0.0f, 0.0f, 3.0f), Quaternion(0.0f, 0.0f, 1.0f, 0.0f)), minAngle: Float = -90f, maxAngle: Float = 90.0f, type: FollowableType = FollowableType.FACE, tolerance: Float = 0.2f, speed: Float = 1.0f, active: Boolean = true) ``` Parameters target: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) Target Entity to follow offset: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) Pose offset to keep from target. Defining a quaternion will rotate the Entity minAngle: Float Minimum Y angle offset a followable will keep from target, 0 is straight ahead, positive values are up, negative values are down maxAngle: Float Maximum Y angle offset a followable will keep from target, 0 is straight ahead, positive values are up, negative values are down type: [FollowableType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_followabletype) The behavior an object has when following (faces user, pivots on y axis, etc.) tolerance: Float This is the change in distance needed to start moving speed: Float How fast followable tracks to its desired location. Float value is a percent of default speed active: Boolean Whether entity is actively following or not Returns [Followable](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_followable) |
| --- | --- |

## Properties

| **active** : Boolean [Get][Set] | Whether entity is actively following or not Signature ```kotlin var active: Boolean ``` |
| --- | --- |
| **cachable** : BuildConfig.COMPONENTCACHE_LEVEL >= 1 [Get][Set] | Signature ```kotlin open override var cachable: BuildConfig.COMPONENTCACHE_LEVEL >= 1 ``` |
| **entID** : Long [Get][Set] | Signature ```kotlin var entID: Long ``` |
| **isDirty** : Boolean [Get][Set] | Signature ```kotlin var isDirty: Boolean ``` |
| **maxAngle** : Float [Get][Set] | Maximum Y angle offset a followable will keep from target, 0 is straight ahead, positive values are up, negative values are down Signature ```kotlin var maxAngle: Float ``` |
| **minAngle** : Float [Get][Set] | Minimum Y angle offset a followable will keep from target, 0 is straight ahead, positive values are up, negative values are down Signature ```kotlin var minAngle: Float ``` |
| **offset** : [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) [Get][Set] | Pose offset to keep from target. Defining a quaternion will rotate the Entity Signature ```kotlin var offset: Pose ``` |
| **recycled** : Boolean [Get][Set] | Signature ```kotlin var recycled: Boolean ``` |
| **speed** : Float [Get][Set] | How fast followable tracks to its desired location. Float value is a percent of default speed Signature ```kotlin var speed: Float ``` |
| **target** : [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) [Get][Set] | Target Entity to follow Signature ```kotlin var target: Entity ``` |
| **timeStamp** : Long [Get][Set] | Signature ```kotlin var timeStamp: Long ``` |
| **tolerance** : Float [Get][Set] | This is the change in distance needed to start moving Signature ```kotlin var tolerance: Float ``` |
| **type** : [FollowableType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_followabletype) [Get][Set] | The type of behavior an object has when following (faces user, pivots on y axis, etc.) Signature ```kotlin var type: FollowableType ``` |

## Functions

| **companion** () | Gets the companion object for this component. The companion object provides metadata about the component. Signature ```kotlin open override fun companion(): ComponentCompanion ``` Returns [ComponentCompanion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentcompanion) The component's companion object Throws RuntimeException If the companion is not implemented |
| --- | --- |
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

| **activeData** : [BooleanAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_booleanattributedata) [Get] | Signature ```kotlin val activeData: BooleanAttributeData ``` |
| --- | --- |
| **activeId** [Get] | Signature ```kotlin val activeId: ``` |
| **attributeKeys_** : IntArray [Get] | Signature ```kotlin val attributeKeys_: IntArray ``` |
| **attributeTypeCounts_** : IntArray [Get] | Signature ```kotlin val attributeTypeCounts_: IntArray ``` |
| **attributeTypes_** : IntArray [Get] | Signature ```kotlin val attributeTypes_: IntArray ``` |
| **attrMetaData_** : Map [Get] | Signature ```kotlin val attrMetaData_: Map ``` |
| **createDefaultInstance** : Function0 [Get] | Signature ```kotlin open override val createDefaultInstance: () -> Followable ``` |
| **enumClassesMap_** : Map [Get] | Signature ```kotlin val enumClassesMap_: Map<Int, Class<out Enum<*>>> ``` |
| **id** [Get] | Signature ```kotlin open override val id: ``` |
| **keyStringToKeyIntMap_** : Map [Get] | Signature ```kotlin val keyStringToKeyIntMap_: Map<String, Int> ``` |
| **maxAngleData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val maxAngleData: FloatAttributeData ``` |
| **maxAngleId** [Get] | Signature ```kotlin val maxAngleId: ``` |
| **minAngleData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val minAngleData: FloatAttributeData ``` |
| **minAngleId** [Get] | Signature ```kotlin val minAngleId: ``` |
| **offsetData** : [PoseAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_poseattributedata) [Get] | Signature ```kotlin val offsetData: PoseAttributeData ``` |
| **offsetId** [Get] | Signature ```kotlin val offsetId: ``` |
| **speedData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val speedData: FloatAttributeData ``` |
| **speedId** [Get] | Signature ```kotlin val speedId: ``` |
| **targetData** : [EntityAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entityattributedata) [Get] | Signature ```kotlin val targetData: EntityAttributeData ``` |
| **targetId** [Get] | Signature ```kotlin val targetId: ``` |
| **toleranceData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val toleranceData: FloatAttributeData ``` |
| **toleranceId** [Get] | Signature ```kotlin val toleranceId: ``` |
| **typeData** : [EnumAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_enumattributedata) [Get] | Signature ```kotlin val typeData: EnumAttributeData ``` |
| **typeId** [Get] | Signature ```kotlin val typeId: ``` |

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