# LayerColorScaleBias Class

*Modifiers:
final*

Controls color adjustment for rendering layers.

LayerColorScaleBias provides a way to adjust the color output of a layer by applying scale and bias transformations to the RGBA color channels. This allows for effects like tinting, brightness adjustment, contrast modification, and transparency control.

The color transformation is applied using the formula: `finalColor = (sourceColor * scale) + bias`

Example usage:

```kotlin // Create a layer config with 50% opacity
val halfTransparent = LayerColorScaleBias(
    scale = Vector4(1.0f, 1.0f, 1.0f, 0.5f),  // Keep RGB the same, reduce alpha to 50%
    bias = Vector4(0.0f, 0.0f, 0.0f, 0.0f)    // No bias
)
// Create a layer config with a blue tint
val blueTint = LayerColorScaleBias(
    scale = Vector4(0.8f, 0.8f, 1.0f, 1.0f),  // Reduce red and green, keep blue and alpha
    bias = Vector4(0.0f, 0.0f, 0.2f, 0.0f)    // Add some blue
) ```

## Signature

```kotlin
class LayerColorScaleBias(var scale: Vector4, var bias: Vector4)
```

## Constructors

| **LayerColorScaleBias** ( scale , bias ) | Signature ```kotlin constructor(scale: Vector4, bias: Vector4) ``` Parameters scale: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) Vector4 containing RGBA scale factors to multiply with the source color bias: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) Vector4 containing RGBA bias values to add to the scaled color Returns [LayerColorScaleBias](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layercolorscalebias) |
| --- | --- |

## Properties

| **bias** : [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) [Get][Set] | Vector4 containing RGBA bias values to add to the scaled color Signature ```kotlin var bias: Vector4 ``` |
| --- | --- |
| **scale** : [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) [Get][Set] | Vector4 containing RGBA scale factors to multiply with the source color Signature ```kotlin var scale: Vector4 ``` |