# PanelCreator Class

Extends
[PanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelregistration)
*Modifiers:
final*

PanelCreator is a class that allows you to specify the panel creator function for a panel. The panel creator function is any customized function that takes an entity as input and returns the [PanelSceneObject](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelsceneobject) .

## See Also

- [PanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelregistration)

## Signature

```kotlin
class PanelCreator(val registrationId: Int, panelCreator: (entity: Entity) -> PanelSceneObject) : PanelRegistration
```

## Constructors

| **PanelCreator** ( registrationId , panelCreator ) | Signature ```kotlin constructor(registrationId: Int, panelCreator: (entity: Entity) -> PanelSceneObject) ``` Parameters registrationId: Int The unique identifier for the panel. panelCreator: Function1 A function that takes an entity as input and returns a PanelSceneObject. Returns [PanelCreator](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelcreator) |
| --- | --- |

## Properties

| **activityClass** : Class? [Get][Set] | Activity class if the panel is powered by an activity and its layout/logic. Signature ```kotlin var activityClass: Class<*>? ``` |
| --- | --- |
| **init** : Function2 [Get] | The initialization block that will be called when the panel is created Signature ```kotlin val init: PanelRegistration.(entity: Entity) -> Unit ``` |
| **layoutResourceId** : Int? [Get][Set] | Layout resource id if the panel is view-based and created in the same immersive activity. Signature ```kotlin var layoutResourceId: Int? ``` |
| **panelIntent** : Intent? [Get][Set] | Intent to launch the panel's activity if the panel is activity-based. Signature ```kotlin var panelIntent: Intent ``` |
| **registrationId** : Int [Get] | The unique identifier for this panel Signature ```kotlin val registrationId: Int ``` |

## Functions

| **config** ( overriding , block ) | Signature ```kotlin fun config(overriding: Boolean = true, block: PanelConfigOptions.() -> Unit): PanelRegistration ``` Parameters overriding: Boolean block: Function1 Returns [PanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelregistration) |
| --- | --- |
| **panel** ( overriding , block ) | Signature ```kotlin fun panel(overriding: Boolean = true, block: PanelSceneObject.() -> Unit): PanelRegistration ``` Parameters overriding: Boolean block: Function1 Returns [PanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelregistration) |
| **panelComponent** () | Returns the [Panel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panel) component that will be used to create the panel entity. Signature ```kotlin fun panelComponent(): Panel ``` Returns [Panel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panel) |
| **panelCreator** ( scene , spatialContext ) | Returns a function that takes an entity as input and returns a PanelSceneObject. This function will be used to create the panel scene object in [PanelCreationSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelcreationsystem) . Whenever you create Entity with Panel(registrationId) component, this function will be called to create the panel scene object. Signature ```kotlin open fun panelCreator(scene: Scene, spatialContext: SpatialContext): (entity: Entity) -> PanelSceneObject ``` Parameters scene: [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene in which the panel will be created. spatialContext: [SpatialContext](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialcontext) The spatial context of the panel. Returns Function1 A function that takes an entity as input and returns a PanelSceneObject. |
| **view** ( block ) | Parameters block: Function1 Returns [PanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelregistration) |