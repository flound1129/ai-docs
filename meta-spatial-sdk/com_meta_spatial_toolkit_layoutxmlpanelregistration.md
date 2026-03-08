# LayoutXMLPanelRegistration Class

Extends
[PanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelregistration)
*Modifiers:
final*

Panel registration for XML layout view-based panels.

This class is used when you want to create panels from predefined XML layout files stored in your app's resources. View-based panels are more performant than Activity-based panels.

Use this when:

- You prefer XML layouts over more modern UI frameworks like Jetpack Compose

## Constructors

| **LayoutXMLPanelRegistration** ( registrationId , layoutIdCreator , settingsCreator , panelSetupWithRootView ) | Parameters registrationId: Int Unique identifier for this panel registration layoutIdCreator: Function1 Function that returns the layout resource ID for each panel instance, allowing dynamic layout selection based on the entity settingsCreator: Function1 Function that creates PanelSettings for each panel instance, allowing dynamic panel configuration (size, position, etc.) panelSetupWithRootView: Function3 Optional setup function called after panel creation with access to the inflated root View, PanelSceneObject, and Entity for additional configuration like setting up click listeners, binding data, etc. Returns [LayoutXMLPanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_layoutxmlpanelregistration) |
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
| **panelCreator** ( scene , spatialContext ) | Returns a function that takes an entity as input and returns a PanelSceneObject. This function will be used to create the panel scene object in [PanelCreationSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelcreationsystem) . Whenever you create Entity with Panel(registrationId) component, this function will be called to create the panel scene object. Signature ```kotlin open override fun panelCreator(scene: Scene, spatialContext: SpatialContext): (entity: Entity) -> PanelSceneObject ``` Parameters scene: [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene in which the panel will be created. spatialContext: [SpatialContext](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialcontext) The spatial context of the panel. Returns Function1 A function that takes an entity as input and returns a PanelSceneObject. |
| **view** ( block ) | Parameters block: Function1 Returns [PanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelregistration) |