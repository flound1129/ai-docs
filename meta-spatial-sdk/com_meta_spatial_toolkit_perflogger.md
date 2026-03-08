# PerfLogger Object

Utility for measuring and tracking execution times of operations in the code.

PerfLogger provides a simple way to measure how long different operations take to execute. It stores timing information in a HashMap where the key is a string identifier for the operation and the value is a Pair containing the start and end times in milliseconds since system boot.

This logger is useful for performance profiling and identifying bottlenecks in your application.

Example usage:

```kotlin // Start timing an operation
PerfLogger.startTiming("LoadMesh")
// Perform the operation
val mesh = loadMeshFromFile(file)
// End timing the operation
PerfLogger.endTiming("LoadMesh")
// Later, you can access the timing information
val timingPair = PerfLogger.timings["LoadMesh"]
val startTime = timingPair?.first
val endTime = timingPair?.second
val elapsedTime = if (startTime != null && endTime != null) endTime - startTime else null
println("Loading mesh took ${elapsedTime}ms") ```

## Signature

```kotlin
object PerfLogger
```

## Properties

| **timings** : HashMap<String, Pair<Long, Long>> [Get][Set] | HashMap storing timing information for different operations. The key is a string identifier for the operation being timed. The value is a Pair where: - first: start time in milliseconds (from SystemClock.elapsedRealtime()) - second: end time in milliseconds (from SystemClock.elapsedRealtime()), or 0 if timing hasn't ended Signature ```kotlin var timings: HashMap<String, Pair<Long, Long>> ``` |
| --- | --- |

## Functions

| **endTiming** ( beingTimed ) | Ends timing for an operation and records the elapsed time. This method records the current system time as the end time for the specified operation. If no timing was started for this operation, this method has no effect. Signature ```kotlin fun endTiming(beingTimed: String) ``` Parameters beingTimed: String A string identifier for the operation being timed |
| --- | --- |
| **startTiming** ( beingTimed ) | Starts timing an operation identified by the given string. This method records the current system time as the start time for the specified operation. If timing for this operation already exists, it will be overwritten. Signature ```kotlin fun startTiming(beingTimed: String) ``` Parameters beingTimed: String A string identifier for the operation being timed |