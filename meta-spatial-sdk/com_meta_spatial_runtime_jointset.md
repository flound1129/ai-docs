# JointSet Enum

JointSet selects which body joint topology the body tracking system should provide.

## Signature

```kotlin
enum JointSet : Enum<JointSet>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| DEFAULT | Provides the default joint set supported by the device/runtime (typically upper body and hands where available). |
| FULL_BODY | Requests the full-body joint set (head, spine, arms, hands, hips, legs, and feet). This requires the OpenXR extension XR_META_body_tracking_full_body to be enabled on the device/runtime. |

## Properties

| **index** : Int [Get] | Signature ```kotlin val index: Int ``` |
| --- | --- |