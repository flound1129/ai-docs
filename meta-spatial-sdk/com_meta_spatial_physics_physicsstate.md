# PhysicsState Enum

PhysicsState defines the type of physics simulation applied to an object.

## Signature

```kotlin
enum PhysicsState : Enum<PhysicsState>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| STATIC | The object does not move and is not affected by forces. Use for immovable objects like walls or floors. |
| DYNAMIC | The object moves and is affected by forces and gravity. Use for objects that should have realistic physics behavior and don't have their Transform affected by outside forces. |
| KINEMATIC | The object can be moved programmatically but is not affected by forces or gravity. Use for objects that need to be moved by Spatial SDK systems instead of physics simulation. |