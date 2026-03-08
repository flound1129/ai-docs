# Tracker Enum

Defines the types of real-world objects that can be tracked in the environment.

Tracker types are used to configure which objects the system should detect and track. Multiple trackers can be enabled simultaneously by passing a set of tracker types to configureTrackers().

## See Also

## Signature

```kotlin
enum Tracker : Enum<Tracker>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| Keyboard | Physical keyboard tracking |
| QrCode | QR code marker tracking |