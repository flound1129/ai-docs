# ButtonBits Object

Defines bit flags for controller buttons and input states.

ButtonBits provides constants for individual controller buttons and button states, as well as predefined masks for common button combinations. Each button is represented by a specific bit position, allowing multiple button states to be combined using bitwise operations.

These constants are used for input handling, including:

- Defining which buttons can trigger interactions with panels and UI elements - Configuring grab buttons for the GrabbableSystem - Filtering and processing input events in Scene and InputListener implementations - Detecting specific button combinations for custom interactions

Example usage:

```kotlin // Check if a specific button is pressed
if (buttonState and ButtonBits.ButtonA != 0) {
  // Button A is pressed
}
// Configure grab buttons for GrabbableSystem
systemManager.findSystem<GrabbableSystem>().grabButtons =
  ButtonBits.ButtonSqueezeR or ButtonBits.ButtonSqueezeL or ButtonBits.ButtonX
// Define custom click buttons for a panel
clickButtons = ButtonBits.ButtonA or ButtonBits.ButtonTriggerL or ButtonBits.ButtonTriggerR ```

## Signature

```kotlin
object ButtonBits
```

## Properties

| **AllButtonClickMask** : Int [Get] | Mask for all clickable buttons on both controllers. Combines left and right click button masks. Signature ```kotlin val AllButtonClickMask: Int ``` |
| --- | --- |
| **AllButtonMask** : Int [Get] | Comprehensive mask for all buttons and inputs on both controllers. Combines left and right button masks. Signature ```kotlin val AllButtonMask: Int ``` |
| **ButtonA** : Int [Get] | Right controller A button Signature ```kotlin val ButtonA: Int ``` |
| **ButtonATouch** : Int [Get] | A button touch (finger detected on button) Signature ```kotlin val ButtonATouch: Int ``` |
| **ButtonB** : Int [Get] | Right controller B button Signature ```kotlin val ButtonB: Int ``` |
| **ButtonBTouch** : Int [Get] | B button touch (finger detected on button) Signature ```kotlin val ButtonBTouch: Int ``` |
| **ButtonMenu** : Int [Get] | Menu button (typically on left controller) Signature ```kotlin val ButtonMenu: Int ``` |
| **ButtonSqueezeL** : Int [Get] | Left controller squeeze/grip button Signature ```kotlin val ButtonSqueezeL: Int ``` |
| **ButtonSqueezeR** : Int [Get] | Right controller squeeze/grip button Signature ```kotlin val ButtonSqueezeR: Int ``` |
| **ButtonSystem** : Int [Get] | System button (typically on right controller) Signature ```kotlin val ButtonSystem: Int ``` |
| **ButtonThumbLClick** : Int [Get] | Left thumbstick click (pressed in) Signature ```kotlin val ButtonThumbLClick: Int ``` |
| **ButtonThumbLD** : Int [Get] | Left thumbstick pushed down Signature ```kotlin val ButtonThumbLD: Int ``` |
| **ButtonThumbLL** : Int [Get] | Left thumbstick pushed left Signature ```kotlin val ButtonThumbLL: Int ``` |
| **ButtonThumbLR** : Int [Get] | Left thumbstick pushed right Signature ```kotlin val ButtonThumbLR: Int ``` |
| **ButtonThumbLRest** : Int [Get] | Left thumbstick rest state (finger resting on thumbstick) Signature ```kotlin val ButtonThumbLRest: Int ``` |
| **ButtonThumbLTouch** : Int [Get] | Left thumbstick touch (finger detected on thumbstick) Signature ```kotlin val ButtonThumbLTouch: Int ``` |
| **ButtonThumbLU** : Int [Get] | Left thumbstick pushed up Signature ```kotlin val ButtonThumbLU: Int ``` |
| **ButtonThumbRClick** : Int [Get] | Right thumbstick click (pressed in) Signature ```kotlin val ButtonThumbRClick: Int ``` |
| **ButtonThumbRD** : Int [Get] | Right thumbstick pushed down Signature ```kotlin val ButtonThumbRD: Int ``` |
| **ButtonThumbRL** : Int [Get] | Right thumbstick pushed left Signature ```kotlin val ButtonThumbRL: Int ``` |
| **ButtonThumbRR** : Int [Get] | Right thumbstick pushed right Signature ```kotlin val ButtonThumbRR: Int ``` |
| **ButtonThumbRRest** : Int [Get] | Right thumbstick rest state (finger resting on thumbstick) Signature ```kotlin val ButtonThumbRRest: Int ``` |
| **ButtonThumbRTouch** : Int [Get] | Right thumbstick touch (finger detected on thumbstick) Signature ```kotlin val ButtonThumbRTouch: Int ``` |
| **ButtonThumbRU** : Int [Get] | Right thumbstick pushed up Signature ```kotlin val ButtonThumbRU: Int ``` |
| **ButtonTriggerL** : Int [Get] | Left controller trigger button Signature ```kotlin val ButtonTriggerL: Int ``` |
| **ButtonTriggerLTouch** : Int [Get] | Left trigger touch (finger detected on trigger) Signature ```kotlin val ButtonTriggerLTouch: Int ``` |
| **ButtonTriggerR** : Int [Get] | Right controller trigger button Signature ```kotlin val ButtonTriggerR: Int ``` |
| **ButtonTriggerRTouch** : Int [Get] | Right trigger touch (finger detected on trigger) Signature ```kotlin val ButtonTriggerRTouch: Int ``` |
| **ButtonX** : Int [Get] | Left controller X button Signature ```kotlin val ButtonX: Int ``` |
| **ButtonXTouch** : Int [Get] | X button touch (finger detected on button) Signature ```kotlin val ButtonXTouch: Int ``` |
| **ButtonY** : Int [Get] | Left controller Y button Signature ```kotlin val ButtonY: Int ``` |
| **ButtonYTouch** : Int [Get] | Y button touch (finger detected on button) Signature ```kotlin val ButtonYTouch: Int ``` |
| **LeftButtonClickMask** : Int [Get] | Mask for all click buttons on the left controller. Includes X, Y, left trigger, left thumbstick click, and left squeeze buttons. Signature ```kotlin val LeftButtonClickMask: Int ``` |
| **LeftButtonMask** : Int [Get] | Comprehensive mask for all left controller buttons and inputs. Combines click buttons, touch buttons, thumbstick motion, and menu button. Signature ```kotlin val LeftButtonMask: Int ``` |
| **LeftButtonTouchMask** : Int [Get] | Mask for all touch buttons on the left controller. Includes left thumbstick touch, X touch, Y touch, and left trigger touch. Signature ```kotlin val LeftButtonTouchMask: Int ``` |
| **LeftThumbMotionMask** : Int [Get] | Mask for all left thumbstick directional inputs and rest state. Includes left, right, up, down, and rest positions. Signature ```kotlin val LeftThumbMotionMask: Int ``` |
| **RightButtonClickMask** : Int [Get] | Mask for all click buttons on the right controller. Includes A, B, right trigger, right thumbstick click, and right squeeze buttons. Signature ```kotlin val RightButtonClickMask: Int ``` |
| **RightButtonMask** : Int [Get] | Comprehensive mask for all right controller buttons and inputs. Combines click buttons, touch buttons, thumbstick motion, and system button. Signature ```kotlin val RightButtonMask: Int ``` |
| **RightButtonTouchMask** : Int [Get] | Mask for all touch buttons on the right controller. Includes right thumbstick touch, A touch, B touch, and right trigger touch. Signature ```kotlin val RightButtonTouchMask: Int ``` |
| **RightThumbMotionMask** : Int [Get] | Mask for all right thumbstick directional inputs and rest state. Includes left, right, up, down, and rest positions. Signature ```kotlin val RightThumbMotionMask: Int ``` |