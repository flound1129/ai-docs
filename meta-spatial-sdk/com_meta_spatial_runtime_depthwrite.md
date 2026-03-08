# DepthWrite Enum

Controls whether rendering operations write to the depth buffer.

The depth buffer (or Z-buffer) stores depth information for each pixel in a rendered scene. This enum determines whether a material will update the depth buffer when rendered.

Depth writing works in conjunction with depth testing ( [DepthTest](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_depthtest) ). While depth testing determines whether a fragment should be drawn based on existing depth values, depth writing controls whether that fragment updates the depth buffer with its own depth value.

Example usage:

```kotlin // Enable depth writing for standard opaque objects
sceneMaterial.setDepthWrite(DepthWrite.ENABLE)
// Disable depth writing for transparent objects
sceneMaterial.setDepthWrite(DepthWrite.DISABLE) ```

Common use cases:

- Enable depth writing for opaque objects to ensure proper occlusion - Disable depth writing for transparent objects to allow proper blending

## Signature

```kotlin
enum DepthWrite : Enum<DepthWrite>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| ENABLE | Enables writing to the depth buffer. When a fragment passes the depth test, its depth value will be written to the depth buffer, updating the stored depth at that pixel location. This is the standard setting for opaque objects to ensure proper occlusion in 3D scenes. |
| DISABLE | Disables writing to the depth buffer. When a fragment passes the depth test, it will be drawn but will not update the depth buffer. This is useful for transparent objects or special effects where you want to render something without affecting subsequent depth tests. |

## Properties

| **encoding** : Int [Get] | Integer value corresponding to the native graphics API encoding for this depth write mode Signature ```kotlin val encoding: Int ``` |
| --- | --- |