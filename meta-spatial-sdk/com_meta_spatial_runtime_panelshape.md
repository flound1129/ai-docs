# PanelShape Class

*Modifiers:
final*

Creates and manages the 3D shape of a panel.

PanelShape is responsible for creating the appropriate mesh and layer for a panel based on the provided configuration. It handles different panel geometries (quad, cylinder, equirect) and manages the associated layers for high-fidelity rendering.

## Signature

```kotlin
class PanelShape(scene: Scene, val config: PanelShapeConfig, var panelSurface: PanelSurface, val sceneObject: SceneObject)
```

## Constructors

| **PanelShape** ( scene , config , panelSurface , sceneObject ) | Signature ```kotlin constructor(scene: Scene, config: PanelShapeConfig, panelSurface: PanelSurface, sceneObject: SceneObject) ``` Parameters scene: [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) config: [PanelShapeConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelshapeconfig) panelSurface: [PanelSurface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelsurface) sceneObject: [SceneObject](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sceneobject) Returns [PanelShape](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelshape) |
| --- | --- |

## Properties

| **config** : [PanelShapeConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelshapeconfig) [Get] | Signature ```kotlin val config: PanelShapeConfig ``` |
| --- | --- |
| **layer** : [SceneLayer?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenelayer) [Get][Set] | Signature ```kotlin var layer: SceneLayer? ``` |
| **panelSurface** : [PanelSurface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelsurface) [Get][Set] | Signature ```kotlin var panelSurface: PanelSurface ``` |
| **scale** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get][Set] | Signature ```kotlin var scale: Vector3 ``` |
| **sceneObject** : [SceneObject](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sceneobject) [Get] | Signature ```kotlin val sceneObject: SceneObject ``` |

## Functions

| **destroy** () | Signature ```kotlin fun destroy() ``` |
| --- | --- |
| **resize** ( scene , newPanelSurface ) | Signature ```kotlin fun resize(scene: Scene, newPanelSurface: PanelSurface) ``` Parameters scene: [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) newPanelSurface: [PanelSurface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelsurface) |