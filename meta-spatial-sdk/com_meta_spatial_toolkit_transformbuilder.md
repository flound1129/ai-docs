# TransformBuilder Class

*Modifiers:
final*

A builder class for creating and chaining spatial transformations that result in a final [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose)

TransformBuilder allows for the creation of complex transformations by combining translation and rotation operations. These operations can be chained together to create composite transformations.

It is important to note that chaining transformations makes it so that the subsequent transformations are applied as if looking from the rotation of the previous transformation, not from the world graph. For example, if you rotate 180 degrees around the y-axis, then move +1 meter along the z-axis, the resulting world position will be (0, 0, -1) instead of (0, 0, 1).

Example usage:

```kotlin val pose = TransformBuilder().move(1f, 2f, 3f).then(TransformBuilder().rotateX(90f)).build() ```

## Signature

```kotlin
class TransformBuilder
```

## Constructors

| **TransformBuilder** () | Signature ```kotlin constructor() ``` Returns [TransformBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_transformbuilder) |
| --- | --- |

## Functions

| **build** () | Builds the final Transform from the configured transformation steps. Signature ```kotlin fun build(): Transform ``` Returns [Transform](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_transform) A Transform object representing the composite transformation Throws NullPointerException if no transformation steps have been added |
| --- | --- |
| **cosDegrees** ( angleInDegrees ) | Helper function that calculates the cosine of an angle specified in degrees. Signature ```kotlin fun cosDegrees(angleInDegrees: Float): Float ``` Parameters angleInDegrees: Float The angle in degrees Returns Float The cosine value of the angle |
| **degreesToRadians** ( angleInDegrees ) | Helper function that converts an angle from degrees to radians. Signature ```kotlin fun degreesToRadians(angleInDegrees: Float): Float ``` Parameters angleInDegrees: Float The angle in degrees Returns Float The equivalent angle in radians |
| **move** ( x , y , z ) | Creates a translation transformation. It is important to note that the translation is applied as if looking from the rotation of the previous TransformBuilder transformation, not from the world graph. For example, if you had rotated 180 degrees around the y-axis, the applied this transformation to move with z=1, the resulting world position will be (0, 0, -1) instead of (0, 0, 1). Signature ```kotlin fun move(x: Float = 0.0f, y: Float = 0.0f, z: Float = 0.0f): TransformBuilder.TransformStepBuilder ``` Parameters x: Float The translation distance along the X axis y: Float The translation distance along the Y axis z: Float The translation distance along the Z axis Returns TransformBuilder.TransformStepBuilder A TransformStepBuilder that can be used to chain additional transformations |
| **rotate_x** ( angleInDegrees ) | Helper function that creates a quaternion representing a rotation around the X axis. Signature ```kotlin fun rotate_x(angleInDegrees: Float): Quaternion ``` Parameters angleInDegrees: Float The rotation angle in degrees Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A Quaternion representing the rotation |
| **rotate_y** ( angleInDegrees ) | Helper function that creates a quaternion representing a rotation around the Y axis. Signature ```kotlin fun rotate_y(angleInDegrees: Float): Quaternion ``` Parameters angleInDegrees: Float The rotation angle in degrees Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A Quaternion representing the rotation |
| **rotate_z** ( angleInDegrees ) | Helper function that creates a quaternion representing a rotation around the Z axis. Signature ```kotlin fun rotate_z(angleInDegrees: Float): Quaternion ``` Parameters angleInDegrees: Float The rotation angle in degrees Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A Quaternion representing the rotation |
| **rotateX** ( angleInDegrees ) | Creates a rotation transformation around the X axis. Note that the rotation is applied as if looking from the rotation of the previous transformation, so if you rotated 180 degrees around the x-axis, then applied this transformation to rotate 90 degrees around the x-axis, the resulting world rotation will be 270 degrees around the x-axis Signature ```kotlin fun rotateX(angleInDegrees: Float): TransformBuilder.TransformStepBuilder ``` Parameters angleInDegrees: Float The rotation angle in degrees Returns TransformBuilder.TransformStepBuilder A TransformStepBuilder that can be used to chain additional transformations |
| **rotateY** ( angleInDegrees ) | Creates a rotation transformation around the Y axis. Note that the rotation is applied as if looking from the rotation of the previous transformation, so if you rotated 180 degrees around the y-axis, then applied this transformation to rotate 90 degrees around the y-axis, the resulting world rotation will be 270 degrees around the y-axis Signature ```kotlin fun rotateY(angleInDegrees: Float): TransformBuilder.TransformStepBuilder ``` Parameters angleInDegrees: Float The rotation angle in degrees Returns TransformBuilder.TransformStepBuilder A TransformStepBuilder that can be used to chain additional transformations |
| **rotateZ** ( angleInDegrees ) | Creates a rotation transformation around the Z axis. Note that the rotation is applied as if looking from the rotation of the previous transformation, so if you rotated 180 degrees around the z-axis, then applied this transformation to rotate 90 degrees around the z-axis, the resulting world rotation will be 270 degrees around the z-axis Signature ```kotlin fun rotateZ(angleInDegrees: Float): TransformBuilder.TransformStepBuilder ``` Parameters angleInDegrees: Float The rotation angle in degrees Returns TransformBuilder.TransformStepBuilder A TransformStepBuilder that can be used to chain additional transformations |
| **sinDegrees** ( angleInDegrees ) | Helper function that calculates the sine of an angle specified in degrees. Signature ```kotlin fun sinDegrees(angleInDegrees: Float): Float ``` Parameters angleInDegrees: Float The angle in degrees Returns Float The sine value of the angle |

## Inner Class

### TransformStepBuilder Class

*Modifiers:
final*

A builder class for chaining transformation steps. This is as a helper class for [TransformBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_transformbuilder) . Use the [TransformBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_transformbuilder) to create your transforms

This class allows for the composition of multiple transformations through chaining.

Signature
```kotlin
class TransformStepBuilder(var value: Pose? = null, var root: TransformBuilder, var left: TransformBuilder.TransformStepBuilder? = null, var right: TransformBuilder.TransformStepBuilder? = null)
```

Constructors
| **TransformStepBuilder** ( value , root , left , right ) | Signature ```kotlin constructor(value: Pose? = null, root: TransformBuilder, left: TransformBuilder.TransformStepBuilder? = null, right: TransformBuilder.TransformStepBuilder? = null) ``` Parameters value: [Pose?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) root: [TransformBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_transformbuilder) left: TransformBuilder.TransformStepBuilder? right: TransformBuilder.TransformStepBuilder? Returns TransformBuilder.TransformStepBuilder |
| --- | --- |

Properties
| **left** : TransformBuilder.TransformStepBuilder? [Get][Set] | Signature ```kotlin var left: TransformBuilder.TransformStepBuilder? ``` |
| --- | --- |
| **right** : TransformBuilder.TransformStepBuilder? [Get][Set] | Signature ```kotlin var right: TransformBuilder.TransformStepBuilder? ``` |
| **root** : [TransformBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_transformbuilder) [Get][Set] | Signature ```kotlin var root: TransformBuilder ``` |
| **value** : [Pose?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) [Get][Set] | Signature ```kotlin var value: Pose? ``` |

Functions
| **build** () | Builds the final Pose from the transformation steps. Signature ```kotlin fun build(): Pose ``` Returns [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) A Pose object representing the composite transformation |
| --- | --- |
| **then** ( nextStep ) | Chains this transformation step with another transformation step. Signature ```kotlin infix fun then(nextStep: TransformBuilder.TransformStepBuilder): TransformBuilder.TransformStepBuilder ``` Parameters nextStep: TransformBuilder.TransformStepBuilder The next transformation step to apply Returns TransformBuilder.TransformStepBuilder A new TransformStepBuilder representing the combined transformation |