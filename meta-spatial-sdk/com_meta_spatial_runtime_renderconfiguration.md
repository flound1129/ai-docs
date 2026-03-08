# RenderConfiguration Class

*Modifiers:
final*

Controls the render resolution scaling for the app. Set in AppSystemActivity.renderConfiguration().

Example:

```kotlin class ImmersiveActivity : AppSystemActivity() {
   override fun renderConfiguration(): RenderConfiguration {
     return RenderConfiguration(0.95f) // Slightly lower visual quality for better performance.
   }
   ...
} ```

## Signature

```kotlin
data class RenderConfiguration(val suggestRenderSizeScale: Float = 1.0f)
```

## Constructors

| **RenderConfiguration** ( suggestRenderSizeScale ) | Signature ```kotlin constructor(suggestRenderSizeScale: Float = 1.0f) ``` Parameters suggestRenderSizeScale: Float The scaling factor for render resolution: - 1.0f (default): Renders at the native/default resolution - < 1.0f: Renders at a lower resolution (better performance, reduced visual quality) - 1.0f: Renders at a higher resolution (better visual quality, reduced performance) Returns [RenderConfiguration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_renderconfiguration) |
| --- | --- |

## Properties

| **suggestRenderSizeScale** : Float [Get] | The scaling factor for render resolution: - 1.0f (default): Renders at the native/default resolution - < 1.0f: Renders at a lower resolution (better performance, reduced visual quality) - 1.0f: Renders at a higher resolution (better visual quality, reduced performance) Signature ```kotlin val suggestRenderSizeScale: Float = 1.0f ``` |
| --- | --- |