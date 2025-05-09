# PiStaX

## The Modular Mini Computer

This is a fully modular minicomputer based on the Raspberry Pi Zero 2W.
The example layers include a main part with the Raspberry Pi and an I/O extender.
The top layer contains a screen and a keyboard (for more info on the keyboard, see the license section).
--------------------------------------------------------------------------------------------------------

# Module Connector

The connector between modules is made of 4 parts

| Part                  | Description      | LCSC-Part-Nr |
| --------------------- | ---------------- | ------------ |
| 2X2 Connector male    | USB data/power   | C3294460     |
| 2X2 Connector female  | USB data/power   | C27983455    |
| 2X20 Connector male   | Raspberry Pi I/O | C3294478     |
| 2X20 Connector female | Raspberry Pi I/O | C3975165     |

The power is preferably transferred over the USB header and not over the Raspberry Pi pins directly. If possible, use a GND and VCC layer.
