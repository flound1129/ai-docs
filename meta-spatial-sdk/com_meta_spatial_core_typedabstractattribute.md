# TypedAbstractAttribute Class

Implements
[AbstractAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_abstractattribute)
*Modifiers:
abstract*

Base class for typed attributes that provides common functionality.

This abstract class implements the AbstractAttribute interface and provides common functionality for typed attributes, including validation and error checking.

## Signature

```kotlin
abstract class TypedAbstractAttribute<T>(keyString: String, key: Int, component: ComponentBase) : AbstractAttribute
```

## Constructors

| **TypedAbstractAttribute** ( keyString , key , component ) | Signature ```kotlin constructor(keyString: String, key: Int, component: ComponentBase) ``` Parameters keyString: String The string key for this attribute key: Int The integer key for this attribute component: [ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase) The component this attribute belongs to Returns [TypedAbstractAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_typedabstractattribute) |
| --- | --- |

## Functions

| **checkIfComponentIsOld** () | Signature ```kotlin fun checkIfComponentIsOld() ``` |
| --- | --- |
| **checkIfComponentIsRecycled** () | Signature ```kotlin fun checkIfComponentIsRecycled() ``` |
| **get** () | Signature ```kotlin abstract fun get(): Any ``` Returns Any |
| **keyName** () | Signature ```kotlin fun keyName(): String ``` Returns String |
| **set** ( value ) | Signature ```kotlin abstract fun set(value: Any) ``` Parameters value: Any |