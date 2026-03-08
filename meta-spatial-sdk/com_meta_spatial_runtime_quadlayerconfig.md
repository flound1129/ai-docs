# QuadLayerConfig Class

Extends
[LayerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layerconfig)
*Modifiers:
final*

Layer config for a flat, single-sided, rectangular surface

## Signature

```kotlin
class QuadLayerConfig(var alphaBlend: LayerAlphaBlend? = null, var colorScaleBias: LayerColorScaleBias? = null, var zIndex: Int = 0) : LayerConfig
```

## Constructors

| **QuadLayerConfig** ( alphaBlend , colorScaleBias , zIndex ) | Signature ```kotlin constructor(alphaBlend: LayerAlphaBlend? = null, colorScaleBias: LayerColorScaleBias? = null, zIndex: Int = 0) ``` Parameters alphaBlend: [LayerAlphaBlend?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layeralphablend) colorScaleBias: [LayerColorScaleBias?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layercolorscalebias) zIndex: Int Returns [QuadLayerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_quadlayerconfig) |
| --- | --- |

## Properties

| **alphaBlend** : [LayerAlphaBlend?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layeralphablend) [Get][Set] | Configuration for alpha blending, or null to use default blending Signature ```kotlin var alphaBlend: LayerAlphaBlend? ``` |
| --- | --- |
| **colorScaleBias** : [LayerColorScaleBias?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layercolorscalebias) [Get][Set] | Color adjustment settings, or null to use default colors Signature ```kotlin var colorScaleBias: LayerColorScaleBias? ``` |
| **filters** : Int [Get][Set] | Signature ```kotlin var filters: Int ``` |
| **secure** : Boolean [Get][Set] | Whether the layer should be rendered securely to enable DRM. Signature ```kotlin var secure: Boolean ``` |
| **zIndex** : Int [Get][Set] | Integer value controlling the rendering order (higher values render on top). Layers of the same z-index are rendered based on the distance of entity origin from head pose. Signature ```kotlin var zIndex: Int ``` |