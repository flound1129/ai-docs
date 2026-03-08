# SystemManager Class

*Modifiers:
final*

Manages the lifecycle and execution of systems within the Spatial SDK.

SystemManager is responsible for organizing, prioritizing, and executing systems in a deterministic order based on their dependencies. It maintains a directed acyclic graph (DAG) of systems to ensure proper execution order and handles system registration, discovery, and lifecycle management.

Systems can be registered with different priority groups (EARLY, NORMAL, LATE) to control their relative execution order. The manager ensures systems are executed in topologically sorted order based on their dependencies and priority groups.

Example usage:

```kotlin // Register a system
systemManager.registerSystem(MyCustomSystem())
// Find a system by class
val avatarSystem = systemManager.findSystem<AvatarSystem>() ```

The SystemManager is created and managed by AppSystemActivity or other activity classes that extend from VrActivity.

## Signature

```kotlin
class SystemManager
```

## Constructors

| **SystemManager** () | Signature ```kotlin constructor() ``` Returns [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) |
| --- | --- |

## Functions

| **findSystem** ( clazz ) | Finds a system by its class. Signature ```kotlin fun <T : SystemBase> findSystem(clazz: KClass<T>): T ``` Parameters clazz: KClass The class of the system to find. Returns [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system instance. Throws Exception if the system is not found. |
| --- | --- |
| **findSystem** () | Finds a system by its type using reified type parameters. Signature ```kotlin inline fun <T : SystemBase> findSystem(): T ``` Returns [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system instance. Throws Exception if the system is not found. |
| **getScene** () | Returns the scene associated with the manager. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The associated scene. |
| **registerEarlySystem** ( system ) | Registers an early system that will be executed before other systems. Signature ```kotlin fun registerEarlySystem(system: SystemBase) ``` Parameters system: [SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase) The early system to register. |
| **registerLateSystem** ( system ) | Registers a late system that will be executed after other systems. Signature ```kotlin fun registerLateSystem(system: SystemBase) ``` Parameters system: [SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase) The late system to register. |
| **registerSystem** ( system ) | Adds a system to the manager, which will be called for all operations. Example usage: ```kotlin override fun onCreate(savedInstanceState: Bundle?) { systemManager.registerSystem(MyCustomSystem()) } ``` Signature ```kotlin fun registerSystem(system: SystemBase) ``` Parameters system: [SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase) The system to add. |
| **setEarlySystems** ( earlySystems ) | Sets the early systems in the manager. Early systems are executed before normal priority systems. Signature ```kotlin fun setEarlySystems(earlySystems: List<SystemBase>) ``` Parameters earlySystems: List The early systems to set. |
| **setLateSystems** ( lateSystems ) | Sets the late systems in the manager. Late systems are executed after normal priority systems. Signature ```kotlin fun setLateSystems(lateSystems: List<SystemBase>) ``` Parameters lateSystems: List The late systems to set. |
| **tryFindSystem** ( clazz ) | Tries to find a system by its class. Signature ```kotlin fun <T : SystemBase> tryFindSystem(clazz: KClass<T>): T? ``` Parameters clazz: KClass The class of the system to find. Returns [SystemManager?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system instance or null if not found. |
| **tryFindSystem** () | Tries to find a system by its type using reified type parameters. Signature ```kotlin inline fun <T : SystemBase> tryFindSystem(): T? ``` Returns [SystemManager?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system instance or null if not found. |
| **unregisterSystem** ( clazz ) | Unregisters a system from the manager. Example usage: ```kotlin override fun onCreate(savedInstanceState: Bundle?) { // Unregister locomotion system to prevent controller movement systemManager.unregisterSystem<LocomotionSystem>() } ``` Signature ```kotlin fun <T : SystemBase> unregisterSystem(clazz: KClass<T>) ``` Parameters clazz: KClass The class of the system to unregister. |
| **unregisterSystem** () | Unregisters a system by its type using reified type parameters. Signature ```kotlin inline fun <T : SystemBase> unregisterSystem() ``` |