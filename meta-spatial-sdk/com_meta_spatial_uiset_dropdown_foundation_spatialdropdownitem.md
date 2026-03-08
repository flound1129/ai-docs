# SpatialDropdownItem Class

*Modifiers:
final*

Represents a single item in a dropdown menu.

## Signature

```kotlin
data class SpatialDropdownItem(val leading: () -> Unit? = null, val icon: () -> Unit? = null, val title: String? = null, val subtitle: String? = null, val enabled: Boolean = true, val suffix: () -> Unit? = null)
```

## Constructors

| **SpatialDropdownItem** ( leading , icon , title , subtitle , enabled , suffix ) | Signature ```kotlin constructor(leading: () -> Unit? = null, icon: () -> Unit? = null, title: String? = null, subtitle: String? = null, enabled: Boolean = true, suffix: () -> Unit? = null) ``` Parameters leading: Function0? A composable function that represents the leading icon or content of the item. icon: Function0? A composable function that represents the icon of the item. title: String? The title text of the item. subtitle: String? The subtitle text of the item. enabled: Boolean A boolean indicating whether the item is enabled or not. suffix: Function0? A composable function that represents the suffix of the item. Can be used to display a checkmark on selected items. Returns [SpatialDropdownItem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_uiset_dropdown_foundation_spatialdropdownitem) |
| --- | --- |

## Properties

| **enabled** : Boolean [Get] | Signature ```kotlin val enabled: Boolean = true ``` |
| --- | --- |
| **icon** : Function0? [Get] | Signature ```kotlin val icon: () -> Unit? = null ``` |
| **leading** : Function0? [Get] | Signature ```kotlin val leading: () -> Unit? = null ``` |
| **subtitle** : String? [Get] | Signature ```kotlin val subtitle: String? = null ``` |
| **suffix** : Function0? [Get] | Signature ```kotlin val suffix: () -> Unit? = null ``` |
| **title** : String? [Get] | Signature ```kotlin val title: String? = null ``` |