# SystemMap Type Alias

Maps system classes to their corresponding system instances. Used to track all registered systems and retrieve their instances when needed.

## Signature

```kotlin
typealias SystemMap = MutableMap<SystemClass, SystemBase>
```