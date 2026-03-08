# IsdkGrabMovementType Enum

IsdkGrabMovementType is an enum that defines the type of movement allowed for a grabbable object.

## Signature

```kotlin
enum IsdkGrabMovementType : Enum<IsdkGrabMovementType>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| Direct | The object moves directly with the grabber. |
| Billboard | The object faces the user when grabbed. |
| AxialBillboard | The object faces the user but does not pitch up and down (i.e. stays on the vertical axis) |
| None | The object will not move when grabbed (but will still emit pointer events). Use this if you want to implement your own grab transform logic. |