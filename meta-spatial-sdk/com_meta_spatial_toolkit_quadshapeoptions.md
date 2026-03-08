# QuadShapeOptions Class

Implements
[PanelConfigOptionsModifier](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelconfigoptionsmodifier)
,
[UIPanelShapeOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_uipanelshapeoptions)
,
[MediaPanelShapeOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mediapanelshapeoptions)
*Modifiers:
final*

## Signature

```kotlin
data class QuadShapeOptions(val width: Float = 1.0f, val height: Float = 0.75f) : PanelConfigOptionsModifier, UIPanelShapeOptions, MediaPanelShapeOptions
```

## Constructors

| **QuadShapeOptions** ( width , height ) | Signature ```kotlin constructor(width: Float = 1.0f, height: Float = 0.75f) ``` Parameters width: Float height: Float Returns [QuadShapeOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_quadshapeoptions) |
| --- | --- |

## Properties

| **height** : Float [Get] | Signature ```kotlin val height: Float = 0.75f ``` |
| --- | --- |
| **width** : Float [Get] | Signature ```kotlin val width: Float = 1.0f ``` |

## Functions

| **applyTo** ( options ) | Signature ```kotlin open override fun applyTo(options: PanelConfigOptions) ``` Parameters options: [PanelConfigOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelconfigoptions) |
| --- | --- |