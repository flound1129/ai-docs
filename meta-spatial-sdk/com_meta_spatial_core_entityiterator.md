# EntityIterator Interface

Extends
Iterator, Closeable
## Signature

```kotlin
interface EntityIterator : Iterator<Entity> , Closeable
```

## Functions

| **close** () | Signature ```kotlin abstract override fun close() ``` |
| --- | --- |
| **forEachRemaining** ( p0 ) | Signature ```kotlin open fun forEachRemaining(p0: Consumer<in Entity>) ``` Parameters p0: Consumer |
| **hasNext** () | Signature ```kotlin abstract operator fun hasNext(): Boolean ``` Returns Boolean |
| **next** () | Signature ```kotlin abstract operator fun next(): Entity ``` Returns [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |