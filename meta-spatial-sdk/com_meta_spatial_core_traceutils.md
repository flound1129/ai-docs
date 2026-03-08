# TraceUtils Object

TraceUtils are used to perform traces on code and do performance optimization. You can utilize Perfetto to analyze the traces.

forceEnabled is set to false by default. If you want to enable tracing, set it to true.

Example usage:

```kotlin TraceUtils.forceEnabled = true
TraceUtils.trace("myTrace") {
  // do something
} ```

## Signature

```kotlin
object TraceUtils
```

## Properties

| **cookie** : Int [Get][Set] | Signature ```kotlin var cookie: Int ``` |
| --- | --- |
| **forceEnabled** : Boolean [Get][Set] | Signature ```kotlin var forceEnabled: Boolean ``` |

## Functions

| **beginAsyncSection** ( sectionName ) | Begin an async trace section. You will need to call endAsyncSection() to end the current trace section. ```kotlin val id = TraceUtils.beginAsyncSection("myTrace") // do something TraceUtils.endAsyncSection("myTrace", id) ``` Signature ```kotlin fun beginAsyncSection(sectionName: String): Int ``` Parameters sectionName: String The name of the trace section. Returns Int |
| --- | --- |
| **beginSection** ( sectionName ) | Begin a trace section. You will need to call endSection() to end the current trace section. You can nest trace sections. ```kotlin TraceUtils.beginSection("myTrace") // do something TraceUtils.beginSection("myNestedTrace") // do something else TraceUtils.endSection() // end myNestedTrace // do other stuff TraceUtils.endSection() // end myTrace ``` Signature ```kotlin fun beginSection(sectionName: String) ``` Parameters sectionName: String The name of the trace section. |
| **endAsyncSection** ( sectionName , id ) | End an async trace section. Make sure you have called a beginAsyncSection() before calling this with the same id. ```kotlin val id = TraceUtils.beginAsyncSection("myTrace") // do something TraceUtils.endAsyncSection("myTrace", id) ``` Signature ```kotlin fun endAsyncSection(sectionName: String, id: Int) ``` Parameters sectionName: String The name of the trace section. id: Int The id of the trace section that you retrieved from beginAsyncSection(). |
| **endSection** () | End the current trace section. Make sure you have called a beginSection() before calling this. You are responsible for managing your trace sections. ```kotlin TraceUtils.beginSection("myTrace") // do something TraceUtils.endSection() // end myTrace ``` Signature ```kotlin fun endSection() ``` |
| **trace** ( sectionName , block ) | This method is a convenience method that handles the beginSection() and endSection() for you. It will run the block of code within the trace section. ```kotlin TraceUtils.trace("myTrace") { // do something } ``` Signature ```kotlin inline fun trace(sectionName: String, block: () -> Unit) ``` Parameters sectionName: String The name of the trace section. block: Function0 The block of code to run within the trace section. |
| **traceAsync** ( sectionName , block ) | This method is a convenience method that handles the beginAsyncSection() and endAsyncSection() for you. It will run the block of code within the trace section. ```kotlin TraceUtils.traceAsync("myTrace") { // do something } ``` Signature ```kotlin inline fun traceAsync(sectionName: String, block: () -> Unit) ``` Parameters sectionName: String The name of the trace section. block: Function0 The block of code to run within the trace section. |