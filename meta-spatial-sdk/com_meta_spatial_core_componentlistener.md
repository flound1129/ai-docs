# ComponentListener Type Alias

Callback method that is run when the defined component is changed

## Signature

```kotlin
typealias ComponentListener = (entity: Entity, dataModel: DataModel, componentID: Int, component: ComponentBase, packet: Any?) -> Unit
```