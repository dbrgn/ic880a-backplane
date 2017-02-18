# iC880A + Raspberry Pi Backplane

This is a backplane to connect an iC880A-SPI concentrator board to a Raspberry
Pi. It is inspired by the [iC880A backplane by
@gonzalocasas](https://github.com/gonzalocasas/ic880a-backplane), but aims to
give you the following additional features:

- Full access to Raspberry Pi GPIO header
- Pin header for power input/output (5V/GND)
- Pin header for I²C based sensors (SDA/SCL/GND/3.3V/5V)
- Pin header for serial communication (RX/TX)
- Footprint for three general purpose SMD LEDs
- Footprint for a [SHT21](https://sensirion.com/sht21/) temperature/humidity
  sensor (SMD package)
- Mounting holes for Raspberry Pi B+ / 2B / 3B / Zero

![Rendered](rendered.png)

![Rendered](rendered-back.png)


## Development

This PCB was created using KiCad 4.

Make sure that you clone all submodules:

    git submodule init
    git submodule update


## License

© 2017 Danilo Bargen. Licensed under the TAPR Open Hardware License (www.tapr.org/OHL).

If you make any modification to this board, it would be great if you could let
me know at mail@dbrgn.ch.
