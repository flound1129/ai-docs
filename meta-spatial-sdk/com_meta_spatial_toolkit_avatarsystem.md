# AvatarSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

This System handles the visibility of the controllers and hands.

This System comes default with Meta Spatial SDK and operates on entities with [AvatarAttachment](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_avatarattachment) and [Controller](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_controller) components. It interacts with [Transform](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_transform) , [Mesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mesh) , [Box](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_box) , [CreatorVisibility](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_creatorvisibility) , and [Visible](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_visible) components to manage avatar representation in the scene.

## Signature

```kotlin
class AvatarSystem : SystemBase
```

## Constructors

| **AvatarSystem** () | Signature ```kotlin constructor() ``` Returns [AvatarSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_avatarsystem) |
| --- | --- |

## Properties

| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| --- | --- |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **delete** ( entity ) | System should do any housekeeping based on [AvatarSystem.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_avatarsystem#delete) being removed from the scene Signature ```kotlin open override fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open fun destroy() ``` |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | The system must run after the PlayerBodyAttachmentSystem and before the MeshCreationSystem. Signature ```kotlin open override fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |
| **setShowControllers** ( showControllers ) | Set the visibility of the controllers. Signature ```kotlin fun setShowControllers(showControllers: Boolean = true) ``` Parameters showControllers: Boolean Whether to show the controllers. |
| **setShowHands** ( showHands ) | Set the visibility of the hands. By default, we show the hands wrapping around the controllers. If hands are set as visible while controllers are set as invisible, the hands will mimic natural poses while using the controller. Signature ```kotlin fun setShowHands(showHands: Boolean = true) ``` Parameters showHands: Boolean Whether to show the hands. |