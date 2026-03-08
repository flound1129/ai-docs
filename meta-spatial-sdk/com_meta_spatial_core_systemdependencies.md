# SystemDependencies Class

*Modifiers:
final*

Represents a collection of system dependencies.

## Signature

```kotlin
data class SystemDependencies(val mustRunBefore: MutableSet<SystemDependencyConfig>? = null, val mustRunAfter: MutableSet<SystemDependencyConfig>? = null)
```

## Constructors

| **SystemDependencies** ( mustRunBefore , mustRunAfter ) | Signature ```kotlin constructor(mustRunBefore: MutableSet<SystemDependencyConfig>? = null, mustRunAfter: MutableSet<SystemDependencyConfig>? = null) ``` Parameters mustRunBefore: MutableSet? A set of systems that must run before this system. mustRunAfter: MutableSet? A set of systems that must run after this system. Returns [SystemDependencies](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) |
| --- | --- |

## Properties

| **mustRunAfter** : MutableSet? [Get] | A set of systems that must run after this system. Signature ```kotlin val mustRunAfter: MutableSet<SystemDependencyConfig>? = null ``` |
| --- | --- |
| **mustRunBefore** : MutableSet? [Get] | A set of systems that must run before this system. Signature ```kotlin val mustRunBefore: MutableSet<SystemDependencyConfig>? = null ``` |