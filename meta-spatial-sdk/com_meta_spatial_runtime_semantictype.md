# SemanticType Enum

Enum class representing different semantic types for pointer events.

These identify the intention of the event. For example: "Select" indicates a user attempted to select this entity. "Grab" indicates the user attempted to grab this entity. "Scroll" is sent when a user scrolls using an alternate method like thumb-stick.

## Signature

```kotlin
enum SemanticType : Enum<SemanticType>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| Unknown | Smantic type was unspecified. |
| None | No emantic type was set for this interaction. |
| Select | This entity was selected (e.g. a mouse left click-down). |
| Grab | This entity was grabbed (e.g. user is holding the grip button. |
| Scroll | This entity should be scrolled (e.g. user pressed thumbstick up on a panel. |

## Properties

| **id** : Int [Get] | Signature ```kotlin val id: Int ``` |
| --- | --- |