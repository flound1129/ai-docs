# ComponentManager Class

*Modifiers:
final*

Manages component registration, creation, and lifecycle in the Spatial SDK.

The ComponentManager is responsible for:

- Registering components with the system - Creating component instances - Tracking attribute information for components - Handling entity component lifecycle

How to register a component in your Spatial SDK Activity/Service:

```kotlin override fun onCreate() {
  super.onCreate()
  componentManager.registerComponent<MyComponent>(MyComponent.Companion)
} ```

## Signature

```kotlin
class ComponentManager
```

## Constructors

| **ComponentManager** () | Signature ```kotlin constructor() ``` Returns [ComponentManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentmanager) |
| --- | --- |

## Functions

| **assertComponent** ( clazz ) | Asserts that a component class is registered. Signature ```kotlin fun assertComponent(clazz: KClass<*>) ``` Parameters clazz: KClass The Kotlin class to check Throws IllegalArgumentException If the component class is not registered |
| --- | --- |
| **checkComponent** ( clazz ) | Checks if a component class is registered. Signature ```kotlin fun checkComponent(clazz: KClass<*>): Boolean ``` Parameters clazz: KClass The Kotlin class to check Returns Boolean True if the component is registered, false otherwise |
| **registerComponent** ( clazz , name , sendRate , companionObjectInstance ) | This method registers a component class with the ComponentManager, making it available for use with entities. It also registers the component's attributes with the DataModel and configures metadata settings. Signature ```kotlin fun registerComponent(clazz: KClass<*>, name: String, sendRate: SendRate, companionObjectInstance: ComponentCompanion) ``` Parameters clazz: KClass The Kotlin class of the component name: String The name of the component sendRate: SendRate companionObjectInstance: [ComponentCompanion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentcompanion) The companion object instance of the component class |
| **registerComponent** ( companionObjectInstance , sendRate ) | Registers a component with the ComponentManager using reified type parameters. Signature ```kotlin inline fun <T : ComponentBase> registerComponent(companionObjectInstance: ComponentCompanion, sendRate: SendRate = SendRate.DEFAULT) ``` Parameters companionObjectInstance: [ComponentCompanion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentcompanion) The companion object instance of the component class sendRate: SendRate The network synchronization rate for this component (defaults to DEFAULT) |