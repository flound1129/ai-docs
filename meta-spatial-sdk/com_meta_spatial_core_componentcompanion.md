# ComponentCompanion Interface

An interface for component companion objects that provides metadata about components.

This interface defines methods that return information about a component's dependencies, attributes, and other metadata.

## Signature

```kotlin
interface ComponentCompanion
```

## Properties

| **createDefaultInstance** : Function0 [Get] | Signature ```kotlin abstract val createDefaultInstance: () -> ComponentBase ``` |
| --- | --- |
| **id** : Int [Get] | Signature ```kotlin abstract val id: Int ``` |

## Functions

| **attributeKeys** () | Signature ```kotlin open fun attributeKeys(): IntArray ``` Returns IntArray |
| --- | --- |
| **attributeMetaData** () | Returns Map |
| **attributeTypeCountAvailable** () | Signature ```kotlin open fun attributeTypeCountAvailable(): Boolean ``` Returns Boolean |
| **attributeTypeCounts** () | Signature ```kotlin open fun attributeTypeCounts(): IntArray ``` Returns IntArray |
| **attributeTypes** () | Signature ```kotlin open fun attributeTypes(): IntArray ``` Returns IntArray |
| **dependents** () | Signature ```kotlin open fun dependents(): IntArray ``` Returns IntArray |
| **enumClassesMap** () | Signature ```kotlin open fun enumClassesMap(): Map<Int, Class<out Enum<*>>> ``` Returns Map |
| **keyStringToKeyIntMap** ( keyString ) | Signature ```kotlin open fun keyStringToKeyIntMap(keyString: String): Int? ``` Parameters keyString: String Returns Int? |