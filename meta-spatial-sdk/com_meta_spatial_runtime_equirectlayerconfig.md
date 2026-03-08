# EquirectLayerConfig Class

Extends
[LayerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layerconfig)
*Modifiers:
final*

Layer config for a single-sided, surface projected on the inside of a sphere

## Signature

```kotlin
class EquirectLayerConfig(var radius: Float, var centralHorizontalAngle: Float = (2.0 * Math.PI).toFloat(), var upperVerticalAngle: Float = (Math.PI / 2).toFloat(), var lowerVerticalAngle: Float = -(Math.PI / 2).toFloat(), var alphaBlend: LayerAlphaBlend? = null, var colorScaleBias: LayerColorScaleBias? = null, var zIndex: Int = 0) : LayerConfig
```

## Constructors

| **EquirectLayerConfig** ( radius , centralHorizontalAngle , upperVerticalAngle , lowerVerticalAngle , alphaBlend , colorScaleBias , zIndex ) | Signature ```kotlin constructor(radius: Float, centralHorizontalAngle: Float = (2.0 * Math.PI).toFloat(), upperVerticalAngle: Float = (Math.PI / 2).toFloat(), lowerVerticalAngle: Float = -(Math.PI / 2).toFloat(), alphaBlend: LayerAlphaBlend? = null, colorScaleBias: LayerColorScaleBias? = null, zIndex: Int = 0) ``` Parameters radius: Float centralHorizontalAngle: Float upperVerticalAngle: Float lowerVerticalAngle: Float alphaBlend: [LayerAlphaBlend?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layeralphablend) colorScaleBias: [LayerColorScaleBias?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layercolorscalebias) zIndex: Int Returns [EquirectLayerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_equirectlayerconfig) |
| --- | --- |

## Properties

| **alphaBlend** : [LayerAlphaBlend?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layeralphablend) [Get][Set] | Configuration for alpha blending, or null to use default blending Signature ```kotlin var alphaBlend: LayerAlphaBlend? ``` |
| --- | --- |
| **centralHorizontalAngle** : Float [Get][Set] | Signature ```kotlin var centralHorizontalAngle: Float ``` |
| **colorScaleBias** : [LayerColorScaleBias?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layercolorscalebias) [Get][Set] | Color adjustment settings, or null to use default colors Signature ```kotlin var colorScaleBias: LayerColorScaleBias? ``` |
| **filters** : Int [Get][Set] | Signature ```kotlin var filters: Int ``` |
| **lowerVerticalAngle** : Float [Get][Set] | Signature ```kotlin var lowerVerticalAngle: Float ``` |
| **radius** : Float [Get][Set] | Signature ```kotlin var radius: Float ``` |
| **secure** : Boolean [Get][Set] | Whether the layer should be rendered securely to enable DRM. Signature ```kotlin var secure: Boolean ``` |
| **upperVerticalAngle** : Float [Get][Set] | Signature ```kotlin var upperVerticalAngle: Float ``` |
| **zIndex** : Int [Get][Set] | Integer value controlling the rendering order (higher values render on top). Layers of the same z-index are rendered based on the distance of entity origin from head pose. Signature ```kotlin var zIndex: Int ``` |