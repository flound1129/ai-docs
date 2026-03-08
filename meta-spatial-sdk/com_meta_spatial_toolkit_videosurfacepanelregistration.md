# VideoSurfacePanelRegistration Class

Extends
[PanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_panelregistration)
*Modifiers:
final*

Panel registration for direct-to-surface media rendering.

This class is used when you want to create panels that render media content directly to a surface, bypassing the standard Android View system for optimal performance. This is particularly useful for video playback, camera feeds, or other media content that benefits from direct surface rendering.

DisplayOptions within MediaPanelSettings will be ignored in this API. The pixel resolution of this panel will be driven by the surface you pass in. For example, if you pass in an exoplayer surface then the media content driving exoplayer will set the pixel resolution on the panel.

Use this when:

- You need to render video or other media content with minimal latency - You want to bypass the Android View system for performance-critical media rendering - You have custom media rendering logic that works directly with Android surfaces

## Constructors

| **VideoSurfacePanelRegistration** ( registrationId , surfaceConsumer , settingsCreator , panelSetup ) | Parameters registrationId: Int Unique identifier for this panel registration surfaceConsumer: Function2 Function that receives the entity and surface for custom media rendering setup. This is where you would configure your media player or renderer to output to the provided surface. settingsCreator: Function1 Function that creates MediaPanelSettings for each panel instance, allowing dynamic panel configuration optimized for media content panelSetup: Function2 Optional setup function called after panel creation for additional configuration of the PanelSceneObject Returns [VideoSurfacePanelRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_videosurfacepanelregistration) |
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