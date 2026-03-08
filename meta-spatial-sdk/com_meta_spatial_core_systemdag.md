# SystemDAG Class

*Modifiers:
final*

Manages the dependency graph of systems in the Spatial SDK.

SystemDAG (Directed Acyclic Graph) is responsible for:

- Tracking system dependencies and their relationships - Ensuring proper execution order based on dependencies - Detecting and preventing dependency cycles - Organizing systems into priority groups for execution

Systems can specify dependencies using mustRunBefore and mustRunAfter relationships, which this class resolves into a valid execution order.

## Signature

```kotlin
class SystemDAG
```

## Constructors

| **SystemDAG** () | Signature ```kotlin constructor() ``` Returns [SystemDAG](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdag) |
| --- | --- |

## Functions

| **addSystem** ( system , priorityGroup ) | Adds a system to the dependency graph. This method: - Checks for duplicate systems - Adds the system's dependencies to the graph - Applies any missing edges to the new system - Registers the system in the appropriate priority group Signature ```kotlin fun addSystem(system: SystemBase, priorityGroup: PriorityGroup = PriorityGroup.NORMAL) ``` Parameters system: [SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase) The system instance to add priorityGroup: [PriorityGroup](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_prioritygroup) The priority group to assign to the system (default: NORMAL) Throws IllegalArgumentException If the system is already registered |
| --- | --- |
| **findSystem** ( clazz ) | Finds a system in the dependency graph. Throws an exception if the system is not found. Signature ```kotlin fun <T : SystemBase> findSystem(clazz: KClass<T>): T ``` Parameters clazz: KClass The class reference of the system to find Returns [SystemDAG](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdag) The system instance Throws Exception If the system is not registered with the SystemManager |
| **getEarlySystems** () | Gets the list of early systems that runs before all other systems. Signature ```kotlin fun getEarlySystems(): List<SystemBase> ``` Returns List The list of early systems |
| **getLateSystems** () | Gets the list of late systems that runs after all other systems. Signature ```kotlin fun getLateSystems(): List<SystemBase> ``` Returns List The list of late systems |
| **getUnorderedLateExecuteSystems** () | Gets the list of all systems that implement LateExecuteSystem that have been added to the DAG. The order of the systems is NOT guaranteed. Signature ```kotlin fun getUnorderedLateExecuteSystems(): List<SystemBaseWithLateExecute> ``` Returns List The list of all LateExecuteSystems in the DAG (unordered) |
| **removeSystem** ( clazz ) | Removes a system from the dependency graph. Signature ```kotlin fun <T : SystemBase> removeSystem(clazz: KClass<T>): Boolean ``` Parameters clazz: KClass The class reference of the system to remove Returns Boolean True if the system was found and removed, false otherwise |
| **removeSystem** () | Removes a system from the dependency graph using reified type parameter. Signature ```kotlin inline fun <T : SystemBase> removeSystem(): Boolean ``` Returns Boolean True if the system was found and removed, false otherwise |
| **setEarlySystems** ( earlySystems ) | Sets the list of early systems that runs before all other systems. Signature ```kotlin fun setEarlySystems(earlySystems: List<SystemBase>) ``` Parameters earlySystems: List The list of early systems Throws RuntimeException If early systems have already been set |
| **setLateSystems** ( lateSystems ) | Sets the list of late systems that runs after all other systems. Signature ```kotlin fun setLateSystems(lateSystems: List<SystemBase>) ``` Parameters lateSystems: List The list of late systems Throws RuntimeException If late systems have already been set |
| **topologicalSortWithCycleDetection** () | Performs a topological sort of the systems based on their dependencies. This method: - Validates that all required dependencies are present - Detects and reports any dependency cycles - Ensures systems are ordered according to their priority groups - Ensures systems within each priority group respect their dependencies Signature ```kotlin fun topologicalSortWithCycleDetection(): MutableList<SystemBase> ``` Returns MutableList A sorted list of systems in the order they should be executed Throws RuntimeException If required dependencies are missing or if a cycle is detected |
| **tryFindSystem** ( clazz ) | Attempts to find a system in the dependency graph. Signature ```kotlin fun <T : SystemBase> tryFindSystem(clazz: KClass<T>): T? ``` Parameters clazz: KClass The class reference of the system to find Returns [SystemDAG?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdag) The system instance if found, null otherwise |