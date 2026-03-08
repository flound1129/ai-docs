# SpatialTextField Function

*Modifiers:
final*

Use text fields to input text into the system. Text fields show a preview of the text before submission and can be single or multi-line, depending on the information needed. When you select a text field, the keyboard appears in front of the user. Partially opaque “hint” text may be present to prompt the user for specific information, such as email or password. Text fields may be paired with the assistance of chip-selections to help speed up productivity of the user’s intention, or a microphone button to prompt users to enter text via dictation.

## Parameters

value:
String
The current text value.
label:
String
The label for the text field.
onValueChange:
Function1
Callback to be invoked when the text value changes.
modifier:
Modifier
Optional Modifier for styling.
onSubmit:
Function1?
Optional callback to be invoked when the user submits the text.
validationPredicate:
Function1?
Optional predicate to validate the input asynchronously.
initialState:
[FieldValidationState](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_input_foundation_fieldvalidationstate)
Initial validation state of the text field.
placeholder:
String?
Optional placeholder text.
helperText:
String?
Optional helper text displayed below the text field.
enabled:
Boolean
Whether the text field is enabled or not.
leadingIcon:
Function0?
Optional leading icon displayed before the text input.
trailingIcon:
Function0?
Optional trailing icon displayed after the text input.
singleLine:
Boolean
Whether to restrict the input to a single line or not.
autoValidate:
Boolean
Whether to automatically validate the input or not.
autoCorrectEnabled:
Boolean
Whether to enable auto-correction or not.
capitalization:
KeyboardCapitalization
The capitalization style for the keyboard input.
keyboardType:
KeyboardType
The type of keyboard to display for input.
interactionSource:
MutableInteractionSource