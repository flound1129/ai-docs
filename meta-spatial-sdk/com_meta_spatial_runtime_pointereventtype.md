# PointerEventType Enum

Enum class representing different types of pointer events.

A PointerEvent represents some activity on an entity. This enum classifies the nature of the action taken. For example when we start hovering an entity we get a "Hover" type of event.

Notice we do not know if the intent of the user. E.g. is this to grab or select or teleport. See the SemanticType enum for the intent of the interaction.

## Signature

```kotlin
enum PointerEventType : Enum<PointerEventType>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| Hover | Event triggered when the pointer starts hovering over an entity. |
| Unhover | Event triggered when the pointer stops hovering over an entity. |
| Select | Event triggered when the pointer initially selects an entity (i.e. click-down). |
| Unselect | Event triggered when the pointer stops selecting an entity (i.e. click-up). |
| Move | Event triggered every frame while hovering or selecting an entity. |
| Cancel | Event triggered when the pointer event is cancelled (e.g. poke too far through a panel). |

## Properties

| **id** : Int [Get] | Signature ```kotlin val id: Int ``` |
| --- | --- |