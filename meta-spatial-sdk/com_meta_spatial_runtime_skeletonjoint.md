# SkeletonJoint Class

*Modifiers:
final*

## Signature

```kotlin
data class SkeletonJoint(val jointIndex: Int, val parentJointIndex: Int, val pose: Pose)
```

## Constructors

| **SkeletonJoint** ( jointIndex , parentJointIndex , pose ) | Signature ```kotlin constructor(jointIndex: Int, parentJointIndex: Int, pose: Pose) ``` Parameters jointIndex: Int parentJointIndex: Int pose: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) Returns [SkeletonJoint](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_skeletonjoint) |
| --- | --- |

## Properties

| **jointIndex** : Int [Get] | Signature ```kotlin val jointIndex: Int ``` |
| --- | --- |
| **parentJointIndex** : Int [Get] | Signature ```kotlin val parentJointIndex: Int ``` |
| **pose** : [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) [Get] | Signature ```kotlin val pose: Pose ``` |