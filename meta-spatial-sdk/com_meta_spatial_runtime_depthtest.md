# DepthTest Enum

Defines depth test comparison functions used in 3D rendering.

Depth testing is a technique used in 3D graphics to determine whether a fragment (pixel) should be drawn based on its depth value compared to the existing value in the depth buffer. This helps ensure that objects closer to the camera properly occlude objects that are farther away.

Each enum value represents a different comparison function that can be applied when testing the depth of a new fragment against the existing depth buffer value. The comparison determines whether the fragment passes the depth test and gets rendered.

Example usage:

```kotlin // Configure a material to only render pixels that are closer to the camera than existing pixels
sceneMaterial.setDepthTest(DepthTest.LESS)
// Configure a material to always render regardless of depth (useful for debug lines)
sceneMaterial.setDepthTest(DepthTest.ALWAYS)
// Configure a material to only render pixels at exactly the same depth as existing pixels
sceneMaterial.setDepthTest(DepthTest.EQUAL) ```

## Signature

```kotlin
enum DepthTest : Enum<DepthTest>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| NEVER | Never passes the depth test. The fragment is always discarded regardless of depth. Rarely used in practice. |
| LESS | Passes the depth test if the fragment's depth is less than the stored depth. This is the most common depth test function for standard 3D rendering, as it ensures closer objects occlude farther ones. |
| EQUAL | Passes the depth test if the fragment's depth is equal to the stored depth. Useful for drawing objects at exactly the same depth, like decals or overlays. |
| LESS_OR_EQUAL | Passes the depth test if the fragment's depth is less than or equal to the stored depth. Similar to LESS, but also includes fragments at exactly the same depth. |
| GREATER | Passes the depth test if the fragment's depth is greater than the stored depth. Can be used for special effects or rendering the back faces of objects. |
| NOT_EQUAL | Passes the depth test if the fragment's depth is not equal to the stored depth. Rarely used in standard rendering. |
| GREATER_OR_EQUAL | Passes the depth test if the fragment's depth is greater than or equal to the stored depth. Can be used for special effects or when rendering from back to front. |
| ALWAYS | Always passes the depth test. The fragment is always drawn regardless of depth. Useful for UI elements, skyboxes, or other objects that should not be occluded. |

## Properties

| **encoding** : Int [Get] | Integer value corresponding to the native graphics API encoding for this depth test function Signature ```kotlin val encoding: Int ``` |
| --- | --- |