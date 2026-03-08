# ReferenceSpace Enum

Reference spaces determine how positions and orientations are interpreted relative to the user and physical environment. Each space has different behavior when the user recenters their view or moves around in the physical world.

Example: Setting ReferenceSpace to LOCAL_FLOOR to enable recentering:

```kotlin scene.setReferenceSpace(ReferenceSpace.LOCAL_FLOOR) ```

## Signature

```kotlin
enum ReferenceSpace : Enum<ReferenceSpace>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| UNKNOWN | Represents invalid reference space. Do not use. |
| VIEW | Space that is relative to the view (headset). Objects in this space maintain a fixed position relative to the user's head, regardless of how they move or recenter. This is ideal for UI elements that should always remain in the user's field of view, such as HUD elements. |
| LOCAL | Space that is relative to an arbitrary origin. When the user recenters their view, the origin is updated to the latest headset position. This creates a new reference point for all objects in this space. |
| STAGE | World space that remains fixed regardless of user movement. Recentering doesn't affect positions in this space since it's anchored to the physical world. This is the recommended space for Mixed Reality applications where virtual objects need to maintain consistent positions relative to the real environment. |
| LOCAL_FLOOR | Similar to LOCAL but takes into account the user's height. When recentering, this space updates the origin to the latest headset position while maintaining the correct relationship to the floor. This is the recommended space for Virtual Reality applications where floor-relative positioning is important. |
| RAW |  |

## Properties

| **space** : Int [Get] | Integer value corresponding to the native reference space type Signature ```kotlin val space: Int ``` |
| --- | --- |