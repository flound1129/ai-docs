# UIPanelRenderOptions Class

Implements
[PanelConfigOptionsModifier](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelconfigoptionsmodifier)
*Modifiers:
final*

Rendering configuration specific to UI panels.

## Signature

```kotlin
data class UIPanelRenderOptions(val renderMode: PanelRenderMode = PanelRenderMode.Layer()) : PanelConfigOptionsModifier
```

## Constructors

| **UIPanelRenderOptions** ( renderMode ) | Signature ```kotlin constructor(renderMode: PanelRenderMode = PanelRenderMode.Layer()) ``` Parameters renderMode: [PanelRenderMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelrendermode) Control how the panel will render in the scene. Use layers to make panels appear crisp and high resolution, or mesh for basic rendering without compositor layers. Returns [UIPanelRenderOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_uipanelrenderoptions) |
| --- | --- |

## Properties

| **renderMode** : [PanelRenderMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelrendermode) [Get] | Control how the panel will render in the scene. Use layers to make panels appear crisp and high resolution, or mesh for basic rendering without compositor layers. Signature ```kotlin val renderMode: PanelRenderMode ``` |
| --- | --- |

## Functions

| **applyTo** ( options ) | Signature ```kotlin open override fun applyTo(options: PanelConfigOptions) ``` Parameters options: [PanelConfigOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelconfigoptions) |
| --- | --- |