# GrabbableType Enum

GrabbableType is an enum that defines the type of behavior an object has when grabbed.

## Signature

```kotlin
enum GrabbableType : Enum<GrabbableType>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| FACE | The object faces the user when grabbed. |
| PIVOT_Y | The object rotates around the Y axis to face the user (will not look up or down). |