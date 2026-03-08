# SpatialSearchBar Function

*Modifiers:
final*

A search bar component that allows users to input a query and submit it.

## Signature

```kotlin
fun SpatialSearchBar(modifier: Modifier, query: String = "", placeholder: String = "Search", enableAudio: Boolean = false, onQueryChange: (String) -> Unit, onQuerySubmit: (String) -> Unit, enabled: Boolean = true, autoCorrectEnabled: Boolean = false, capitalization: KeyboardCapitalization, keyboardType: KeyboardType, interactionSource: MutableInteractionSource) })
```

## Parameters

modifier:
Modifier
Modifier to be applied to the search bar.
query:
String
The current text in the search bar.
placeholder:
String
Placeholder text when the search bar is empty.
enableAudio:
Boolean
Whether to show an audio input button.
onQueryChange:
Function1
Callback invoked when the query changes.
onQuerySubmit:
Function1
Callback invoked when the query is submitted.
enabled:
Boolean
Whether the search bar is enabled or not.
autoCorrectEnabled:
Boolean
Whether auto-correction is enabled for the text input.
capitalization:
KeyboardCapitalization
The capitalization option for the text input.
keyboardType:
KeyboardType
The keyboard type for the text input.
interactionSource:
MutableInteractionSource