# DeleteListenerHolder Class

*Modifiers:
final*

Holder class for delete listeners that allows weak reference semantics. When a CachedQuery goes out of scope, the weak reference to its DeleteListenerHolder will be automatically cleaned up during the next delete notification.

## Signature

```kotlin
class DeleteListenerHolder(val listener: (Long) -> Unit)
```

## Constructors

| **DeleteListenerHolder** ( listener ) | Signature ```kotlin constructor(listener: (Long) -> Unit) ``` Parameters listener: Function1 Returns [DeleteListenerHolder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_deletelistenerholder) |
| --- | --- |

## Properties

| **listener** : Function1 [Get] | Signature ```kotlin val listener: (Long) -> Unit ``` |
| --- | --- |

## Functions

| **invoke** ( entityId ) | Signature ```kotlin operator fun invoke(entityId: Long) ``` Parameters entityId: Long |
| --- | --- |