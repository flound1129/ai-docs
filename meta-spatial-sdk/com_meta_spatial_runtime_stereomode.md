# StereoMode Enum

StereoMode controls how a single texture is mapped to left and right eye views for stereoscopic rendering. Used in [PanelConfigOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelconfigoptions) for panel creation and [SceneMaterial](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenematerial) for material mapping based on eye display.

Example usage: Creating a panel for displaying stereoscopic 1920x1080 video.

```kotlin override fun registerPanels(): List<PanelRegistration> {
  return listOf(
      PanelRegistration(R.layout.panel_layout) {
        config {
          includeGlass = false
          width = 1.0f * (1920f / 1080f) // Match aspect ratio of panel shape with video resolution
          height = 1.0f
          layoutWidthInPx = 1920 * 2 // Displaying a StereoMode.LeftRight video, so width needs to be doubled.
          layoutHeightInPx = 1080
          stereoMode = StereoMode.LeftRight // Assign StereoMode
        }
      })
} ```

Example usage: SceneMaterial applying a Stereoscopic effect to its texture. (Useful for custom shaders that use a Stereoscopic panel's [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) as input)

```kotlin SceneMaterial.custom(
          "customShaderName",
          arrayOf(
              SceneMaterialAttribute("albedoSampler", SceneMaterialDataType.Texture2D),
          ))
      .apply {
         setTexture("albedoSampler", albedoTexture)
         setStereoMode(StereoMode.None)
       } ```

## Signature

```kotlin
enum StereoMode : Enum<StereoMode>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| None | Default mode with no stereoscopic rendering. The entire texture is shown identically to both eyes without any UV modifications. Use this for regular 2D content or when stereo is handled elsewhere. |
| LeftRight | Side-by-side stereo mode. Displays the left half of the texture in the left eye, and the right half in the right eye. This is commonly used for side-by-side stereo videos and images where the left and right eye views are placed horizontally adjacent to each other in a single texture. |
| UpDown | Top-bottom stereo mode. Displays the top half of the texture in the left eye, and the bottom half in the right eye. This is commonly used for over-under stereo videos and images where the left and right eye views are stacked vertically in a single texture. |
| MonoLeft | Monoscopic left mode. Displays only the left half of the texture, showing the same content to both eyes. This can be used to display the left eye view of side-by-side stereo content as a regular monoscopic image. |
| MonoUp | Monoscopic top mode. Displays only the top half of the texture, showing the same content to both eyes. This can be used to display the left eye view of top-bottom stereo content as a regular monoscopic image. |

## Properties

| **view2OffsetX** : Float [Get] | X offset for the second view (right eye) Signature ```kotlin val view2OffsetX: Float ``` |
| --- | --- |
| **view2OffsetY** : Float [Get] | Y offset for the second view (right eye) Signature ```kotlin val view2OffsetY: Float ``` |
| **viewScaleX** : Float [Get] | X scale factor for both views Signature ```kotlin val viewScaleX: Float ``` |
| **viewScaleY** : Float [Get] | Y scale factor for both views Signature ```kotlin val viewScaleY: Float ``` |