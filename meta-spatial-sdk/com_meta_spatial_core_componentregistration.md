# ComponentRegistration Class

*Modifiers:
final*

ComponentRegistration is used to register components when creating a SpatialFeature. It is generally used and returned in a list in the SpatialFeature.componentsToRegister() method. It is recommeded to create a ComponentRegistration using the static createConfig() method.

Example:

```kotlin override fun componentsToRegister(): List<ComponentRegistration> {
  return listOf(
      ComponentRegistration.createConfig<Audio>(Audio.Companion),
      ComponentRegistration.createConfig<Video>(Video.Companion))
 } ```

## Signature

```kotlin
class ComponentRegistration(val clazz: KClass<out ComponentBase>, val companionObjectInstance: ComponentCompanion, val sendRate: SendRate = SendRate.DEFAULT)
```

## Constructors

| **ComponentRegistration** ( clazz , companionObjectInstance , sendRate ) | Signature ```kotlin constructor(clazz: KClass<out ComponentBase>, companionObjectInstance: ComponentCompanion, sendRate: SendRate = SendRate.DEFAULT) ``` Parameters clazz: KClass The Kotlin class of the component being registered companionObjectInstance: [ComponentCompanion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentcompanion) The companion object instance for the component, which provides metadata about the component's attributes and dependencies sendRate: SendRate The network synchronization rate and reliability settings for this component, determining how often and how reliably component updates are sent over the network Returns [ComponentRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentregistration) |
| --- | --- |

## Properties

| **clazz** : KClass [Get] | The Kotlin class of the component being registered Signature ```kotlin val clazz: KClass<out ComponentBase> ``` |
| --- | --- |
| **companionObjectInstance** : [ComponentCompanion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentcompanion) [Get] | The companion object instance for the component, which provides metadata about the component's attributes and dependencies Signature ```kotlin val companionObjectInstance: ComponentCompanion ``` |
| **sendRate** : SendRate [Get] | The network synchronization rate and reliability settings for this component, determining how often and how reliably component updates are sent over the network Signature ```kotlin val sendRate: SendRate ``` |

## Companion Object

### Companion Object Functions

| **createConfig** ( companionObjectInstance , sendRate ) | Creates a ComponentRegistration configuration for the specified component type. This is generally used and returned in a list in the SpatialFeature.componentsToRegister() method. Example: ```kotlin override fun componentsToRegister(): List<ComponentRegistration> { return listOf( ComponentRegistration.createConfig<Audio>(Audio.Companion), ComponentRegistration.createConfig<Video>(Video.Companion)) } ``` Signature ```kotlin inline fun <T : ComponentBase> createConfig(companionObjectInstance: ComponentCompanion, sendRate: SendRate = SendRate.DEFAULT): ComponentRegistration ``` Parameters companionObjectInstance: [ComponentCompanion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentcompanion) The companion object instance for the component sendRate: SendRate The network synchronization settings for this component Returns [ComponentRegistration](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentregistration) A new ComponentRegistration instance for the specified component type |
| --- | --- |