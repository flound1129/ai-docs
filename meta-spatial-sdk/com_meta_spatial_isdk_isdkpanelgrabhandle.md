# IsdkPanelGrabHandle Class

Extends
[ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase)
*Modifiers:
final*

IsdkPanelGrabHandle adds a grab handle to panels. Must add IsdkGrabbable to make the panel grabbable.

```kotlin Visual dimensions are hardcoded (66dp edges, 52dp resize corners). Collision widths/sizes directly set collider dimensions in native layer.

@param grabHandleCollisionWidths Collision widths for edge and grab corner hitboxes (left, top, right, bottom) in meters - Android Rect order. These values directly set collider widths.
@param resizeCornerCollisionSizes Collision sizes for resize corner hitboxes (TL, TR, BR, BL) in meters - clockwise from top-left. These values directly set collider sizes.
@param resizeCornerCollisionInset Moves resize corner colliders inward toward panel center (meters). Default 0.005m (6dp) matches hardcoded visual overlap. Does not affect viual.
@param outset Outset from panel edges (left, top, right, bottom) in meters - Android Rect order. Positive values expand grab area outward from each edge independently.
@param zOffset Front/back offset distance from panel surface in meters. Positive values move handles forward (toward user), negative values move backward.
@param color Base color for handle segments (RGBA). 233/255 = 0.9137 for light gray.
@param scaleFactor Scale factor for handle segments and outsets (width, height). Set to panel scale for uniform scaling, or (1, 1) for constant-size handles. ```

## Signature

```kotlin
class IsdkPanelGrabHandle(grabHandleCollisionWidths: Vector4 = Vector4(0.061f, 0.061f, 0.061f, 0.061f), resizeCornerCollisionSizes: Vector4 = Vector4(0.105f, 0.105f, 0.105f, 0.105f), resizeCornerCollisionInset: Float = 0.015f, outset: Vector4 = Vector4(0.0f, 0.0f, 0.0f, 0.0f), zOffset: Float = 0.0f, color: Vector4 = Vector4(0.9137f, 0.9137f, 0.9137f, 1.0f), scaleFactor: Vector2 = Vector2(1.0f, 1.0f)) : ComponentBase
```

## Constructors

| **IsdkPanelGrabHandle** ( grabHandleCollisionWidths , resizeCornerCollisionSizes , resizeCornerCollisionInset , outset , zOffset , color , scaleFactor ) | Signature ```kotlin constructor(grabHandleCollisionWidths: Vector4 = Vector4(0.061f, 0.061f, 0.061f, 0.061f), resizeCornerCollisionSizes: Vector4 = Vector4(0.105f, 0.105f, 0.105f, 0.105f), resizeCornerCollisionInset: Float = 0.015f, outset: Vector4 = Vector4(0.0f, 0.0f, 0.0f, 0.0f), zOffset: Float = 0.0f, color: Vector4 = Vector4(0.9137f, 0.9137f, 0.9137f, 1.0f), scaleFactor: Vector2 = Vector2(1.0f, 1.0f)) ``` Parameters grabHandleCollisionWidths: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) resizeCornerCollisionSizes: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) resizeCornerCollisionInset: Float outset: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) zOffset: Float color: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) scaleFactor: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) Returns [IsdkPanelGrabHandle](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdkpanelgrabhandle) |
| --- | --- |

## Properties

| **cachable** : BuildConfig.COMPONENTCACHE_LEVEL >= 1 [Get][Set] | Signature ```kotlin open override var cachable: BuildConfig.COMPONENTCACHE_LEVEL >= 1 ``` |
| --- | --- |
| **color** : [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) [Get][Set] | Base color for handle segments (RGBA). 233/255 = 0.9137 for light gray. Signature ```kotlin var color: Vector4 ``` |
| **entID** : Long [Get][Set] | Signature ```kotlin var entID: Long ``` |
| **grabHandleCollisionWidths** : [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) [Get][Set] | Collision widths for edge and grab corner hitboxes (left, top, right, bottom) in meters - Android Rect order. These values directly set collider widths. Signature ```kotlin var grabHandleCollisionWidths: Vector4 ``` |
| **isDirty** : Boolean [Get][Set] | Signature ```kotlin var isDirty: Boolean ``` |
| **outset** : [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) [Get][Set] | Outset from panel edges (left, top, right, bottom) in meters - Android Rect order. Positive values expand grab area outward from each edge independently. Signature ```kotlin var outset: Vector4 ``` |
| **recycled** : Boolean [Get][Set] | Signature ```kotlin var recycled: Boolean ``` |
| **resizeCornerCollisionInset** : Float [Get][Set] | Moves resize corner colliders inward toward panel center (meters). Default 0.005m (6dp) matches hardcoded visual overlap. Does not affect viual. Signature ```kotlin var resizeCornerCollisionInset: Float ``` |
| **resizeCornerCollisionSizes** : [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) [Get][Set] | Collision sizes for resize corner hitboxes (TL, TR, BR, BL) in meters - clockwise from top-left. These values directly set collider sizes. Signature ```kotlin var resizeCornerCollisionSizes: Vector4 ``` |
| **scaleFactor** : [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) [Get][Set] | Scale factor for handle segments and outsets (width, height). Set to panel scale for uniform scaling, or (1, 1) for constant-size handles. Signature ```kotlin var scaleFactor: Vector2 ``` |
| **timeStamp** : Long [Get][Set] | Signature ```kotlin var timeStamp: Long ``` |
| **zOffset** : Float [Get][Set] | Front/back offset distance from panel surface in meters. Positive values move handles forward (toward user), negative values move backward. Signature ```kotlin var zOffset: Float ``` |

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
| **colorData** : [Vector4AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4attributedata) [Get] | Signature ```kotlin val colorData: Vector4AttributeData ``` |
| **colorId** [Get] | Signature ```kotlin val colorId: ``` |
| **createDefaultInstance** : Function0 [Get] | Signature ```kotlin open override val createDefaultInstance: () -> IsdkPanelGrabHandle ``` |
| **enumClassesMap_** : Map [Get] | Signature ```kotlin val enumClassesMap_: Map<Int, Class<out Enum<*>>> ``` |
| **grabHandleCollisionWidthsData** : [Vector4AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4attributedata) [Get] | Signature ```kotlin val grabHandleCollisionWidthsData: Vector4AttributeData ``` |
| **grabHandleCollisionWidthsId** [Get] | Signature ```kotlin val grabHandleCollisionWidthsId: ``` |
| **id** [Get] | Signature ```kotlin open override val id: ``` |
| **keyStringToKeyIntMap_** : Map [Get] | Signature ```kotlin val keyStringToKeyIntMap_: Map<String, Int> ``` |
| **outsetData** : [Vector4AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4attributedata) [Get] | Signature ```kotlin val outsetData: Vector4AttributeData ``` |
| **outsetId** [Get] | Signature ```kotlin val outsetId: ``` |
| **resizeCornerCollisionInsetData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val resizeCornerCollisionInsetData: FloatAttributeData ``` |
| **resizeCornerCollisionInsetId** [Get] | Signature ```kotlin val resizeCornerCollisionInsetId: ``` |
| **resizeCornerCollisionSizesData** : [Vector4AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4attributedata) [Get] | Signature ```kotlin val resizeCornerCollisionSizesData: Vector4AttributeData ``` |
| **resizeCornerCollisionSizesId** [Get] | Signature ```kotlin val resizeCornerCollisionSizesId: ``` |
| **scaleFactorData** : [Vector2AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2attributedata) [Get] | Signature ```kotlin val scaleFactorData: Vector2AttributeData ``` |
| **scaleFactorId** [Get] | Signature ```kotlin val scaleFactorId: ``` |
| **zOffsetData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val zOffsetData: FloatAttributeData ``` |
| **zOffsetId** [Get] | Signature ```kotlin val zOffsetId: ``` |

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