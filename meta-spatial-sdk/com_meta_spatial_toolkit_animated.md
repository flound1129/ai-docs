# Animated Class

Extends
[ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase)
*Modifiers:
final*

The animated component is used to play animations for a glTF asset. It also configures different settings for animation playback. It allows the selection of different playback types, states, and different animation tracks if applicable.

## Signature

```kotlin
class Animated(startTime: Long = -1L, pausedTime: Float = 0.0f, playbackState: PlaybackState = PlaybackState.PLAYING, playbackType: PlaybackType = PlaybackType.LOOP, track: Int = 0, animationName: String = "") : ComponentBase
```

## Constructors

| **Animated** ( startTime , pausedTime , playbackState , playbackType , track , animationName ) | Signature ```kotlin constructor(startTime: Long = -1L, pausedTime: Float = 0.0f, playbackState: PlaybackState = PlaybackState.PLAYING, playbackType: PlaybackType = PlaybackType.LOOP, track: Int = 0, animationName: String = "") ``` Parameters startTime: Long World time at which animation started (ms since epoch) pausedTime: Float Paused location/time (sec) within animation track playbackState: [PlaybackState](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_playbackstate) State of the animation (playing or paused) playbackType: [PlaybackType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_playbacktype) The type of animation playback to be used track: Int which animation track of the glTF to play animationName: String Returns [Animated](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_animated) |
| --- | --- |

## Properties

| **animationName** : String [Get][Set] | Name of the animation track in the glTF to play (takes precedence over track ID if set) Signature ```kotlin var animationName: String ``` |
| --- | --- |
| **cachable** : BuildConfig.COMPONENTCACHE_LEVEL >= 1 [Get][Set] | Signature ```kotlin open override var cachable: BuildConfig.COMPONENTCACHE_LEVEL >= 1 ``` |
| **entID** : Long [Get][Set] | Signature ```kotlin var entID: Long ``` |
| **isDirty** : Boolean [Get][Set] | Signature ```kotlin var isDirty: Boolean ``` |
| **pausedTime** : Float [Get][Set] | Paused location/time (sec) within animation track Signature ```kotlin var pausedTime: Float ``` |
| **playbackState** : [PlaybackState](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_playbackstate) [Get][Set] | State of the animation (playing or paused) Signature ```kotlin var playbackState: PlaybackState ``` |
| **playbackType** : [PlaybackType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_playbacktype) [Get][Set] | The type of animation playback to be used Signature ```kotlin var playbackType: PlaybackType ``` |
| **recycled** : Boolean [Get][Set] | Signature ```kotlin var recycled: Boolean ``` |
| **startTime** : Long [Get][Set] | World time at which animation started (ms since epoch) Signature ```kotlin var startTime: Long ``` |
| **timeStamp** : Long [Get][Set] | Signature ```kotlin var timeStamp: Long ``` |
| **track** : Int [Get][Set] | which animation track of the glTF to play (used when animationName is not set) Signature ```kotlin var track: Int ``` |

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

| **animationNameData** : [StringAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_stringattributedata) [Get] | Signature ```kotlin val animationNameData: StringAttributeData ``` |
| --- | --- |
| **animationNameId** [Get] | Signature ```kotlin val animationNameId: ``` |
| **attributeKeys_** : IntArray [Get] | Signature ```kotlin val attributeKeys_: IntArray ``` |
| **attributeTypeCounts_** : IntArray [Get] | Signature ```kotlin val attributeTypeCounts_: IntArray ``` |
| **attributeTypes_** : IntArray [Get] | Signature ```kotlin val attributeTypes_: IntArray ``` |
| **attrMetaData_** : Map [Get] | Signature ```kotlin val attrMetaData_: Map ``` |
| **createDefaultInstance** : Function0 [Get] | Signature ```kotlin open override val createDefaultInstance: () -> Animated ``` |
| **enumClassesMap_** : Map [Get] | Signature ```kotlin val enumClassesMap_: Map<Int, Class<out Enum<*>>> ``` |
| **id** [Get] | Signature ```kotlin open override val id: ``` |
| **keyStringToKeyIntMap_** : Map [Get] | Signature ```kotlin val keyStringToKeyIntMap_: Map<String, Int> ``` |
| **pausedTimeData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val pausedTimeData: FloatAttributeData ``` |
| **pausedTimeId** [Get] | Signature ```kotlin val pausedTimeId: ``` |
| **playbackStateData** : [EnumAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_enumattributedata) [Get] | Signature ```kotlin val playbackStateData: EnumAttributeData ``` |
| **playbackStateId** [Get] | Signature ```kotlin val playbackStateId: ``` |
| **playbackTypeData** : [EnumAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_enumattributedata) [Get] | Signature ```kotlin val playbackTypeData: EnumAttributeData ``` |
| **playbackTypeId** [Get] | Signature ```kotlin val playbackTypeId: ``` |
| **startTimeData** : [LongAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_longattributedata) [Get] | Signature ```kotlin val startTimeData: LongAttributeData ``` |
| **startTimeId** [Get] | Signature ```kotlin val startTimeId: ``` |
| **trackData** : [IntAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_intattributedata) [Get] | Signature ```kotlin val trackData: IntAttributeData ``` |
| **trackId** [Get] | Signature ```kotlin val trackId: ``` |

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