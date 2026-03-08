# LayerAlphaBlend Class

*Modifiers:
final*

Defines the coefficients of how to blend the layer (using an add operation). "Source" refers to the layer you are currently compositing and "destination" refers to whatever is already in the buffer. This compositing can be modeled by:

finalColor = (sourceColor * sourceFactorColor) + (destinationColor * destinationFactorColor) finalAlpha = (sourceAlpha * sourceFactorAlpha) + (destinationAlpha * destinationFactorAlpha)

## Signature

```kotlin
data class LayerAlphaBlend(val sourceFactorColor: BlendFactor, val destinationFactorColor: BlendFactor, val sourceFactorAlpha: BlendFactor, val destinationFactorAlpha: BlendFactor)
```

## Constructors

| **LayerAlphaBlend** ( sourceFactorColor , destinationFactorColor , sourceFactorAlpha , destinationFactorAlpha ) | Signature ```kotlin constructor(sourceFactorColor: BlendFactor, destinationFactorColor: BlendFactor, sourceFactorAlpha: BlendFactor, destinationFactorAlpha: BlendFactor) ``` Parameters sourceFactorColor: [BlendFactor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_blendfactor) destinationFactorColor: [BlendFactor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_blendfactor) sourceFactorAlpha: [BlendFactor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_blendfactor) destinationFactorAlpha: [BlendFactor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_blendfactor) Returns [LayerAlphaBlend](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_layeralphablend) |
| --- | --- |

## Properties

| **destinationFactorAlpha** : [BlendFactor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_blendfactor) [Get] | Signature ```kotlin val destinationFactorAlpha: BlendFactor ``` |
| --- | --- |
| **destinationFactorColor** : [BlendFactor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_blendfactor) [Get] | Signature ```kotlin val destinationFactorColor: BlendFactor ``` |
| **sourceFactorAlpha** : [BlendFactor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_blendfactor) [Get] | Signature ```kotlin val sourceFactorAlpha: BlendFactor ``` |
| **sourceFactorColor** : [BlendFactor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_blendfactor) [Get] | Signature ```kotlin val sourceFactorColor: BlendFactor ``` |