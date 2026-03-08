# MicrogestureBits Object

Defines bit flags for microgesture input states.

MicrogestureBits provides constants for individual hand microgestures, as well as predefined masks for common microgesture combinations. Each microgesture is represented by a specific bit position, allowing multiple microgesture states to be combined using bitwise operations.

These constants are used for detecting specific microgesture combinations for custom interactions

Example usage:

```kotlin val microgestures = entity.getComponent<Microgestures>()
val changedMicrogestures = microgestures.changedMicrogestures
val microgestureState = microgestures.microgestureState
val microgesturesPressed = microgestureState and changedMicrogestures
val microgesturesReleased = microgestureState.inv() and changedMicrogestures
if (microgesturesPressed and MicrogestureBits.LeftMicrogestureSwipeLeft != 0) {
  // Left hand swipe left microgesture detected
} ```

## Signature

```kotlin
object MicrogestureBits
```

## Properties

| **AllMicrogesturesMask** : Int [Get] | Comprehensive mask for all microgestures from both hands. Combines left and right microgesture masks. Signature ```kotlin val AllMicrogesturesMask: Int ``` |
| --- | --- |
| **LeftMicrogestures** : Int [Get] | Mask for all left hand microgestures. Includes swipe left, swipe right, swipe forward, swipe back, and tap thumb. Signature ```kotlin val LeftMicrogestures: Int ``` |
| **LeftMicrogestureSwipeBack** : Int [Get] | Left hand swipe back microgesture Signature ```kotlin val LeftMicrogestureSwipeBack: Int ``` |
| **LeftMicrogestureSwipeForward** : Int [Get] | Left hand swipe forward microgesture Signature ```kotlin val LeftMicrogestureSwipeForward: Int ``` |
| **LeftMicrogestureSwipeLeft** : Int [Get] | Left hand swipe left microgesture Signature ```kotlin val LeftMicrogestureSwipeLeft: Int ``` |
| **LeftMicrogestureSwipeRight** : Int [Get] | Left hand swipe right microgesture Signature ```kotlin val LeftMicrogestureSwipeRight: Int ``` |
| **LeftMicrogestureTapThumb** : Int [Get] | Left hand tap thumb microgesture Signature ```kotlin val LeftMicrogestureTapThumb: Int ``` |
| **RightMicrogestures** : Int [Get] | Mask for all right hand microgestures. Includes swipe left, swipe right, swipe forward, swipe back, and tap thumb. Signature ```kotlin val RightMicrogestures: Int ``` |
| **RightMicrogestureSwipeBack** : Int [Get] | Right hand swipe back microgesture Signature ```kotlin val RightMicrogestureSwipeBack: Int ``` |
| **RightMicrogestureSwipeForward** : Int [Get] | Right hand swipe forward microgesture Signature ```kotlin val RightMicrogestureSwipeForward: Int ``` |
| **RightMicrogestureSwipeLeft** : Int [Get] | Right hand swipe left microgesture Signature ```kotlin val RightMicrogestureSwipeLeft: Int ``` |
| **RightMicrogestureSwipeRight** : Int [Get] | Right hand swipe right microgesture Signature ```kotlin val RightMicrogestureSwipeRight: Int ``` |
| **RightMicrogestureTapThumb** : Int [Get] | Right hand tap thumb microgesture Signature ```kotlin val RightMicrogestureTapThumb: Int ``` |