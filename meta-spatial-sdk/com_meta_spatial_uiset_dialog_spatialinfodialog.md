# SpatialInfoDialog Function

*Modifiers:
final*

Displays a spatial dialog with an info banner, title, description, and action buttons.

## Signature

```kotlin
fun SpatialInfoDialog(title: String, description: String, infoBannerIcon: () -> Unit, infoBannerText: String, primaryChoiceActionLabel: String, onPrimaryChoiceActionClick: () -> Unit, secondaryChoiceActionLabel: String? = null, onSecondaryChoiceActionClick: () -> Unit? = null, tertiaryChoiceActionLabel: String? = null, onTertiaryChoiceActionClick: () -> Unit? = null, leading: () -> Unit? = null, trailing: () -> Unit? = null)
```

## Parameters

title:
String
The title of the dialog.
description:
String
The description of the dialog.
infoBannerIcon:
Function0
A composable function that provides the icon to display in the info banner.
infoBannerText:
String
The text to display in the info banner.
primaryChoiceActionLabel:
String
The label for the primary action button.
onPrimaryChoiceActionClick:
Function0
The callback to invoke when the primary action button is clicked.
secondaryChoiceActionLabel:
String?
The label for the secondary action button (optional).
onSecondaryChoiceActionClick:
Function0?
The callback to invoke when the secondary action button is clicked (optional).
tertiaryChoiceActionLabel:
String?
The label for the tertiary action button (optional).
onTertiaryChoiceActionClick:
Function0?
The callback to invoke when the tertiary action button is clicked (optional).
leading:
Function0?
An optional composable to display as leading content.
trailing:
Function0?
An optional composable to display as trailing content.