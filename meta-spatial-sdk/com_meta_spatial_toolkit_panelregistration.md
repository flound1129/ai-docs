# PanelRegistration Class

*Modifiers:
open*

PanelRegistration is a class that allows you to register a panel with the Spatial Toolkit. To use panels in your app, you will need to:

- Register the panel definition - Spawn the panel in the 3D scene

Details on how to use this class can be found in the [Spatial Toolkit documentation](https://developers.meta.com/horizon/documentation/spatial-sdk/spatial-sdk-2dpanel-registration) .

## See Also

- [PanelCreationSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelcreationsystem)

## Signature

```kotlin
open class PanelRegistration(val registrationId: Int, val init: PanelRegistration.(entity: Entity) -> Unit = {})
```

## Constructors

| **PanelRegistration** ( registrationId , init ) | Signature ```kotlin constructor(registrationId: Int, init: PanelRegistration.(entity: Entity) -> Unit = {}) ``` Parameters registrationId: Int The unique identifier for this panel init: Function2 The initialization block that will be called when the panel is created Returns [PanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelregistration) |
| --- | --- |

## Properties

| **activityClass** : Class? [Get][Set] | Activity class if the panel is powered by an activity and its layout/logic. Signature ```kotlin var activityClass: Class<*>? ``` |
| --- | --- |
| **init** : Function2 [Get] | The initialization block that will be called when the panel is created Signature ```kotlin val init: PanelRegistration.(entity: Entity) -> Unit ``` |
| **layoutResourceId** : Int? [Get][Set] | Layout resource id if the panel is view-based and created in the same immersive activity. Signature ```kotlin var layoutResourceId: Int? ``` |
| **panelIntent** : Intent? [Get][Set] | Intent to launch the panel's activity if the panel is activity-based. Signature ```kotlin var panelIntent: Intent ``` |
| **registrationId** : Int [Get] | The unique identifier for this panel Signature ```kotlin val registrationId: Int ``` |

## Functions

| **composePanel** ( composeViewFun ) | Parameters composeViewFun: Function1 Returns [PanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelregistration) |
| --- | --- |
| **config** ( overriding , block ) | Signature ```kotlin fun config(overriding: Boolean = true, block: PanelConfigOptions.() -> Unit): PanelRegistration ``` Parameters overriding: Boolean block: Function1 Returns [PanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelregistration) |
| **panel** ( overriding , block ) | Signature ```kotlin fun panel(overriding: Boolean = true, block: PanelSceneObject.() -> Unit): PanelRegistration ``` Parameters overriding: Boolean block: Function1 Returns [PanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelregistration) |
| **panelComponent** () | Returns the [Panel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panel) component that will be used to create the panel entity. Signature ```kotlin fun panelComponent(): Panel ``` Returns [Panel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panel) |
| **panelCreator** ( scene , spatialContext ) | Returns a function that takes an entity as input and returns a PanelSceneObject. This function will be used to create the panel scene object in [PanelCreationSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelcreationsystem) . Whenever you create Entity with Panel(registrationId) component, this function will be called to create the panel scene object. Signature ```kotlin open fun panelCreator(scene: Scene, spatialContext: SpatialContext): (entity: Entity) -> PanelSceneObject ``` Parameters scene: [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene in which the panel will be created. spatialContext: [SpatialContext](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialcontext) The spatial context of the panel. Returns Function1 A function that takes an entity as input and returns a PanelSceneObject. |
| **view** ( block ) | Parameters block: Function1 Returns [PanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelregistration) |