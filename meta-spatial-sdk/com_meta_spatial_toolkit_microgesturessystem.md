# MicrogesturesSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

System for handling microgesture detection and state management.

This system monitors microgesture state changes and provides an API for other systems to register listeners for these changes.

Example usage:

```kotlin // Register a listener and get a handle
val handle = microgesturesSystem.addListener { microgestureBit, isActive ->
    when (microgestureBit) {
        MicrogestureBits.LeftMicrogestureSwipeLeft -> {
            // Handle left hand swipe left
        }
        MicrogestureBits.RightMicrogestureTapThumb -> {
            // Handle right hand thumb tap
        }
        // Handle other microgestures...
    }
}
// Remove the listener when no longer needed
microgesturesSystem.removeListener(handle) ```

## Signature

```kotlin
class MicrogesturesSystem : SystemBase
```

## Constructors

| **MicrogesturesSystem** () | Signature ```kotlin constructor() ``` Returns [MicrogesturesSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_microgesturessystem) |
| --- | --- |

## Properties

| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| --- | --- |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |

## Functions

| **addListener** ( listener ) | Add a listener for microgesture state changes Signature ```kotlin fun addListener(listener: MicrogestureStateChangeListener): MicrogestureListenerHandle ``` Parameters listener: [MicrogestureStateChangeListener](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_microgesturestatechangelistener) The lambda function to call when a microgesture state changes Returns [MicrogestureListenerHandle](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_microgesturelistenerhandle) A handle that can be used to remove the listener |
| --- | --- |
| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| **delete** ( entity ) | System should do any housekeeping based on [SystemBase.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase#delete) being removed from the scene Signature ```kotlin open fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open fun destroy() ``` |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |
| **removeListener** ( handle ) | Remove a listener for microgesture state changes Signature ```kotlin fun removeListener(handle: MicrogestureListenerHandle): Boolean ``` Parameters handle: [MicrogestureListenerHandle](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_microgesturelistenerhandle) The handle returned from addListener Returns Boolean True if the listener was removed, false if the handle was invalid |