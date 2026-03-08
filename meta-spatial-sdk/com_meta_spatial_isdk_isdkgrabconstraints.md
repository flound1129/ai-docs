# IsdkGrabConstraints Class

Extends
[ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase)
*Modifiers:
final*

IsdkGrabConstraints specifies constraints for Grabbable interactions when the IsdkFeature is active.     @param lockFlags flags controlling transformations are locked during grabbing     @param scaleMinMax the minimum and maximum scale values for the object     @param verticalMinMax the minimum and maximum vertical values for the object     @param depthMinMax the minimum and maximum depth values for the object     @param lateralMinMax the minimum and maximum lateral values for the object     @param maxGrabbers the maximum number of grabbers allowed for the object

## Signature

```kotlin
class IsdkGrabConstraints(lockFlagsValue: Int = 0, scaleMinMax: Vector2 = Vector2(-Float.MAX_VALUE, Float.MAX_VALUE), verticalMinMax: Vector2 = Vector2(-Float.MAX_VALUE, Float.MAX_VALUE), depthMinMax: Vector2 = Vector2(-Float.MAX_VALUE, Float.MAX_VALUE), lateralMinMax: Vector2 = Vector2(-Float.MAX_VALUE, Float.MAX_VALUE), maxGrabbers: Int = 1) : ComponentBase
```

## Constructors

| **IsdkGrabConstraints** ( lockFlagsValue , scaleMinMax , verticalMinMax , depthMinMax , lateralMinMax , maxGrabbers ) | Signature ```kotlin constructor(lockFlagsValue: Int = 0, scaleMinMax: Vector2 = Vector2(-Float.MAX_VALUE, Float.MAX_VALUE), verticalMinMax: Vector2 = Vector2(-Float.MAX_VALUE, Float.MAX_VALUE), depthMinMax: Vector2 = Vector2(-Float.MAX_VALUE, Float.MAX_VALUE), lateralMinMax: Vector2 = Vector2(-Float.MAX_VALUE, Float.MAX_VALUE), maxGrabbers: Int = 1) ``` Parameters lockFlagsValue: Int scaleMinMax: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) verticalMinMax: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) depthMinMax: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) lateralMinMax: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) maxGrabbers: Int Returns [IsdkGrabConstraints](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdkgrabconstraints) |
| --- | --- |

## Properties

| **cachable** : BuildConfig.COMPONENTCACHE_LEVEL >= 1 [Get][Set] | Signature ```kotlin open override var cachable: BuildConfig.COMPONENTCACHE_LEVEL >= 1 ``` |
| --- | --- |
| **depthMinMax** : [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) [Get][Set] | the minimum and maximum depth values for the object Signature ```kotlin var depthMinMax: Vector2 ``` |
| **entID** : Long [Get][Set] | Signature ```kotlin var entID: Long ``` |
| **isDirty** : Boolean [Get][Set] | Signature ```kotlin var isDirty: Boolean ``` |
| **lateralMinMax** : [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) [Get][Set] | the minimum and maximum lateral values for the object Signature ```kotlin var lateralMinMax: Vector2 ``` |
| **lockFlags** : IsdkGrabConstraints.LockFlags [Get][Set] | Signature ```kotlin var lockFlags: IsdkGrabConstraints.LockFlags ``` |
| **lockFlagsValue** : Int [Get][Set] | flags controlling transformations are locked during grabbing Signature ```kotlin var lockFlagsValue: Int ``` |
| **maxGrabbers** : Int [Get][Set] | the maximum number of grabbers allowed for the object Signature ```kotlin var maxGrabbers: Int ``` |
| **recycled** : Boolean [Get][Set] | Signature ```kotlin var recycled: Boolean ``` |
| **scaleMinMax** : [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) [Get][Set] | the minimum and maximum scale values for the object Signature ```kotlin var scaleMinMax: Vector2 ``` |
| **timeStamp** : Long [Get][Set] | Signature ```kotlin var timeStamp: Long ``` |
| **verticalMinMax** : [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) [Get][Set] | the minimum and maximum vertical values for the object Signature ```kotlin var verticalMinMax: Vector2 ``` |

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

| **attributeKeys_** : IntArray [Get] | Signature ```kotlin val attributeKeys_: IntArray ``` |
| --- | --- |
| **attributeTypeCounts_** : IntArray [Get] | Signature ```kotlin val attributeTypeCounts_: IntArray ``` |
| **attributeTypes_** : IntArray [Get] | Signature ```kotlin val attributeTypes_: IntArray ``` |
| **attrMetaData_** : Map [Get] | Signature ```kotlin val attrMetaData_: Map ``` |
| **createDefaultInstance** : Function0 [Get] | Signature ```kotlin open override val createDefaultInstance: () -> IsdkGrabConstraints ``` |
| **depthMinMaxData** : [Vector2AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2attributedata) [Get] | Signature ```kotlin val depthMinMaxData: Vector2AttributeData ``` |
| **depthMinMaxId** [Get] | Signature ```kotlin val depthMinMaxId: ``` |
| **enumClassesMap_** : Map [Get] | Signature ```kotlin val enumClassesMap_: Map<Int, Class<out Enum<*>>> ``` |
| **id** [Get] | Signature ```kotlin open override val id: ``` |
| **keyStringToKeyIntMap_** : Map [Get] | Signature ```kotlin val keyStringToKeyIntMap_: Map<String, Int> ``` |
| **lateralMinMaxData** : [Vector2AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2attributedata) [Get] | Signature ```kotlin val lateralMinMaxData: Vector2AttributeData ``` |
| **lateralMinMaxId** [Get] | Signature ```kotlin val lateralMinMaxId: ``` |
| **lockFlagsValueData** : [IntAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_intattributedata) [Get] | Signature ```kotlin val lockFlagsValueData: IntAttributeData ``` |
| **lockFlagsValueId** [Get] | Signature ```kotlin val lockFlagsValueId: ``` |
| **maxGrabbersData** : [IntAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_intattributedata) [Get] | Signature ```kotlin val maxGrabbersData: IntAttributeData ``` |
| **maxGrabbersId** [Get] | Signature ```kotlin val maxGrabbersId: ``` |
| **scaleMinMaxData** : [Vector2AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2attributedata) [Get] | Signature ```kotlin val scaleMinMaxData: Vector2AttributeData ``` |
| **scaleMinMaxId** [Get] | Signature ```kotlin val scaleMinMaxId: ``` |
| **verticalMinMaxData** : [Vector2AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2attributedata) [Get] | Signature ```kotlin val verticalMinMaxData: Vector2AttributeData ``` |
| **verticalMinMaxId** [Get] | Signature ```kotlin val verticalMinMaxId: ``` |

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

## Inner Class

### LockFlags Class

*Modifiers:
final*

Companion Object
Companion Object Properties
| **ALL** : IsdkGrabConstraints.LockFlags [Get] | Signature ```kotlin val ALL: IsdkGrabConstraints.LockFlags ``` |
| --- | --- |
| **NONE** : IsdkGrabConstraints.LockFlags [Get] | Signature ```kotlin val NONE: IsdkGrabConstraints.LockFlags ``` |
| **POSITION** : IsdkGrabConstraints.LockFlags [Get] | Signature ```kotlin val POSITION: IsdkGrabConstraints.LockFlags ``` |
| **ROTATION** : IsdkGrabConstraints.LockFlags [Get] | Signature ```kotlin val ROTATION: IsdkGrabConstraints.LockFlags ``` |
| **SCALE** : IsdkGrabConstraints.LockFlags [Get] | Signature ```kotlin val SCALE: IsdkGrabConstraints.LockFlags ``` |

Companion Object Functions
| **valueOf** ( value ) | Signature ```kotlin fun valueOf(value: Int): IsdkGrabConstraints.LockFlags ``` Parameters value: Int Returns IsdkGrabConstraints.LockFlags |
| --- | --- |

Signature
```kotlin
class LockFlags(val value: Int)
```

Constructors
| **LockFlags** ( value ) | Signature ```kotlin constructor(value: Int) ``` Parameters value: Int Returns IsdkGrabConstraints.LockFlags |
| --- | --- |

Properties
| **value** : Int [Get] | Signature ```kotlin val value: Int ``` |
| --- | --- |

Functions
| **contains** ( flag ) | Signature ```kotlin operator fun contains(flag: IsdkGrabConstraints.LockFlags): Boolean ``` Parameters flag: IsdkGrabConstraints.LockFlags Returns Boolean |
| --- | --- |
| **or** ( other ) | Signature ```kotlin infix fun or(other: IsdkGrabConstraints.LockFlags): IsdkGrabConstraints.LockFlags ``` Parameters other: IsdkGrabConstraints.LockFlags Returns IsdkGrabConstraints.LockFlags |