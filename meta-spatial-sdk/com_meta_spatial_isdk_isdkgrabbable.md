# IsdkGrabbable Class

Extends
[ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase)
*Modifiers:
final*

IsdkGrabbable provides a grabbable object for ISDK interactions. It can be used instead of the regular Grabbable component when more fine grained control over the grab behavior is required.     @param enabled whether the object is grabbable     @param grabState the current grab state of the object     @param movementType the type of movement allowed for the object     @param responsiveness the responsiveness of the object     @param billboardOrientation orientation offset to be applied after the transform faces towards the user

## Signature

```kotlin
class IsdkGrabbable(enabled: Boolean = true, grabState: IsdkGrabState = IsdkGrabState.NotGrabbed, movementType: IsdkGrabMovementType = IsdkGrabMovementType.Direct, responsiveness: Float = 0.15f, billboardOrientation: Vector3 = Vector3(0.0f, 0.0f, 0.0f)) : ComponentBase
```

## Constructors

| **IsdkGrabbable** ( enabled , grabState , movementType , responsiveness , billboardOrientation ) | Signature ```kotlin constructor(enabled: Boolean = true, grabState: IsdkGrabState = IsdkGrabState.NotGrabbed, movementType: IsdkGrabMovementType = IsdkGrabMovementType.Direct, responsiveness: Float = 0.15f, billboardOrientation: Vector3 = Vector3(0.0f, 0.0f, 0.0f)) ``` Parameters enabled: Boolean grabState: [IsdkGrabState](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdkgrabstate) movementType: [IsdkGrabMovementType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdkgrabmovementtype) responsiveness: Float billboardOrientation: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) Returns [IsdkGrabbable](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdkgrabbable) |
| --- | --- |

## Properties

| **billboardOrientation** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get][Set] | Additional orientation offset of the billboard to be applied after the transform faces towards the user. Field order is Pitch, Yaw, Roll. Units are degrees. This is only used when movementType is IsdkGrabMovementType.Billboard or IsdkGrabMovementType.AxialBillboard Signature ```kotlin var billboardOrientation: Vector3 ``` |
| --- | --- |
| **cachable** : BuildConfig.COMPONENTCACHE_LEVEL >= 1 [Get][Set] | Signature ```kotlin open override var cachable: BuildConfig.COMPONENTCACHE_LEVEL >= 1 ``` |
| **enabled** : Boolean [Get][Set] | whether the object is grabbable Signature ```kotlin var enabled: Boolean ``` |
| **entID** : Long [Get][Set] | Signature ```kotlin var entID: Long ``` |
| **grabState** : [IsdkGrabState](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdkgrabstate) [Get][Set] | the current grab state of the object Signature ```kotlin var grabState: IsdkGrabState ``` |
| **isDirty** : Boolean [Get][Set] | Signature ```kotlin var isDirty: Boolean ``` |
| **movementType** : [IsdkGrabMovementType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdkgrabmovementtype) [Get][Set] | the type of movement allowed for the object Signature ```kotlin var movementType: IsdkGrabMovementType ``` |
| **recycled** : Boolean [Get][Set] | Signature ```kotlin var recycled: Boolean ``` |
| **responsiveness** : Float [Get][Set] | the responsiveness of the object: 1 moves instantly, values between 0 to 1 are smooth, 0 is immovable Signature ```kotlin var responsiveness: Float ``` |
| **timeStamp** : Long [Get][Set] | Signature ```kotlin var timeStamp: Long ``` |

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
| **billboardOrientationData** : [Vector3AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3attributedata) [Get] | Signature ```kotlin val billboardOrientationData: Vector3AttributeData ``` |
| **billboardOrientationId** [Get] | Signature ```kotlin val billboardOrientationId: ``` |
| **createDefaultInstance** : Function0 [Get] | Signature ```kotlin open override val createDefaultInstance: () -> IsdkGrabbable ``` |
| **enabledData** : [BooleanAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_booleanattributedata) [Get] | Signature ```kotlin val enabledData: BooleanAttributeData ``` |
| **enabledId** [Get] | Signature ```kotlin val enabledId: ``` |
| **enumClassesMap_** : Map [Get] | Signature ```kotlin val enumClassesMap_: Map<Int, Class<out Enum<*>>> ``` |
| **grabStateData** : [EnumAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_enumattributedata) [Get] | Signature ```kotlin val grabStateData: EnumAttributeData ``` |
| **grabStateId** [Get] | Signature ```kotlin val grabStateId: ``` |
| **id** [Get] | Signature ```kotlin open override val id: ``` |
| **keyStringToKeyIntMap_** : Map [Get] | Signature ```kotlin val keyStringToKeyIntMap_: Map<String, Int> ``` |
| **movementTypeData** : [EnumAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_enumattributedata) [Get] | Signature ```kotlin val movementTypeData: EnumAttributeData ``` |
| **movementTypeId** [Get] | Signature ```kotlin val movementTypeId: ``` |
| **responsivenessData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val responsivenessData: FloatAttributeData ``` |
| **responsivenessId** [Get] | Signature ```kotlin val responsivenessId: ``` |

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