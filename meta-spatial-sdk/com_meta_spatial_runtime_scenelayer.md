# SceneLayer Class

*Modifiers:
abstract*

Base class for creating a Layer in the Scene.

## Signature

```kotlin
abstract class SceneLayer(scene_: Scene, id_: Int)
```

## Constructors

| **SceneLayer** ( scene_ , id_ ) | Signature ```kotlin constructor(scene_: Scene, id_: Int) ``` Parameters scene_: [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that owns this layer id_: Int The unique identifier for this layer Returns [SceneLayer](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenelayer) |
| --- | --- |

## Functions

| **destroy** () | Signature ```kotlin fun destroy() ``` |
| --- | --- |
| **setAlphaBlend** ( layerAlphaBlend ) | Sets the alpha blending mode for this layer. This controls how the layer blends with content behind it. Signature ```kotlin fun setAlphaBlend(layerAlphaBlend: LayerAlphaBlend) ``` Parameters layerAlphaBlend: [LayerAlphaBlend](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layeralphablend) The alpha blending configuration to use |
| **setClip** ( minUV , maxUV , minRightUV , maxRightUV ) | Sets the UV clip region for this layer's swapchain texture. This allows showing only a portion of the texture, or showing different portions for each eye in stereo rendering. Signature ```kotlin fun setClip(minUV: Vector2, maxUV: Vector2, minRightUV: Vector2 = minUV, maxRightUV: Vector2 = maxUV) ``` Parameters minUV: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The minimum UV coordinates for the left eye (or both eyes if mono) maxUV: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The maximum UV coordinates for the left eye (or both eyes if mono) minRightUV: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The minimum UV coordinates for the right eye (defaults to minUV) maxRightUV: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The maximum UV coordinates for the right eye (defaults to maxUV) |
| **setColorScaleBias** ( scale , bias ) | Sets the color scale and bias for this layer. This allows for color adjustment using the formula: output = input * scale + bias Signature ```kotlin fun setColorScaleBias(scale: Vector4, bias: Vector4) ``` Parameters scale: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The scale factor for each color channel (r, g, b, a) bias: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The bias value for each color channel (r, g, b, a) |
| **setFilters** ( filters ) | Signature ```kotlin fun setFilters(filters: Int) ``` Parameters filters: Int |
| **setScale** ( scale ) | Sets the scale of this layer. Signature ```kotlin fun setScale(scale: Vector3) ``` Parameters scale: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The scale vector to apply (x, y, z) |
| **setSecure** ( secure ) | Sets whether this layer should be secure. When a layer is secure, its content cannot be captured or copied by other applications. Needs to be enabled to play DRM protected content. Signature ```kotlin fun setSecure(secure: Boolean) ``` Parameters secure: Boolean Whether the layer should be secure |
| **setZIndex** ( zIndex ) | Sets the Z-index of this layer, controlling its rendering order. Layers with higher Z-index values are rendered on top of layers with lower values. When layers have the same Z-index, they are sorted by distance to the viewer. Signature ```kotlin fun setZIndex(zIndex: Int) ``` Parameters zIndex: Int The Z-index value (default is 0) |