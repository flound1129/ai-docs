# PlayerBodyAttachmentSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

This PlayerBodyAttachmentSystem is responsible for setting the local player's avatar body components based on the local player's attachments.

This System comes default with Meta Spatial SDK and operates on entities with [AvatarAttachment](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_avatarattachment) components. It interacts with [Controller](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_controller) , [AvatarBody](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_avatarbody) , and [Transform](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_transform) components to manage the local player's avatar representation.

## Signature

```kotlin
class PlayerBodyAttachmentSystem : SystemBase
```

## Constructors

| **PlayerBodyAttachmentSystem** () | Signature ```kotlin constructor() ``` Returns [PlayerBodyAttachmentSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_playerbodyattachmentsystem) |
| --- | --- |

## Properties

| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| --- | --- |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **delete** ( entity ) | System should do any housekeeping based on [SystemBase.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase#delete) being removed from the scene Signature ```kotlin open fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open fun destroy() ``` |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |
| **tryGetLocalPlayerAvatarBody** () | Get the local player's avatar body, if it exists. Signature ```kotlin fun tryGetLocalPlayerAvatarBody(): AvatarBody? ``` Returns [AvatarBody?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_avatarbody) |