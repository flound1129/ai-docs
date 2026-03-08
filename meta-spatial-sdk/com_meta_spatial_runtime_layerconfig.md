# LayerConfig Class

*Modifiers:
open*

Configuration options for rendering layers. Setting this in PanelConfig will enable Layers.

Layers are used to render Panels with higher fidelity. More information can be found [here](https://developers.meta.com/horizon/documentation/spatial-sdk/spatial-sdk-2dpanel-layers) .

## Signature

```kotlin
open class LayerConfig(var alphaBlend: LayerAlphaBlend? = null, var colorScaleBias: LayerColorScaleBias? = null, var zIndex: Int = 0, var secure: Boolean = false, var filters: Int = 0)
```

## Constructors

| **LayerConfig** ( alphaBlend , colorScaleBias , zIndex , secure , filters ) | Signature ```kotlin constructor(alphaBlend: LayerAlphaBlend? = null, colorScaleBias: LayerColorScaleBias? = null, zIndex: Int = 0, secure: Boolean = false, filters: Int = 0) ``` Parameters alphaBlend: [LayerAlphaBlend?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layeralphablend) Configuration for alpha blending, or null to use default blending colorScaleBias: [LayerColorScaleBias?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layercolorscalebias) Color adjustment settings, or null to use default colors zIndex: Int Integer value controlling the rendering order (higher values render on top). Layers of the same z-index are rendered based on the distance of entity origin from head pose. secure: Boolean Whether the layer should be rendered securely to enable DRM. filters: Int Returns [LayerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layerconfig) |
| --- | --- |

## Properties

| **alphaBlend** : [LayerAlphaBlend?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layeralphablend) [Get][Set] | Configuration for alpha blending, or null to use default blending Signature ```kotlin var alphaBlend: LayerAlphaBlend? ``` |
| --- | --- |
| **colorScaleBias** : [LayerColorScaleBias?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layercolorscalebias) [Get][Set] | Color adjustment settings, or null to use default colors Signature ```kotlin var colorScaleBias: LayerColorScaleBias? ``` |
| **filters** : Int [Get][Set] | Signature ```kotlin var filters: Int ``` |
| **secure** : Boolean [Get][Set] | Whether the layer should be rendered securely to enable DRM. Signature ```kotlin var secure: Boolean ``` |
| **zIndex** : Int [Get][Set] | Integer value controlling the rendering order (higher values render on top). Layers of the same z-index are rendered based on the distance of entity origin from head pose. Signature ```kotlin var zIndex: Int ``` |