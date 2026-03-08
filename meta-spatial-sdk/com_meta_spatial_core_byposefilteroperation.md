# ByPoseFilterOperation Class

*Modifiers:
final*

A class representing a filter operation for Pose attributes. It is used to build a filter expression by specifying comparison operations on Pose attribute values.

This class provides methods for creating filter nodes that represent various comparison operations on Pose attributes. It supports both:

- Comparing entire Pose values (all position and orientation components together) - Component-wise comparisons (filtering on just one component of position or orientation)

The component-wise filtering is enabled through the byPositionX/Y/Z() and byOrientationW/X/Y/Z() methods, which configure the filter to operate on a specific component of the Pose.

Example:

```kotlin // Find entities where poseVar equals Pose()
Query.where { has(TestComponent.id) }
    .filter { by(TestComponent.poseVar).isEqualTo(Pose()) }
// Find entities where poseVar's postition X is greater than 0.5f
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.poseVar).byPositionX().greaterThan(0.5f) }
// Find entities where poseVar's orientation W is between 0.0f and 1.0f
Query.where { has(TestComponent.id)}
     .filter { by(TestComponent.poseVar).byOrientationW().greaterThanOrEqualTo(0.0f) and
               by(TestComponent.poseVar).byOrientationW().lessThanOrEqualTo(1.0f) } ```

## Signature

```kotlin
class ByPoseFilterOperation(val attrId: Int, var propId: Int = 0, val filterBuilder: FilterBuilder)
```

## Constructors

| **ByPoseFilterOperation** ( attrId , propId , filterBuilder ) | Signature ```kotlin constructor(attrId: Int, propId: Int = 0, filterBuilder: FilterBuilder) ``` Parameters attrId: Int The attribute id of the filter operation. propId: Int The property id of the filter operation (0-2 for position x/y/z, 3-6 for orientation w/x/y/z). filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [ByPoseFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilteroperation) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **filterBuilder** : [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) [Get] | Signature ```kotlin val filterBuilder: FilterBuilder ``` |
| **propId** : Int [Get][Set] | Signature ```kotlin var propId: Int ``` |

## Functions

| **byOrientationW** () | Sets the filter to operate on the W component of the Pose's orientation quaternion. Signature ```kotlin fun byOrientationW(): ByPoseFilterOperation ``` Returns [ByPoseFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilteroperation) This filter operation configured to filter on the orientation's W component. |
| --- | --- |
| **byOrientationX** () | Sets the filter to operate on the X component of the Pose's orientation quaternion. Signature ```kotlin fun byOrientationX(): ByPoseFilterOperation ``` Returns [ByPoseFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilteroperation) This filter operation configured to filter on the orientation's X component. |
| **byOrientationY** () | Sets the filter to operate on the Y component of the Pose's orientation quaternion. Signature ```kotlin fun byOrientationY(): ByPoseFilterOperation ``` Returns [ByPoseFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilteroperation) This filter operation configured to filter on the orientation's Y component. |
| **byOrientationZ** () | Sets the filter to operate on the Z component of the Pose's orientation quaternion. Signature ```kotlin fun byOrientationZ(): ByPoseFilterOperation ``` Returns [ByPoseFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilteroperation) This filter operation configured to filter on the orientation's Z component. |
| **byPositionX** () | Sets the filter to operate on the X component of the Pose's position. Signature ```kotlin fun byPositionX(): ByPoseFilterOperation ``` Returns [ByPoseFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilteroperation) This filter operation configured to filter on the position's X component. |
| **byPositionY** () | Sets the filter to operate on the Y component of the Pose's position. Signature ```kotlin fun byPositionY(): ByPoseFilterOperation ``` Returns [ByPoseFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilteroperation) This filter operation configured to filter on the position's Y component. |
| **byPositionZ** () | Sets the filter to operate on the Z component of the Pose's position. Signature ```kotlin fun byPositionZ(): ByPoseFilterOperation ``` Returns [ByPoseFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilteroperation) This filter operation configured to filter on the position's Z component. |
| **greaterThan** ( value ) | Creates a filter node representing a greater than condition with the given float value. This compares only the component specified by propId (position X/Y/Z or orientation W/X/Y/Z). By default, the filter operates on the position's X component. Signature ```kotlin fun greaterThan(value: Float): ByPoseFilterNode ``` Parameters value: Float The float value to compare against. Returns [ByPoseFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilternode) A filter node representing the greater than condition. |
| **greaterThanOrEqualTo** ( value ) | Creates a filter node representing a greater than or equal to condition with the given float value. This compares only the component specified by propId (position X/Y/Z or orientation W/X/Y/Z). By default, the filter operates on the position's X component. Signature ```kotlin fun greaterThanOrEqualTo(value: Float): ByPoseFilterNode ``` Parameters value: Float The float value to compare against. Returns [ByPoseFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilternode) A filter node representing the greater than or equal to condition. |
| **isEqualTo** ( value ) | Creates a filter node representing an equality condition with the given Pose value. This compares all position (x, y, z) and orientation (w, x, y, z) components of the pose. Signature ```kotlin fun isEqualTo(value: Pose): ByPoseFilterNode ``` Parameters value: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) The Pose value to compare against. Returns [ByPoseFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilternode) A filter node representing the equality condition. |
| **isEqualTo** ( value ) | Creates a filter node representing an equality condition with the given float value. This compares only the component specified by propId (position X/Y/Z or orientation W/X/Y/Z). By default, the filter operates on the position's X component. Signature ```kotlin fun isEqualTo(value: Float): ByPoseFilterNode ``` Parameters value: Float The float value to compare against. Returns [ByPoseFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilternode) A filter node representing the equality condition. |
| **lessThan** ( value ) | Creates a filter node representing a less than condition with the given float value. This compares only the component specified by propId (position X/Y/Z or orientation W/X/Y/Z). By default, the filter operates on the position's X component. Signature ```kotlin fun lessThan(value: Float): ByPoseFilterNode ``` Parameters value: Float The float value to compare against. Returns [ByPoseFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilternode) A filter node representing the less than condition. |
| **lessThanOrEqualTo** ( value ) | Creates a filter node representing a less than or equal to condition with the given float value. This compares only the component specified by propId (position X/Y/Z or orientation W/X/Y/Z). By default, the filter operates on the position's X component. Signature ```kotlin fun lessThanOrEqualTo(value: Float): ByPoseFilterNode ``` Parameters value: Float The float value to compare against. Returns [ByPoseFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilternode) A filter node representing the less than or equal to condition. |