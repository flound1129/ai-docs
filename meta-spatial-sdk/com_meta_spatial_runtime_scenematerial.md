# SceneMaterial Class

*Modifiers:
final*

Represents a material used for rendering [SceneMesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenemesh) es. SceneMaterials are created from [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) s and can also be generated with custom shaders via SceneMaterial.custom().

SceneMaterial takes image content via [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) and opens up options to modify its display prior to rendering. This includes:

- [AlphaMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_alphamode) , which is how the renderer handles transparency. - Supplying a shader, default is SceneMaterial.PHYSICALLY_BASED_SHADER - If the default SceneMaterial.PHYSICALLY_BASED_SHADER is used, the inputs to the shader can be     modified with functions like SceneMaterial.setRoughness() - If a custom shader is used, the setAttribute() and setTexture() functions exist to update its     input.

Example usage: Use a Drawable from the resources directory. Scale the Material by a factor of 5 and adjust the roughness.

```kotlin SceneMaterial(SceneTexture(getDrawable(R.drawable.Grass))).apply {
             setRepeat(5f, 5f, 0f, 0f)
             setRoughness(0.7f)
            } ```

Example usage: Applying a custom shader named "grassShader" ("grassShader" must exist in shaders directory). Passes in a custom color and Texture to compute a shader.

```kotlin customMaterial =
  SceneMaterial.custom(
          "grassShader",
          arrayOf<SceneMaterialAttribute>(
              SceneMaterialAttribute("color", SceneMaterialDataType.Vector4),
              SceneMaterialAttribute("textureA", SceneMaterialDataType.Texture2D),
          ))
      .apply {
        setAttribute("color", Vector4(1f, 0f, 0f, 1f))
        setTexture("textureA", SceneTexture(getDrawable(R.drawable.Grass)))
      } ```

Learn more about custom shader materials [here](https://developers.meta.com/horizon/documentation/spatial-sdk/spatial-sdk-custom-shaders#custom-materials) .

## Signature

```kotlin
class SceneMaterial
```

## Constructors

| **SceneMaterial** ( texture , alphaMode , shader ) | Creates a material with the specified texture and alpha mode. Signature ```kotlin constructor(texture: SceneTexture, alphaMode: AlphaMode = AlphaMode.OPAQUE, shader: String = "") ``` Parameters texture: [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) The primary texture to use for this material alphaMode: [AlphaMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_alphamode) How transparency should be handled (default: OPAQUE) shader: String Optional path to a custom shader relative to your assets directory (default: empty string uses the default shader) Returns [SceneMaterial](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenematerial) |
| --- | --- |

## Properties

| **handle** : Long [Get] | Signature ```kotlin var handle: Long ``` |
| --- | --- |
| **params** : Array? [Get] | Signature ```kotlin var params: Array<SceneMaterialAttribute>? ``` |
| **texture** : [SceneTexture?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) [Get] | Signature ```kotlin var texture: SceneTexture? ``` |
| **textures** : HashMap<String, SceneTexture>() [Get] | Signature ```kotlin var textures: HashMap<String, SceneTexture>() ``` |

## Functions

| **destroy** () | Signature ```kotlin fun destroy() ``` |
| --- | --- |
| **getAttributeIndex** ( name ) | Gets the index of a named attribute in a custom shader. Signature ```kotlin fun getAttributeIndex(name: String): Int ``` Parameters name: String The name of the attribute Returns Int The index of the attribute, or -1 if not found |
| **setAlbedoColor** ( color ) | Sets the albedo (base color) for this material. Signature ```kotlin fun setAlbedoColor(color: Color) ``` Parameters color: Color The color to use as the albedo |
| **setAlbedoTexture** ( texture ) | Sets the primary albedo (base color) texture for this material. Signature ```kotlin fun setAlbedoTexture(texture: SceneTexture?) ``` Parameters texture: [SceneTexture?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) The texture to use as the albedo, or null to clear |
| **setAttribute** ( name , v ) | Sets a Vector4 attribute value by name for a custom shader. Signature ```kotlin fun setAttribute(name: String, v: Vector4) ``` Parameters name: String The name of the attribute v: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The Vector4 value to set |
| **setAttribute** ( name , v ) | Sets a texture attribute by name for a custom shader. Signature ```kotlin fun setAttribute(name: String, v: SceneTexture?) ``` Parameters name: String The name of the attribute v: [SceneTexture?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) The texture to set, or null to clear |
| **setAttribute** ( index , v ) | Sets a Vector4 attribute value by index for a custom shader. Signature ```kotlin fun setAttribute(index: Int, v: Vector4) ``` Parameters index: Int The index of the attribute v: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The Vector4 value to set |
| **setAttribute** ( index , v ) | Sets a texture attribute by index for a custom shader. Signature ```kotlin fun setAttribute(index: Int, v: SceneTexture?) ``` Parameters index: Int The index of the attribute v: [SceneTexture?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) The texture to set, or null to clear |
| **setBlendMode** ( blendMode ) | Sets the blend mode for this material. By default, custom materials are opaque. Signature ```kotlin fun setBlendMode(blendMode: BlendMode) ``` Parameters blendMode: [BlendMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_blendmode) The blend mode to use |
| **setColorWrite** ( mask ) | Sets which color channels should be written to the framebuffer. By default, a custom material writes all channels. Signature ```kotlin fun setColorWrite(mask: Int) ``` Parameters mask: Int Bit mask of color channels to write (R=1, G=2, B=4, A=8) |
| **setDepthTest** ( depthTest ) | Sets the depth testing function for this material. By default, faces aren't shaded if occluded by other geometry. Signature ```kotlin fun setDepthTest(depthTest: DepthTest) ``` Parameters depthTest: [DepthTest](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_depthtest) The depth test function to use |
| **setDepthWrite** ( depthWrite ) | Sets whether this material should write to the depth buffer. By default, custom materials write depth. Signature ```kotlin fun setDepthWrite(depthWrite: DepthWrite) ``` Parameters depthWrite: [DepthWrite](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_depthwrite) The depth write mode to use |
| **setMetalRoughness** ( roughness ) | Configures the material as metallic with the specified roughness for physically-based rendering. Signature ```kotlin fun setMetalRoughness(roughness: Float) ``` Parameters roughness: Float Surface roughness value (0.0 = smooth, 1.0 = rough) |
| **setRenderOrder** ( renderOrder ) | Sets a render order offset for this material, allowing fine-grained control over render ordering within the same sort order category. This value acts as an override to the sort order, providing additional control over the rendering sequence. Objects with higher render order values are rendered later. Signature ```kotlin fun setRenderOrder(renderOrder: Int) ``` Parameters renderOrder: Int The render order offset, valid range is -3 to +3 |
| **setRepeat** ( scaleX , scaleY , offsetX , offsetY ) | This controls how the texture is tiled and positioned on the surface. Signature ```kotlin fun setRepeat(scaleX: Float, scaleY: Float, offsetX: Float, offsetY: Float) ``` Parameters scaleX: Float Horizontal scaling factor for texture repetition scaleY: Float Vertical scaling factor for texture repetition offsetX: Float Horizontal offset for texture positioning offsetY: Float Vertical offset for texture positioning |
| **setRoughness** ( roughness ) | Configures the material as non-metallic with the specified roughness for physically-based rendering. Signature ```kotlin fun setRoughness(roughness: Float) ``` Parameters roughness: Float Surface roughness value (0.0 = smooth, 1.0 = rough) |
| **setRoughnessMetallicness** ( roughness , metallicness ) | Sets both roughness and metallicness properties for physically-based rendering. Signature ```kotlin fun setRoughnessMetallicness(roughness: Float, metallicness: Float) ``` Parameters roughness: Float Surface roughness value (0.0 = smooth, 1.0 = rough) metallicness: Float Surface metallicness value (0.0 = dielectric, 1.0 = metallic) |
| **setSidedness** ( sidedness ) | Sets whether faces should be rendered on one side, both sides, or neither. By default, only the front faces are rendered. Signature ```kotlin fun setSidedness(sidedness: MaterialSidedness) ``` Parameters sidedness: [MaterialSidedness](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_materialsidedness) The sidedness mode to use |
| **setSortOrder** ( sortOrder ) | Sets the render sort order for this material. By default, custom materials have opaque sort order. Signature ```kotlin fun setSortOrder(sortOrder: SortOrder) ``` Parameters sortOrder: [SortOrder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sortorder) The sort order to use |
| **setStereoMode** ( mode ) | Sets the stereo rendering mode for this material. This can allow you to display stereoscopic 3D media. Signature ```kotlin fun setStereoMode(mode: StereoMode) ``` Parameters mode: [StereoMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_stereomode) The stereo mode to use |
| **setTexture** ( binding , texture ) | Sets the texture for a named attribute in a custom shader. Signature ```kotlin fun setTexture(binding: String, texture: SceneTexture) ``` Parameters binding: String The name of the texture binding in the shader texture: [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) The texture to bind |
| **setUnlit** ( isUnlit ) | Sets whether this material should be rendered without lighting calculations. Unlit materials ignore scene lighting and are rendered with full brightness. For best performance, you can alternatively utilize the `SceneMaterial.UNLIT_SHADER` shader override. Signature ```kotlin fun setUnlit(isUnlit: Boolean) ``` Parameters isUnlit: Boolean True to disable lighting calculations, false to enable them |

## Companion Object

### Companion Object Properties

| **HOLE_PUNCH_PANEL_ALPHA_SHADER** : String [Get] | Hole punch shader which does not feather the edge, and might have black lines on the edge. Used in conjunction with AlphaMode.MASKED_HOLE_PUNCH or AlphaBlendMode.TRANSLUCENT_HOLE_PUNCH Signature ```kotlin val HOLE_PUNCH_PANEL_ALPHA_SHADER: String ``` |
| --- | --- |
| **HOLE_PUNCH_PANEL_EDGE_SHADER** : String [Get] | Hole punch shader which detects and feathers the edges but not the alpha regions in the texture. Used in conjunction with AlphaMode.MASKED_HOLE_PUNCH or AlphaBlendMode.TRANSLUCENT_HOLE_PUNCH Signature ```kotlin val HOLE_PUNCH_PANEL_EDGE_SHADER: String ``` |
| **HOLE_PUNCH_PANEL_FEATHER_SHADER** : String [Get] | Hole punch shader which detects and feathers the edges and the alpha regions in the texture. Used in conjunction with AlphaMode.MASKED_HOLE_PUNCH or AlphaBlendMode.TRANSLUCENT_HOLE_PUNCH Signature ```kotlin val HOLE_PUNCH_PANEL_FEATHER_SHADER: String ``` |
| **HOLE_PUNCH_PANEL_SHADER** : String [Get] | Shader similar to HOLE_PUNCH_SHADER but instead factors in the transparency of the base color (panel). This shader will likely need to be used if you have transparency in your panel so we don't have to punch holes on the areas that are transparent. If you are setting this on your panel, you will likely need to use `forceSceneTexture = true` . Used in conjunction with AlphaMode.HOLE_PUNCH Signature ```kotlin val HOLE_PUNCH_PANEL_SHADER: String ``` |
| **HOLE_PUNCH_SHADER** : String [Get] | Hole punch shader to indiscriminately punch holes on the geometry. Hole punching is used to cut out space for layers to be rendered. Used in conjunction with AlphaMode.HOLE_PUNCH Signature ```kotlin val HOLE_PUNCH_SHADER: String ``` |
| **PHYSICALLY_BASED_SHADER** : String [Get] | Our default physically based renderer. This is complete with lighting and IBL. Has the highest graphical fidelity but is also the most compute intensive Signature ```kotlin val PHYSICALLY_BASED_SHADER: String ``` |
| **TEXTURED_UNLIT_SHADER** : String [Get] | Signature ```kotlin val TEXTURED_UNLIT_SHADER: String ``` |
| **UNLIT_SHADER** : String [Get] | Signature ```kotlin val UNLIT_SHADER: String ``` |

### Companion Object Functions

| **custom** ( shader , params , vertexLayout ) | Create a custom material with a custom shader and params. Learn more about how to create custom shader materials [here](https://developers.meta.com/horizon/documentation/spatial-sdk/spatial-sdk-custom-shaders#custom-materials) . Signature ```kotlin fun custom(shader: String, params: Array<SceneMaterialAttribute>, vertexLayout: VertexLayout = VertexLayout.COMPACT): SceneMaterial ``` Parameters shader: String The path to the shader to use. This is relative to the assets folder. params: Array The list of attributes (vec4 and textures) to use in the shader. They will be bound to the shader in the order in which they are passed in. vertexLayout: [VertexLayout](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_vertexlayout) The vertex layout to use. By default, we use the compact layout Returns [SceneMaterial](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenematerial) |
| --- | --- |
| **depthOnly** ( isPrePass ) | Creates a material that only writes to the depth buffer. Depth-only materials are useful for creating invisible geometry that still participates in depth testing, such as collision surfaces or occlusion volumes. Signature ```kotlin fun depthOnly(isPrePass: Boolean): SceneMaterial ``` Parameters isPrePass: Boolean Whether this material should be rendered in the pre-pass Returns [SceneMaterial](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenematerial) A new depth-only material |
| **passthrough** () | Creates a material for rendering passthrough content. Passthrough materials allow the real world to be visible through virtual content, which is essential for mixed reality applications. Signature ```kotlin fun passthrough(): SceneMaterial ``` Returns [SceneMaterial](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenematerial) A new passthrough material |