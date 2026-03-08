# PriorityGroup Enum

This enum represents the priority group a system belongs to. Systems will run in order of their priority groups, then within each group they will be sorted by their dependencies. Nothing runs between each priority group. mustRunBefore of a system must be run in either the same priority group or an earlier one mustRunAfter of a system must be run in either the same priority group or a later one

## Signature

```kotlin
enum PriorityGroup : Enum<PriorityGroup>
```

## Enumeration Constants

| Member |
| --- |
| EARLY |
| NORMAL |
| LATE |