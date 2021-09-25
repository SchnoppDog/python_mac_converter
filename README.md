# MAC-Address Converter

This is a simple python-class to convert most used mac-address formats to other mac-address formats.
The class also provides an option to lookup the vendor of the given mac-address.

## Supported MAC-Address Formats

Support mac-address formats are referenced from the german [wikipedia article](https://de.wikipedia.org/wiki/MAC-Adresse#Form_(Syntax)) about the mac-address.
Therefore supported mac-convertions are:

1. XX-XX-XX-XX-XX-XX
2. XXXXXX-XXXXXX
3. XX:XX:XX:XX:XX:XX
4. XXXXXXXXXXXX
5. XXXX.XXXX.XXXX

## Installation

To install this class you need to download this repository and unpack it. After unpacking run the `setup.py`:

```cmd
py setup.py install
```

## Usage

To use this class import it into your python script:

```python
from c_mac_address_converter import macAddressConverter
```

### Methods

The following methods are available:

| Function | Parameters | Return | Description | Example |
| --- | ---| --- | --- | ---|
| `macAddressConverter()` | - | - | Initiates the converter | `converter = macAddressConverter()` |
| `printSupportFormats()` | - | - | Prints all supported mac-address formats | `converter.printSupportFormats()` |
| `setMacAddress()` | `macAddress : list` | - | Set one or multiple mac-addresses as list | `converter.setMacAddress([12:34:56:AB:CD:EF])` |
| `getMacFormat1()` | - | `list` | Returns the mac-address(es) in the firs format | `converter.getMacFormat1()` |
| `getMacFormat2()` | - | `list` | Returns the mac-address(es) in the second format | `converter.getMacFormat2()` |
| `getMacFormat3()` | - | `list` | Returns the mac-address(es) in the third format | `converter.getMacFormat3()` |
| `getMacFormat4()` | - | `list` | Returns the mac-address(es) in the fourth format | `converter.getMacFormat4()` |
| `getMacFormat5()` | - | `list` | Returns the mac-address(es) in the fifth format | `converter.getMacFormat5()` |
| `getMacFormatAll()` | - | `list` | Returns the mac-address(es) in all five supported formats | `converter.getMacFormatAll()` |
| `getMacVendor()` | `macAddressList : list` | `list` | Returns the vendor of the mac-address(es) | `converter.getMacVendor([12:34:56:AB:CD:EF])` |

### About 'obtaining the mac-vendor'

To obtain the mac-address vendor I use the requests-module to make a GET-request to the following website `https://api.macvendors.com/` followed by the mac-address.
This is a webiste you can get your mac-address vendor for free. You can make about 1.000 GET-requests per day.

## Supported Python Versions

- Python version 3
- Tested in python version 3.9.7

## License

- MIT
