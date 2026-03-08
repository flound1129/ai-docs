# RoundedBox Class

Extends
[ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase)
*Modifiers:
final*

Defines the dimensions of a box shape with rounded edges by specifying the relative offset of two opposite corners and a Vector3 of radii to modify the roundedness of the edges. This is to be used with the `mesh://roundedbox` URI on [Mesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mesh) component. Material can be customized with the [Material](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_material) component.

Rounded boxes are useful for creating more visually appealing and ergonomic 3D objects than standard boxes.

Example:

```kotlin Entity.create(
    listOf(
        Mesh(RoundedBox.URI),
        RoundedBox(
            Vector3(-0.25f, -0.25f, -0.25f), // Min corner
            Vector3(0.25f, 0.25f, 0.25f),    // Max corner
            Vector3(0.05f, 0.05f, 0.05f)     // Edge radii
        ),
        Material().apply {
          baseColor = Color4(red = 1.0f, green = 0.0f, blue = 1.0f, alpha = 1.0f)
        },
        Transform(Pose(Vector3(x = 0f, y = 1.0f, z = -1.0f)))
    )
) ```

## Signature

```kotlin
class RoundedBox(min: Vector3 = Vector3(0.0f, 0.0f, 0.0f), max: Vector3 = Vector3(1.0f, 1.0f, 1.0f), radius: Vector3 = Vector3(0.1f, 0.1f, 0.1f)) : ComponentBase
```

## Constructors

| **RoundedBox** ( min , max , radius ) | Signature ```kotlin constructor(min: Vector3 = Vector3(0.0f, 0.0f, 0.0f), max: Vector3 = Vector3(1.0f, 1.0f, 1.0f), radius: Vector3 = Vector3(0.1f, 0.1f, 0.1f)) ``` Parameters min: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The relative offset of the bottom corner in meters (furthest in the -x, -y, -z direction) max: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The relative offset of the top corner in meters (furthest in the +x, +y, +z direction) radius: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The radii of the rounded edges of the box in meters Returns [RoundedBox](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_roundedbox) |
| --- | --- |

## Properties

| **cachable** : BuildConfig.COMPONENTCACHE_LEVEL >= 1 [Get][Set] | Signature ```kotlin open override var cachable: BuildConfig.COMPONENTCACHE_LEVEL >= 1 ``` |
| --- | --- |
| **entID** : Long [Get][Set] | Signature ```kotlin var entID: Long ``` |
| **isDirty** : Boolean [Get][Set] | Signature ```kotlin var isDirty: Boolean ``` |
| **max** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get][Set] | The relative offset in meters of the top corner (furthest in the +x, +y, +z direction) of the box from the center Signature ```kotlin var max: Vector3 ``` |
| **min** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get][Set] | The relative offset in meters of the bottom corner (furthest in the -x, -y, -z direction) of the box from the center Signature ```kotlin var min: Vector3 ``` |
| **radius** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get][Set] | The radii in meters of the rounded edges of the box, where the radii corresponds to the edges along that plane. (i.e radius.x corresponds to the edges running along in the x axis) Signature ```kotlin var radius: Vector3 ``` |
| **recycled** : Boolean [Get][Set] | Signature ```kotlin var recycled: Boolean ``` |
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
| **createDefaultInstance** : Function0 [Get] | Signature ```kotlin open override val createDefaultInstance: () -> RoundedBox ``` |
| **enumClassesMap_** : Map [Get] | Signature ```kotlin val enumClassesMap_: Map<Int, Class<out Enum<*>>> ``` |
| **id** [Get] | Signature ```kotlin open override val id: ``` |
| **keyStringToKeyIntMap_** : Map [Get] | Signature ```kotlin val keyStringToKeyIntMap_: Map<String, Int> ``` |
| **maxData** : [Vector3AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3attributedata) [Get] | Signature ```kotlin val maxData: Vector3AttributeData ``` |
| **maxId** [Get] | Signature ```kotlin val maxId: ``` |
| **minData** : [Vector3AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3attributedata) [Get] | Signature ```kotlin val minData: Vector3AttributeData ``` |
| **minId** [Get] | Signature ```kotlin val minId: ``` |
| **radiusData** : [Vector3AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3attributedata) [Get] | Signature ```kotlin val radiusData: Vector3AttributeData ``` |
| **radiusId** [Get] | Signature ```kotlin val radiusId: ``` |
| **URI** : Uri [Get] | URI for the procedural rounded box mesh. Use with [Mesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mesh) component. Signature ```kotlin val URI: Uri ``` |

### Companion Object Functions

| **attributeKeys** () | Signature ```kotlin open override fun attributeKeys(): IntArray ``` Returns IntArray |
| --- | --- |
| **attributeMetaData** () | Returns Map |
| **attributeTypeCountAvailable** () | Signature ```kotlin open override fun attributeTypeCountAvailable(): Boolean ``` Returns Boolean |
| **attributeTypeCounts** () | Signature ```kotlin open override fun attributeTypeCounts(): IntArray ``` Returns IntArray |
| **attributeTypes** () | Signature ```kotlin open override fun attributeTypes(): IntArray ``` Returns IntArray |
| **dependents** () | Signature ```kotlin open override fun dependents(): IntArray ``` Returns IntArray |
| **enumClassesMap** () | Signature ```kotlin open override fun enumClassesMap(): Map<Int, Class<out Enum<*>>> ``` Returns Map |
| **keyStringToKeyIntMap** ( keyString ) | Signature ```kotlin open override fun keyStringToKeyIntMap(keyString: String): Int? ``` Parameters keyString: String Returns Int? |