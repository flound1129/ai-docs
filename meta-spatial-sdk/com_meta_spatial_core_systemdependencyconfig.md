# SystemDependencyConfig Class

*Modifiers:
final*

Represents a configuration for a system dependency.

## Signature

```kotlin
data class SystemDependencyConfig(val clazz: KClass<out SystemBase>, val isRequired: Boolean = true)
```

## Constructors

| **SystemDependencyConfig** ( clazz , isRequired ) | Signature ```kotlin constructor(clazz: KClass<out SystemBase>, isRequired: Boolean = true) ``` Parameters clazz: KClass The class of the dependent system. isRequired: Boolean Whether the dependent system is required or not. Returns [SystemDependencyConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencyconfig) |
| --- | --- |

## Properties

| **clazz** : KClass [Get] | The class of the dependent system. Signature ```kotlin val clazz: KClass<out SystemBase> ``` |
| --- | --- |
| **isRequired** : Boolean [Get] | Whether the dependent system is required or not. Signature ```kotlin val isRequired: Boolean = true ``` |