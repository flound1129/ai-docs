# SessionState Enum

Enum representing OpenXR session states.

These states represent the lifecycle of an XR session and determine what operations are valid at any given time. Session states follow the OpenXR specification and provide detailed information about the current state of the XR runtime.

The typical session lifecycle progresses as: UNKNOWN -> IDLE -> READY -> SYNCHRONIZED -> VISIBLE -> FOCUSED

And during shutdown: FOCUSED -> VISIBLE -> SYNCHRONIZED -> STOPPING -> IDLE -> EXITING

## Signature

```kotlin
enum SessionState : Enum<SessionState>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| UNKNOWN | Initial unknown state. This is the default state before the session is properly initialized. |
| IDLE | Session is idle and not ready to render. The runtime is not presenting frames to the display. This is typically the state when the session is first created or after it has stopped. |
| READY | Session is ready to begin. The application may call xrBeginSession at this point to transition to rendering states. |
| SYNCHRONIZED | Session is synchronized with the runtime. The session has begun and the runtime is preparing to present frames, but they may not yet be visible to the user. |
| VISIBLE | Session is visible but may not have input focus. The application's content is visible to the user but the application may not be receiving input. |
| FOCUSED | Session has input focus and is fully active. This is the primary running state where the application should be rendering frames and processing input. |
| STOPPING | Session is stopping. The runtime has requested that the application stop rendering. The application should call xrEndSession. |
| EXITING | Session is exiting. The session is in the process of terminating and will soon be destroyed. |
| LOSS_PENDING | Session loss is pending. The runtime has encountered an issue and the session will soon be lost. The application should prepare for the session to be destroyed. |

## Properties

| **value** : Int [Get] | Integer value corresponding to the native XrSessionState Signature ```kotlin val value: Int ``` |
| --- | --- |

## Companion Object

### Companion Object Functions

| **fromValue** ( value ) | Converts an integer value to its corresponding SessionState enum. Signature ```kotlin fun fromValue(value: Int): SessionState ``` Parameters value: Int The integer value from native code Returns [SessionState](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sessionstate) The corresponding SessionState, or UNKNOWN if not found |
| --- | --- |