# Controller Class

Extends
[ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase)
*Modifiers:
final*

Represents Controller Data and properties that can be used to facilitate input.

## Signature

```kotlin
class Controller(buttonState: Int = 0, changedButtons: Int = 0, isActive: Boolean = false, type: ControllerType = ControllerType.CONTROLLER, directTouchEnabled: Boolean = false, directTouchButtonState: Int = 0, laserEnabled: Boolean = true) : ComponentBase
```

## Constructors

| **Controller** ( buttonState , changedButtons , isActive , type , directTouchEnabled , directTouchButtonState , laserEnabled ) | Signature ```kotlin constructor(buttonState: Int = 0, changedButtons: Int = 0, isActive: Boolean = false, type: ControllerType = ControllerType.CONTROLLER, directTouchEnabled: Boolean = false, directTouchButtonState: Int = 0, laserEnabled: Boolean = true) ``` Parameters buttonState: Int The current state of the buttons being pressed represented by integer bits changedButtons: Int Which buttons (represented by integer bits) have been changed (pressed or unpressed) isActive: Boolean Whether the controller is active or not type: [ControllerType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_controllertype) What type of controller it is: 0->controller 1->hand directTouchEnabled: Boolean Whether direct touch is enabled or not directTouchButtonState: Int The state of the direct touch buttons laserEnabled: Boolean Whether the laser is enabled or not Returns [Controller](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_controller) |
| --- | --- |

## Properties

| **buttonState** : Int [Get][Set] | The current state of the buttons being pressed represented by integer bits Signature ```kotlin var buttonState: Int ``` |
| --- | --- |
| **cachable** : BuildConfig.COMPONENTCACHE_LEVEL >= 1 [Get][Set] | Signature ```kotlin open override var cachable: BuildConfig.COMPONENTCACHE_LEVEL >= 1 ``` |
| **changedButtons** : Int [Get][Set] | Which buttons (represented by integer bits) have been changed (pressed or unpressed since the last frame) Signature ```kotlin var changedButtons: Int ``` |
| **directTouchButtonState** : Int [Get][Set] | The state of the direct touch buttons Signature ```kotlin var directTouchButtonState: Int ``` |
| **directTouchEnabled** : Boolean [Get][Set] | Signature ```kotlin var directTouchEnabled: Boolean ``` |
| **entID** : Long [Get][Set] | Signature ```kotlin var entID: Long ``` |
| **isActive** : Boolean [Get][Set] | Signature ```kotlin var isActive: Boolean ``` |
| **isDirty** : Boolean [Get][Set] | Signature ```kotlin var isDirty: Boolean ``` |
| **laserEnabled** : Boolean [Get][Set] | Signature ```kotlin var laserEnabled: Boolean ``` |
| **recycled** : Boolean [Get][Set] | Signature ```kotlin var recycled: Boolean ``` |
| **timeStamp** : Long [Get][Set] | Signature ```kotlin var timeStamp: Long ``` |
| **type** : [ControllerType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_controllertype) [Get][Set] | What type of controller it is: 0->controller 1->hand 2->eye Signature ```kotlin var type: ControllerType ``` |

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
| **buttonStateData** : [IntAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_intattributedata) [Get] | Signature ```kotlin val buttonStateData: IntAttributeData ``` |
| **buttonStateId** [Get] | Signature ```kotlin val buttonStateId: ``` |
| **changedButtonsData** : [IntAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_intattributedata) [Get] | Signature ```kotlin val changedButtonsData: IntAttributeData ``` |
| **changedButtonsId** [Get] | Signature ```kotlin val changedButtonsId: ``` |
| **createDefaultInstance** : Function0 [Get] | Signature ```kotlin open override val createDefaultInstance: () -> Controller ``` |
| **directTouchButtonStateData** : [IntAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_intattributedata) [Get] | Signature ```kotlin val directTouchButtonStateData: IntAttributeData ``` |
| **directTouchButtonStateId** [Get] | Signature ```kotlin val directTouchButtonStateId: ``` |
| **directTouchEnabledData** : [BooleanAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_booleanattributedata) [Get] | Signature ```kotlin val directTouchEnabledData: BooleanAttributeData ``` |
| **directTouchEnabledId** [Get] | Signature ```kotlin val directTouchEnabledId: ``` |
| **enumClassesMap_** : Map [Get] | Signature ```kotlin val enumClassesMap_: Map<Int, Class<out Enum<*>>> ``` |
| **id** [Get] | Signature ```kotlin open override val id: ``` |
| **isActiveData** : [BooleanAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_booleanattributedata) [Get] | Signature ```kotlin val isActiveData: BooleanAttributeData ``` |
| **isActiveId** [Get] | Signature ```kotlin val isActiveId: ``` |
| **keyStringToKeyIntMap_** : Map [Get] | Signature ```kotlin val keyStringToKeyIntMap_: Map<String, Int> ``` |
| **laserEnabledData** : [BooleanAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_booleanattributedata) [Get] | Signature ```kotlin val laserEnabledData: BooleanAttributeData ``` |
| **laserEnabledId** [Get] | Signature ```kotlin val laserEnabledId: ``` |
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