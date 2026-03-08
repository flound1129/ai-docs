# MRUKAnchor Class

Extends
[ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase)
*Modifiers:
final*

## Signature

```kotlin
class MRUKAnchor(roomUuid: UUID = UUID(0L, 0L), uuid: UUID = UUID(0L, 0L), handle: Long = 0, labelsCount: Int = 0, parentAnchor: Entity = Entity.nullEntity()) : ComponentBase
```

## Constructors

| **MRUKAnchor** ( roomUuid , uuid , handle , labels , parent ) | Signature ```kotlin constructor(roomUuid: UUID, uuid: UUID = UUID(0, 0), handle: Long = 0, labels: List<MRUKLabel> = listOf(), parent: Entity = Entity.nullEntity()) ``` Parameters roomUuid: UUID uuid: UUID handle: Long labels: List parent: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) Returns [MRUKAnchor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukanchor) |
| --- | --- |
| **MRUKAnchor** ( roomUuid , uuid , handle , labelsCount , parentAnchor ) | Signature ```kotlin constructor(roomUuid: UUID = UUID(0L, 0L), uuid: UUID = UUID(0L, 0L), handle: Long = 0, labelsCount: Int = 0, parentAnchor: Entity = Entity.nullEntity()) ``` Parameters roomUuid: UUID uuid: UUID handle: Long labelsCount: Int parentAnchor: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) Returns [MRUKAnchor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukanchor) |

## Properties

| **cachable** : BuildConfig.COMPONENTCACHE_LEVEL >= 1 [Get][Set] | Signature ```kotlin open override var cachable: BuildConfig.COMPONENTCACHE_LEVEL >= 1 ``` |
| --- | --- |
| **entID** : Long [Get][Set] | Signature ```kotlin var entID: Long ``` |
| **handle** : Long [Get][Set] | Signature ```kotlin var handle: Long ``` |
| **isDirty** : Boolean [Get][Set] | Signature ```kotlin var isDirty: Boolean ``` |
| **labels** : MapDelegate [Get][Set] | Signature ```kotlin var labels: MapDelegate<Int, String> ``` |
| **labelsCount** : Int [Get][Set] | Signature ```kotlin var labelsCount: Int ``` |
| **parentAnchor** : [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) [Get][Set] | Signature ```kotlin var parentAnchor: Entity ``` |
| **recycled** : Boolean [Get][Set] | Signature ```kotlin var recycled: Boolean ``` |
| **roomUuid** : UUID [Get][Set] | Signature ```kotlin var roomUuid: UUID ``` |
| **timeStamp** : Long [Get][Set] | Signature ```kotlin var timeStamp: Long ``` |
| **uuid** : UUID [Get][Set] | Signature ```kotlin var uuid: UUID ``` |

## Functions

| **companion** () | Gets the companion object for this component. The companion object provides metadata about the component. Signature ```kotlin open override fun companion(): ComponentCompanion ``` Returns [ComponentCompanion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentcompanion) The component's companion object Throws RuntimeException If the companion is not implemented |
| --- | --- |
| **getAnchor** () | Signature ```kotlin fun MRUKAnchor.getAnchor(): Anchor ``` Returns [Anchor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_anchor) |
| **getComponentDataAttributeType** ( key ) | Gets the attribute type for the specified key. Signature ```kotlin fun getComponentDataAttributeType(key: Int): AttributePrimitive? ``` Parameters key: Int The integer key to look up Returns [AttributePrimitive?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_attributeprimitive) The attribute primitive type, or null if the key doesn't exist |
| **getComponentDataAttributeType** ( keyString ) | Gets the attribute type for the specified string key. Signature ```kotlin fun getComponentDataAttributeType(keyString: String): AttributePrimitive? ``` Parameters keyString: String The string key to look up Returns [AttributePrimitive?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_attributeprimitive) The attribute primitive type Throws IllegalArgumentException If the key doesn't exist |
| **getComponentDataKey** ( key ) | Gets the integer key associated with the specified string key. Signature ```kotlin fun getComponentDataKey(key: String): Int? ``` Parameters key: String The string key to look up Returns Int? The integer key, or null if the string key doesn't exist |
| **getComponentDataValue** ( key ) | Gets the value for the specified key. Signature ```kotlin fun getComponentDataValue(key: Int): Any? ``` Parameters key: Int The integer key to look up Returns Any? The value associated with the key, or null if the key doesn't exist |
| **getComponentDataValue** ( keyString ) | Gets the value for the specified string key. Signature ```kotlin fun getComponentDataValue(keyString: String): Any? ``` Parameters keyString: String The string key to look up Returns Any? The value associated with the key, or null if the key doesn't exist Throws IllegalArgumentException If the key doesn't exist |
| **getEnumClass** ( key ) | Gets the enum class associated with the specified string key. Signature ```kotlin fun getEnumClass(key: String): Class<out Enum<*>>? ``` Parameters key: String The string key to look up Returns Class? The enum class, or null if the key doesn't exist or is not an enum |
| **getLabelsAsList** () | Signature ```kotlin fun MRUKAnchor.getLabelsAsList(): List<MRUKLabel> ``` Returns List |
| **hasComponentData** ( key ) | Checks if this component has data for the specified key. Signature ```kotlin fun hasComponentData(key: Int): Boolean ``` Parameters key: Int The integer key to check Returns Boolean True if the component has data for the key, false otherwise |
| **hasComponentData** ( keyString ) | Checks if this component has data for the specified string key. Signature ```kotlin fun hasComponentData(keyString: String): Boolean ``` Parameters keyString: String The string key to check Returns Boolean True if the component has data for the key, false otherwise |
| **hasLabel** ( labelToCheck ) | Signature ```kotlin fun MRUKAnchor.hasLabel(labelToCheck: MRUKLabel): Boolean ``` Parameters labelToCheck: [MRUKLabel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mruklabel) Returns Boolean |
| **hasLabels** ( labelsToCheck ) | Signature ```kotlin fun MRUKAnchor.hasLabels(labelsToCheck: List<MRUKLabel>): Boolean ``` Parameters labelsToCheck: List Returns Boolean |
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

| **attributeKeys_** : IntArray [Get] | Signature ```kotlin val attributeKeys_: IntArray ``` |
| --- | --- |
| **attributeTypeCounts_** : IntArray [Get] | Signature ```kotlin val attributeTypeCounts_: IntArray ``` |
| **attributeTypes_** : IntArray [Get] | Signature ```kotlin val attributeTypes_: IntArray ``` |
| **attrMetaData_** : Map [Get] | Signature ```kotlin val attrMetaData_: Map ``` |
| **createDefaultInstance** : Function0 [Get] | Signature ```kotlin open override val createDefaultInstance: () -> MRUKAnchor ``` |
| **enumClassesMap_** : Map [Get] | Signature ```kotlin val enumClassesMap_: Map<Int, Class<out Enum<*>>> ``` |
| **handleData** : [LongAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_longattributedata) [Get] | Signature ```kotlin val handleData: LongAttributeData ``` |
| **handleId** [Get] | Signature ```kotlin val handleId: ``` |
| **id** [Get] | Signature ```kotlin open override val id: ``` |
| **keyStringToKeyIntMap_** : Map [Get] | Signature ```kotlin val keyStringToKeyIntMap_: Map<String, Int> ``` |
| **labelsCountData** : [IntAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_intattributedata) [Get] | Signature ```kotlin val labelsCountData: IntAttributeData ``` |
| **labelsCountId** [Get] | Signature ```kotlin val labelsCountId: ``` |
| **labelsData** : [ExperimentalMapAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_experimentalmapattributedata) [Get] | Signature ```kotlin val labelsData: ExperimentalMapAttributeData<Int, String> ``` |
| **labelsId** [Get] | Signature ```kotlin val labelsId: ``` |
| **parentAnchorData** : [EntityAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entityattributedata) [Get] | Signature ```kotlin val parentAnchorData: EntityAttributeData ``` |
| **parentAnchorId** [Get] | Signature ```kotlin val parentAnchorId: ``` |
| **roomUuidData** : [UUIDAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_uuidattributedata) [Get] | Signature ```kotlin val roomUuidData: UUIDAttributeData ``` |
| **roomUuidId** [Get] | Signature ```kotlin val roomUuidId: ``` |
| **uuidData** : [UUIDAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_uuidattributedata) [Get] | Signature ```kotlin val uuidData: UUIDAttributeData ``` |
| **uuidId** [Get] | Signature ```kotlin val uuidId: ``` |

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