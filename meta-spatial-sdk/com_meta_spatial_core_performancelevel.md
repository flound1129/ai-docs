# PerformanceLevel Enum

Performance level options. More info: [https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#ext_performance_settings-level-definition](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#ext_performance_settings-level-definition)

## Signature

```kotlin
enum PerformanceLevel : Enum<PerformanceLevel>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| SUSTAINED_LOW |  |
| SUSTAINED_HIGH |  |
| BOOST_HINT | Send a hint to boost to maximum performance. This is not a guarantee and the system reserves the right to ignore this request. This can only boost for a maximum of 45s and has required cooldown periods in between usage. |

## Properties

| **value** : Int [Get] | Signature ```kotlin val value: Int ``` |
| --- | --- |