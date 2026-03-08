# ControllerButton Enum

Represents the various buttons and touch inputs on VR controllers.

This enum is commonly used with button event arguments classes like ButtonDownEventArgs and ButtonReleaseEventArgs to identify which specific button triggered an event.

Example usage:

```kotlin // Handle button press events based on which button was pressed
entity.registerEventListener<ButtonDownEventArgs>(ButtonDownEventArgs.EVENT_NAME) { _, eventArgs ->
    when (eventArgs.button) {
        ControllerButton.A -> handleAButtonPress()
        ControllerButton.LeftTrigger -> handleLeftTriggerPress()
        ControllerButton.RightThumbUp -> handleRightThumbstickUp()
        // Handle other buttons...
    }
} ```

## Signature

```kotlin
enum ControllerButton : Enum<ControllerButton>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| A | Right controller "A" button |
| B | Right controller "B" button |
| X | Left controller "X" button |
| Y | Left controller "Y" button |
| RightTrigger | Right controller trigger button (index finger) |
| LeftTrigger | Left controller trigger button (index finger) |
| RightSqueeze | Right controller grip/squeeze button (middle finger) |
| LeftSqueeze | Left controller grip/squeeze button (middle finger) |
| LeftThumbLeft | Left thumbstick pushed left |
| LeftThumbRight | Left thumbstick pushed right |
| RightThumbLeft | Right thumbstick pushed left |
| RightThumbRight | Right thumbstick pushed right |
| LeftThumbUp | Left thumbstick pushed up |
| LeftThumbDown | Left thumbstick pushed down |
| RightThumbUp | Right thumbstick pushed up |
| RightThumbDown | Right thumbstick pushed down |
| LeftThumbClick | Left thumbstick click (pressed in) |
| RightThumbClick | Right thumbstick click (pressed in) |
| LeftThumbTouch | Left thumbstick touch (finger detected on thumbstick) |
| RightThumbTouch | Right thumbstick touch (finger detected on thumbstick) |
| ATouch | A button touch (finger detected on button) |
| BTouch | B button touch (finger detected on button) |
| XTouch | X button touch (finger detected on button) |
| YTouch | Y button touch (finger detected on button) |
| LeftTriggerTouch | Left trigger touch (finger detected on trigger) |
| RightTriggerTouch | Right trigger touch (finger detected on trigger) |
| LeftThumbRest | Left thumbstick rest state (finger resting on thumbstick) |
| RightThumbRest | Right thumbstick rest state (finger resting on thumbstick) |
| MenuButton | Menu button (typically on left controller) |
| SystemButton | System button (typically on right controller) |