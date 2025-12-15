# MAC Address to Binary Converter

This Python script allows you to **validate a MAC address** and **convert it from hexadecimal to binary representation**.  
It supports several common input formats and returns both a compact binary version and an octet-split version.

## Requirements

- Python 3.x
- Standard module `re`

## Feature

- Verify the correctness of the format of a MAC address
- Supports major MAC address formats:
  - `AA:BB:CC:DD:EE:FF`
  - `AA-BB-CC-DD-EE-FF`
  - `AABB.CCDD.EEFF`
  - `AABBCCDDEEFF`
- Converts each hexadecimal octet to binary (8 bits)
- Print:
  - Binary version separated by `:`
  - Compact binary version (48 bit)

## Description

#### check_mac(mac)

- Verify that the entered MAC address complies with one of the formats allowed via **regular expressions**
- Remove any separators (`:`, `-`, `.`)
- Start binary conversion if format is valid

#### convert_mac(mac)

- Split MAC address into 2-character octets
- Converts each octet from **hexadecimal to binary**
- Produces two outputs:
  - Octet-split binary version
  - Compact 48-bit binary version

#### main()

- Requires MAC address input from standard input
- Start the validation and conversion process

## Example

```text
MAC Address: AA:BB:CC:DD:EE:FF
Separate version: 10101010:10111011:11001100:11011101:11101110:11111111
Compact version: 101010101011101111001100110111011110111011111111
```
