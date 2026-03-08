# EnvironmentDepthMode Enum

Defines the modes for environment depth sensing.

Environment depth provides real-time depth information about the physical environment. Different modes control how this depth data is acquired and used during rendering.

Example usage:

```kotlin // Enable depth sensing with automatic occlusion
scene.setEnvironmentDepthMode(EnvironmentDepthMode.OCCLUSION)
// Enable depth sensing without occlusion (texture only)
scene.setEnvironmentDepthMode(EnvironmentDepthMode.TEXTURE_ONLY)
// Disable depth sensing
scene.setEnvironmentDepthMode(EnvironmentDepthMode.OFF) ```

## Signature

```kotlin
enum EnvironmentDepthMode : Enum<EnvironmentDepthMode>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| OFF | Environment depth is disabled. No depth sensing is performed. This is the default state and uses the least resources. |
| OCCLUSION | Environment depth is enabled with automatic occlusion. Virtual objects are automatically occluded by physical surfaces in the environment. The depth texture is also available globally in custom shaders for advanced effects. This is the traditional mode that provides both depth data and automatic occlusion. |
| TEXTURE_ONLY | Environment depth is enabled for texture access only, without automatic occlusion. The depth texture is made available globally in custom shaders, but virtual objects are NOT automatically occluded by the environment. This mode gives you full control over how to use depth data in your shaders. Use this mode when you want to implement custom depth-based effects like: - Custom occlusion logic in shaders - Depth-based visual effects (fog, outlines, etc.) - Soft blending at environment boundaries |

## Properties

| **index** : Int [Get] | The internal ID used to identify this mode in native code Signature ```kotlin val index: Int ``` |
| --- | --- |