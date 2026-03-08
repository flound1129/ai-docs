# PanelRenderMode Class

Sealed class defining how the panel will render in the scene.

## Signature

```kotlin
sealed class PanelRenderMode
```

## Inner Classes

### Mesh Class

Extends
[PanelRenderMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelrendermode)
*Modifiers:
final*

Use a simple mesh-based panel. This is not a good option for panels with text or complex UI as it will appear low-resolution.

Signature
```kotlin
class Mesh : PanelRenderMode
```

Constructors
| **Mesh** () | Signature ```kotlin constructor() ``` Returns PanelRenderMode.Mesh |
| --- | --- |

### Layer Class

Extends
[PanelRenderMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelrendermode)
*Modifiers:
final*

Layers enable sharp, crisp panels that look great to the user. This is the recommended approach for most panels as the benefits outweigh the costs.

Signature
```kotlin
data class Layer(val layerBlendType: PanelShapeLayerBlendType = PanelShapeLayerBlendType.MASKED, val enableLayerFeatheredEdge: Boolean = false, val filters: Int? = null) : PanelRenderMode
```

Constructors
| **Layer** ( layerBlendType , enableLayerFeatheredEdge , filters ) | Signature ```kotlin constructor(layerBlendType: PanelShapeLayerBlendType = PanelShapeLayerBlendType.MASKED, enableLayerFeatheredEdge: Boolean = false, filters: Int? = null) ``` Parameters layerBlendType: [PanelShapeLayerBlendType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelshapelayerblendtype) This parameter determins the type of blending applied to the layer. OPAQUE: Every pixel of the panel is rendered to the screen, and the alpha value of the underlying texture is ignored. MASKED: The default type, where each sample is either rendered or discarded based on the alpha value of the panel. ALPHA_BLEND: The alpha is blended accurately, resulting in higher quality edges. However, it is slower and can result in blending artifacts when overlapping with semitransparent meshes. enableLayerFeatheredEdge: Boolean If true, it uses a special shader that feathers the edges of the panel, as well as edges around the alpha edges in the texture. It slightly shrinks the size of the panel and works best when the layerBlendType is set to ALPHA_BLEND. filters: Int? Optional layer filters using LayerFilters constants. If null, uses the LayerConfig default filtering. In most cases supplying DEFAULT_QUALITY or HIGHEST_QUALITY should be sufficient. For more fine-grained control you can combine filters with bitwise OR operations. Returns PanelRenderMode.Layer |
| --- | --- |

Properties
| **enableLayerFeatheredEdge** : Boolean [Get] | If true, it uses a special shader that feathers the edges of the panel, as well as edges around the alpha edges in the texture. It slightly shrinks the size of the panel and works best when the layerBlendType is set to ALPHA_BLEND. Signature ```kotlin val enableLayerFeatheredEdge: Boolean = false ``` |
| --- | --- |
| **filters** : Int? [Get] | Optional layer filters using LayerFilters constants. If null, uses the LayerConfig default filtering. In most cases supplying DEFAULT_QUALITY or HIGHEST_QUALITY should be sufficient. For more fine-grained control you can combine filters with bitwise OR operations. Signature ```kotlin val filters: Int? = null ``` |
| **layerBlendType** : [PanelShapeLayerBlendType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelshapelayerblendtype) [Get] | This parameter determins the type of blending applied to the layer. OPAQUE: Every pixel of the panel is rendered to the screen, and the alpha value of the underlying texture is ignored. MASKED: The default type, where each sample is either rendered or discarded based on the alpha value of the panel. ALPHA_BLEND: The alpha is blended accurately, resulting in higher quality edges. However, it is slower and can result in blending artifacts when overlapping with semitransparent meshes. Signature ```kotlin val layerBlendType: PanelShapeLayerBlendType ``` |