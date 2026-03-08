# Material Class

Extends
[ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase)
*Modifiers:
final*

Material is a component that describes the material properties of an object. This component is only used to assign properties to procedural meshes such as those created with the [Mesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mesh) component. Meta Spatial SDK provides some basic preset materials with [FlatColorMaterials](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_flatcolormaterials) .

Example of procedural mesh box with material:

```kotlin Entity.create(
  listOf(
      Mesh(Uri.parse("mesh://box")),
      Material().apply {
        baseColor = Color4(red = 0.2f, green = 0.8f, blue = 0.4f, alpha = 1.0f)
      },
      Box(Vector3(0.25f)),
      Transform(Pose(Vector3(0.0f, 0.0f, 0.0f))),
  )) ```

Details about the properties can be found in the [Filament Materials Guide](https://google.github.io/filament/Materials.html)

## Signature

```kotlin
class Material(repeatU: Float = 1.0f, repeatV: Float = 1.0f, offsetU: Float = 0.0f, offsetV: Float = 0.0f, baseColor: Color4 = Color4(0.5f, 0.5f, 0.5f, 1.0f), metallicInternal: Float = 0.0f, roughnessInternal: Float = 0.3f, unlit: Boolean = false, alphaMode: Int = com.meta.spatial.runtime.AlphaMode.OPAQUE.ordinal, shader: String = "", baseTextureAndroidResourceId: Int = 0, baseTextureScale: Float = 1.0f) : ComponentBase
```

## Constructors

| **Material** ( repeatU , repeatV , offsetU , offsetV , baseColor , metallicInternal , roughnessInternal , unlit , alphaMode , shader , baseTextureAndroidResourceId , baseTextureScale ) | Signature ```kotlin constructor(repeatU: Float = 1.0f, repeatV: Float = 1.0f, offsetU: Float = 0.0f, offsetV: Float = 0.0f, baseColor: Color4 = Color4(0.5f, 0.5f, 0.5f, 1.0f), metallicInternal: Float = 0.0f, roughnessInternal: Float = 0.3f, unlit: Boolean = false, alphaMode: Int = com.meta.spatial.runtime.AlphaMode.OPAQUE.ordinal, shader: String = "", baseTextureAndroidResourceId: Int = 0, baseTextureScale: Float = 1.0f) ``` Parameters repeatU: Float repeatV: Float offsetU: Float offsetV: Float baseColor: [Color4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_color4) metallicInternal: Float roughnessInternal: Float unlit: Boolean alphaMode: Int shader: String baseTextureAndroidResourceId: Int baseTextureScale: Float Returns [Material](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_material) |
| --- | --- |

## Properties

| **alphaMode** : Int [Get][Set] | alpha mode of the material Signature ```kotlin var alphaMode: Int ``` |
| --- | --- |
| **baseColor** : [Color4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_color4) [Get][Set] | : base color of the material Signature ```kotlin var baseColor: Color4 ``` |
| **baseTextureAndroidResourceId** : Int [Get][Set] | base texture of the material Signature ```kotlin var baseTextureAndroidResourceId: Int ``` |
| **baseTextureScale** : Float [Get][Set] | scale factor for the base texture (1.0 = original size, 0.5 = half size) Signature ```kotlin var baseTextureScale: Float ``` |
| **cachable** : BuildConfig.COMPONENTCACHE_LEVEL >= 1 [Get][Set] | Signature ```kotlin open override var cachable: BuildConfig.COMPONENTCACHE_LEVEL >= 1 ``` |
| **entID** : Long [Get][Set] | Signature ```kotlin var entID: Long ``` |
| **isDirty** : Boolean [Get][Set] | Signature ```kotlin var isDirty: Boolean ``` |
| **metallic** : Float [Get][Set] | : metallic of the material Signature ```kotlin var metallic: Float ``` |
| **metallicInternal** : Float [Get][Set] | metallic of the material Signature ```kotlin var metallicInternal: Float ``` |
| **offsetU** : Float [Get][Set] | offset u of the material Signature ```kotlin var offsetU: Float ``` |
| **offsetV** : Float [Get][Set] | offset v of the material Signature ```kotlin var offsetV: Float ``` |
| **recycled** : Boolean [Get][Set] | Signature ```kotlin var recycled: Boolean ``` |
| **repeatU** : Float [Get][Set] | repeat u of the material Signature ```kotlin var repeatU: Float ``` |
| **repeatV** : Float [Get][Set] | repeat v of the material Signature ```kotlin var repeatV: Float ``` |
| **roughness** : Float [Get][Set] | : roughness of the material Signature ```kotlin var roughness: Float ``` |
| **roughnessInternal** : Float [Get][Set] | roughness of the material Signature ```kotlin var roughnessInternal: Float ``` |
| **shader** : String [Get][Set] | shader of the material Signature ```kotlin var shader: String ``` |
| **timeStamp** : Long [Get][Set] | Signature ```kotlin var timeStamp: Long ``` |
| **unlit** : Boolean [Get][Set] | whether the material is unlit Signature ```kotlin var unlit: Boolean ``` |

## Functions

| **companion** () | Gets the companion object for this component. The companion object provides metadata about the component. Signature ```kotlin open override fun companion(): ComponentCompanion ``` Returns [ComponentCompanion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentcompanion) The component's companion object Throws RuntimeException If the companion is not implemented |
| --- | --- |
| **generateSceneMaterial** ( entity , ctx ) | Signature ```kotlin fun generateSceneMaterial(entity: Entity, ctx: Context): SceneMaterial ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) ctx: Context Returns [SceneMaterial](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenematerial) |
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

| **alphaModeData** : [IntAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_intattributedata) [Get] | Signature ```kotlin val alphaModeData: IntAttributeData ``` |
| --- | --- |
| **alphaModeId** [Get] | Signature ```kotlin val alphaModeId: ``` |
| **attributeKeys_** : IntArray [Get] | Signature ```kotlin val attributeKeys_: IntArray ``` |
| **attributeTypeCounts_** : IntArray [Get] | Signature ```kotlin val attributeTypeCounts_: IntArray ``` |
| **attributeTypes_** : IntArray [Get] | Signature ```kotlin val attributeTypes_: IntArray ``` |
| **attrMetaData_** : Map [Get] | Signature ```kotlin val attrMetaData_: Map ``` |
| **baseColorData** : [Color4AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_color4attributedata) [Get] | Signature ```kotlin val baseColorData: Color4AttributeData ``` |
| **baseColorId** [Get] | Signature ```kotlin val baseColorId: ``` |
| **baseTextureAndroidResourceIdData** : [IntAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_intattributedata) [Get] | Signature ```kotlin val baseTextureAndroidResourceIdData: IntAttributeData ``` |
| **baseTextureAndroidResourceIdId** [Get] | Signature ```kotlin val baseTextureAndroidResourceIdId: ``` |
| **baseTextureScaleData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val baseTextureScaleData: FloatAttributeData ``` |
| **baseTextureScaleId** [Get] | Signature ```kotlin val baseTextureScaleId: ``` |
| **createDefaultInstance** : Function0 [Get] | Signature ```kotlin open override val createDefaultInstance: () -> Material ``` |
| **enumClassesMap_** : Map [Get] | Signature ```kotlin val enumClassesMap_: Map<Int, Class<out Enum<*>>> ``` |
| **id** [Get] | Signature ```kotlin open override val id: ``` |
| **keyStringToKeyIntMap_** : Map [Get] | Signature ```kotlin val keyStringToKeyIntMap_: Map<String, Int> ``` |
| **metallicInternalData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val metallicInternalData: FloatAttributeData ``` |
| **metallicInternalId** [Get] | Signature ```kotlin val metallicInternalId: ``` |
| **offsetUData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val offsetUData: FloatAttributeData ``` |
| **offsetUId** [Get] | Signature ```kotlin val offsetUId: ``` |
| **offsetVData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val offsetVData: FloatAttributeData ``` |
| **offsetVId** [Get] | Signature ```kotlin val offsetVId: ``` |
| **repeatUData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val repeatUData: FloatAttributeData ``` |
| **repeatUId** [Get] | Signature ```kotlin val repeatUId: ``` |
| **repeatVData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val repeatVData: FloatAttributeData ``` |
| **repeatVId** [Get] | Signature ```kotlin val repeatVId: ``` |
| **roughnessInternalData** : [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) [Get] | Signature ```kotlin val roughnessInternalData: FloatAttributeData ``` |
| **roughnessInternalId** [Get] | Signature ```kotlin val roughnessInternalId: ``` |
| **shaderData** : [StringAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_stringattributedata) [Get] | Signature ```kotlin val shaderData: StringAttributeData ``` |
| **shaderId** [Get] | Signature ```kotlin val shaderId: ``` |
| **unlitData** : [BooleanAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_booleanattributedata) [Get] | Signature ```kotlin val unlitData: BooleanAttributeData ``` |
| **unlitId** [Get] | Signature ```kotlin val unlitId: ``` |

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
| **registerSceneTexture** ( key , texture ) | Registers a SceneTexture in the material cache with a custom key. This allows apps to insert dynamic or pre-processed textures (such as rendered text, converted ShapeDrawables, or procedurally generated images) into the cache so they can be used with the Material component via [Material.baseTextureAndroidResourceId](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_material#basetextureandroidresourceid) . The key should be a unique identifier, typically an Android resource ID or a unique hash. When [Material.generateSceneMaterial](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_material#generatescenematerial) is called with a matching [Material.baseTextureAndroidResourceId](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_material#basetextureandroidresourceid) , it will find the texture in this cache. Example: ```kotlin val bitmap = renderTextToBitmap("Hello World") val texture = SceneTexture(bitmap) Material.registerSceneTexture(myUniqueId, texture) Entity.create(listOf( Transform(Pose(position)), Mesh(Uri.parse("mesh://quad")), Quad(Vector2(-0.1f, -0.025f), Vector2(0.1f, 0.025f)), Material().apply { baseTextureAndroidResourceId = myUniqueId } )) ``` Signature ```kotlin fun registerSceneTexture(key: Int, texture: SceneTexture) ``` Parameters key: Int The unique key for the texture (e.g., resource ID or unique hash) texture: [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) The SceneTexture to register |