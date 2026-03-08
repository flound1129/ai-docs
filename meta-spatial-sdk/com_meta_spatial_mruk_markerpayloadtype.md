# MarkerPayloadType Enum

Defines the types of payloads that can be contained in a tracked marker.

When tracking markers such as QR codes, this enum indicates the type of data contained within the marker or whether the marker could not be read.

## See Also

- [Tracker](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_tracker)

## Signature

```kotlin
enum MarkerPayloadType : Enum<MarkerPayloadType>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| InvalidQrCode | Indicates an invalid or unreadable QR code |
| StringQrCode | QR code containing string/text data |
| BinaryQrCode | QR code containing binary data |