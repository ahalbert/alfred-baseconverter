====
# Alfred Base Converter
====


Convert arbitrary bases(up to base 32) in Alfred 2 and copy them to the clipboard.

Format: `{base}x{number} {target base}`

![](https://github.com/ahalbert/alfred-baseconverter/blob/master/screenshots/hex8.png?raw=true)

Push enter to add the result to the clipboard.

If no base is specified, it will default to decimal. If the source number is decimal, hex will be output.

![](https://github.com/ahalbert/alfred-baseconverter/blob/master/screenshots/hex10.png?raw=true)

Special prefixes:

* None or d: decimal
* 0x : hex/base 16
* 0 or O: octal
* b: binary

![](https://github.com/ahalbert/alfred-baseconverter/blob/master/screenshots/binary.png?raw=true)

These prefixes work for the both the normal base and the target base.

Written by Armand Halbert

Licensed under BSD.
