# IsdkPanelResize Class

Extends
[ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase)
*Modifiers:
final*

IsdkPanelResize enables interactive resizing of panels through corner handles.

```kotlin @param enabled Whether resize functionality is enabled
@param resizeMode Mode of resizing (Simple, Relayout, None)
@param minDimensions Minimum panel dimensions (width, height) in meters
@param maxDimensions Maximum panel dimensions (width, height) in meters
@param preserveAspectRatio Whether to maintain aspect ratio during resize
@param resizeSensitivity Sensitivity multiplier for resize drag movement
@param smoothingEnabled Whether to apply temporal smoothing to resize motion
@param smoothingDecayCoefficient Controls smoothing strength (higher = faster response, lower = smoother). Range: 1.0 (very smooth) to 50.0 (minimal smoothing) ```

## Signature

```kotlin
class IsdkPanelResize(enabled: Boolean = true, resizeMode: ResizeMode = ResizeMode.Simple, minDimensions: Vector2 = Vector2(0.3f, 0.3f), maxDimensions: Vector2 = Vector2(1.5f, 1.5f), preserveAspectRatio: Boolean = true, resizeSensitivity: Float = 1.0f, smoothingEnabled: Boolean = true, smoothingDecayCoefficient: Float = 15.0f, activeResizeCorner: ResizeCornerState = ResizeCornerState.NONE) : ComponentBase
```

## Constructors

| **IsdkPanelResize** ( enabled , resizeMode , minDimensions , maxDimensions , preserveAspectRatio , resizeSensitivity , smoothingEnabled , smoothingDecayCoefficient , activeResizeCorner ) | Signature ```kotlin constructor(enabled: Boolean = true, resizeMode: ResizeMode = ResizeMode.Simple, minDimensions: Vector2 = Vector2(0.3f, 0.3f), maxDimensions: Vector2 = Vector2(1.5f, 1.5f), preserveAspectRatio: Boolean = true, resizeSensitivity: Float = 1.0f, smoothingEnabled: Boolean = true, smoothingDecayCoefficient: Float = 15.0f, activeResizeCorner: ResizeCornerState = ResizeCornerState.NONE) ``` Parameters enabled: Boolean resizeMode: [ResizeMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_resizemode) minDimensions: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) maxDimensions: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) preserveAspectRatio: Boolean resizeSensitivity: Float smoothingEnabled: Boolean smoothingDecayCoefficient: Float activeResizeCorner: [ResizeCornerState](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_resizecornerstate) Returns [IsdkPanelResize](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdkpanelresize) |
| --- | --- |

## Properties

| **activeResizeCorner** : [ResizeCornerState](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_resizecornerstate) [Get][Set] | Indicates which corner is currently being used for resize, if any Signature ```kotlin var activeResizeCorner: ResizeCornerState ``` |
| --- | --- |
| **cachable** : BuildConfig.COMPONENTCACHE_LEVEL >= 1 [Get][Set] | Signature ```kotlin open override var cachable: BuildConfig.COMPONENTCACHE_LEVEL >= 1 ``` |
| **enabled** : Boolean [Get][Set] | Whether resize functionality is enabled Signature ```kotlin var enabled: Boolean ``` |
| **entID** : Long [Get][Set] | Signature ```kotlin var entID: Long ``` |
| **isDirty** : Boolean [Get][Set] | Signature ```kotlin var isDirty: Boolean ``` |
| **maxDimensions** : [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) [Get][Set] | Maximum panel dimensions (width, height) in meters Signature ```kotlin var maxDimensions: Vector2 ``` |
| **minDimensions** : [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) [Get][Set] | Minimum panel dimensions (width, height) in meters Signature ```kotlin var minDimensions: Vector2 ``` |
| **preserveAspectRatio** : Boolean [Get][Set] | Whether to maintain aspect ratio during resize Signature ```kotlin var preserveAspectRatio: Boolean ``` |
| **recycled** : Boolean [Get][Set] | Signature ```kotlin var recycled: Boolean ``` |
| **resizeMode** : [ResizeMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_resizemode) [Get][Set] | Mode of resizing: Simple (modifies scale), Relayout (adjusts dimensions and re-renders UI), or None (custom logic) Signature ```kotlin var resizeMode: ResizeMode ``` |
| **resizeSensitivity** : Float [Get][Set] | Sensitivity multiplier for resize drag movement (higher = more sensitive) Signature ```kotlin var resizeSensitivity: Float ``` |
| **smoothingDecayCoefficient** : Float [Get][Set] | Controls smoothing strength: higher values = faster response (less smoothing), lower values = smoother motion (more lag). Recommended range: 1.0-50.0 Signature ```kotlin var smoothingDecayCoefficient: Float ``` |
| **smoothingEnabled** : Boolean [Get][Set] | Whether to apply temporal smoothing to resize motion (reduces jitter, adds slight lag) Signature ```kotlin var smoothingEnabled: Boolean ``` |
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

| **activeResizeCornerData** : [EnumAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_enumattributedata) [Get] | Signature ```kotlin val activeResizeCornerData: EnumAttributeData ``` |
| --- | --- |
| **activeResizeCornerId** [Get] | Signature ```kotlin val activeResizeCornerId: ``` |
| **attributeKeys_** : IntArray [Get] | Signature ```kotlin val attributeKeys_: IntArray ``` |
| **attributeTypeCounts_** : IntArray [Get] | Signature ```kotlin val attributeTypeCounts_: IntArray ``` |
| **attributeTypes_** : IntArray [Get] | Signature ```kotlin val attributeTypes_: IntArray ``` |
| **attrMetaData_** : Map [Get] | Signature ```kotlin val attrMetaData_: Map ``` |
| **createDefaultInstance** : Function0 [Get] | Signature ```kotlin open override val createDefaultInstance: () -> IsdkPanelResize ``` |
| **enabledData** : [BooleanAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_booleanattributedata) [Get] | Signature ```kotlin val enabledData: BooleanAttributeData ``` |
| **enabledId** [Get] | Signature ```kotlin val enabledId: ``` |
| **enumClassesMap_** : Map [Get] | Signature ```kotlin val enumClassesMap_: Map<Int, Class<out Enum<*>>> ``` |
| **id** [Get] | Signature ```kotlin open override val id: ``` |
| **keyStringToKeyIntMap_** : Map [Get] | Signature ```kotlin val keyStringToKeyIntMap_: Map<String, Int> ``` |
| **maxDimensionsData** : [Vector2AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2attributedata) [Get] | Signature ```kotlin val maxDimensionsData: Vector2AttributeData ``` |
| **maxDimensionsId** [Get] | Signature ```kotlin val maxDimensionsId: ``` |
| **minDimensionsData** : [Vector2AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2attributedata) [Get] | Signature ```kotlin val minDimensionsData: Vector2AttributeData ``` |
| **minDimensionsId** [Get] | Signature ```kotlin val minDimensionsId: ``` |
| **preserveAspectRatioData** : [BooleanAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_booleanattributedata) [Get] | Signature ```kotlin val preserveAspectRatioData: BooleanAttributeData ``` |
| **preserveAspectRatioId** [Get] | Signature ```kotlin val preserveAspectRatioId: ``` |
| **resizeModeData** : [EnumAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_enumattributedata) [Get] | Signature ```kotlin val resizeModeData: EnumAttributeData ``` |
| **resizeModeId** [Get] | Signature ```kotlin val resizeModeId: ``` |
| **resizeSensitivityData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val resizeSensitivityData: FloatAttributeData ``` |
| **resizeSensitivityId** [Get] | Signature ```kotlin val resizeSensitivityId: ``` |
| **smoothingDecayCoefficientData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val smoothingDecayCoefficientData: FloatAttributeData ``` |
| **smoothingDecayCoefficientId** [Get] | Signature ```kotlin val smoothingDecayCoefficientId: ``` |
| **smoothingEnabledData** : [BooleanAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_booleanattributedata) [Get] | Signature ```kotlin val smoothingEnabledData: BooleanAttributeData ``` |
| **smoothingEnabledId** [Get] | Signature ```kotlin val smoothingEnabledId: ``` |

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