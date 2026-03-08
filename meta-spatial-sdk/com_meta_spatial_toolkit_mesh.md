# Mesh Class

Extends
[ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase)
*Modifiers:
final*

Mesh component, used to specify a mesh to be rendered. This component is used to specify the mesh uri, hittable, default shader override, and default scene override.

The Mesh component can point to any glb in the app's assets folder, on device, or over network. URIs pointing to on-device assets should be of the form "file://replace_with_path". The [NetworkedAssetLoader](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_networkedassetloader) should be initialized when downloading assets over network.

```kotlin Entity.create(listOf(Mesh(Uri.parse("environment.glb")), SupportsLocomotion(), Transform())) // From assets folder
Entity.create(listOf(Mesh(Uri.parse("https://github.com/KhronosGroup/glTF-Sample-Models/raw/refs/heads/main/2.0/Duck/glTF-Binary/Duck.glb)), Transform())) // From network ```

Special URIs are supported for procedural meshes:

```kotlin Mesh(Plane.URI) // creates a flat plane (requires Plane component)
Mesh(Sphere.URI) // creates a sphere (requires Sphere component)
Mesh(Box.URI) // creates a cube (requires Box component)
Mesh(RoundedBox.URI) // creates a rounded cube (requires RoundedBox component)
Mesh(Dome.URI) // creates a half-sphere (requires Dome component)
Mesh(Mesh.AXIS_URI) // creates an axis for debugging
Mesh(Mesh.SKYBOX_URI) // creates a skybox
Mesh(Quad.URI) // creates a quad (requires Quad component) ```

The [Plane](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_plane) , [Sphere](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_sphere) , [Box](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_box) , [RoundedBox](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_roundedbox) , [Dome](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_dome) , and [Quad](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_quad) components are provided to customize the dimensions of the procedural meshes. The [Material](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_material) component can be used to customize the material of the procedural meshes.

## Constructors

| **Mesh** ( mesh , hittable , defaultShaderOverride , defaultSceneOverride ) | Signature ```kotlin constructor(mesh: Uri, hittable: MeshCollision = MeshCollision.LineTest, defaultShaderOverride: String = "", defaultSceneOverride: Int = 0) ``` Parameters mesh: Uri : Uri of the mesh to be rendered hittable: [MeshCollision](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_meshcollision) : MeshCollision type, used to determine how a mesh is hit tested defaultShaderOverride: String : String of the default shader to be used for the mesh defaultSceneOverride: Int : Int of the default scene to be used for the mesh Returns [Mesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mesh) |
| --- | --- |

## Properties

| **cachable** : BuildConfig.COMPONENTCACHE_LEVEL >= 1 [Get][Set] | Signature ```kotlin open override var cachable: BuildConfig.COMPONENTCACHE_LEVEL >= 1 ``` |
| --- | --- |
| **defaultSceneOverride** : Int [Get][Set] | Int of the default scene to be used for the mesh Signature ```kotlin var defaultSceneOverride: Int ``` |
| **defaultShaderOverride** : String [Get][Set] | String of the default shader to be used for the mesh Signature ```kotlin var defaultShaderOverride: String ``` |
| **entID** : Long [Get][Set] | Signature ```kotlin var entID: Long ``` |
| **hittable** : [MeshCollision](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_meshcollision) [Get][Set] | The type of behavior the object can be hit using. Signature ```kotlin var hittable: MeshCollision ``` |
| **isDirty** : Boolean [Get][Set] | Signature ```kotlin var isDirty: Boolean ``` |
| **mesh** : Uri [Get][Set] | Uri of the mesh to be rendered Signature ```kotlin var mesh: Uri ``` |
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
| **AXIS_URI** : Uri [Get] | URI for the procedural axis mesh, useful for debugging and visualization. Signature ```kotlin val AXIS_URI: Uri ``` |
| **createDefaultInstance** : Function0 [Get] | Signature ```kotlin open override val createDefaultInstance: () -> Mesh ``` |
| **defaultSceneOverrideData** : [IntAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_intattributedata) [Get] | Signature ```kotlin val defaultSceneOverrideData: IntAttributeData ``` |
| **defaultSceneOverrideId** [Get] | Signature ```kotlin val defaultSceneOverrideId: ``` |
| **defaultShaderOverrideData** : [StringAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_stringattributedata) [Get] | Signature ```kotlin val defaultShaderOverrideData: StringAttributeData ``` |
| **defaultShaderOverrideId** [Get] | Signature ```kotlin val defaultShaderOverrideId: ``` |
| **enumClassesMap_** : Map [Get] | Signature ```kotlin val enumClassesMap_: Map<Int, Class<out Enum<*>>> ``` |
| **hittableData** : [EnumAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_enumattributedata) [Get] | Signature ```kotlin val hittableData: EnumAttributeData ``` |
| **hittableId** [Get] | Signature ```kotlin val hittableId: ``` |
| **id** [Get] | Signature ```kotlin open override val id: ``` |
| **keyStringToKeyIntMap_** : Map [Get] | Signature ```kotlin val keyStringToKeyIntMap_: Map<String, Int> ``` |
| **meshData** : [URIAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_uriattributedata) [Get] | Signature ```kotlin val meshData: URIAttributeData ``` |
| **meshId** [Get] | Signature ```kotlin val meshId: ``` |
| **SKYBOX_URI** : Uri [Get] | URI for the procedural skybox mesh with a default radius of ~1km. Signature ```kotlin val SKYBOX_URI: Uri ``` |

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