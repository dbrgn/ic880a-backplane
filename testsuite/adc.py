"""
Example script to read the input voltage, measured by the MCP3425 ADC.
Datasheet: http://ww1.microchip.com/downloads/en/DeviceDoc/22072b.pdf
"""
# -*- coding: utf-8 -*-
from __future__ import print_function, division

import time

# ADC reference
ADC_REF = 2048  # mV

# Config register bits
BIT_G0 = 0
BIT_G1 = 1
BIT_S0 = 2
BIT_S1 = 3
BIT_OC = 4
BIT_C0 = 5
BIT_C1 = 6
BIT_RDY = 7

# Conversion mode
CONVERSION_MODE_ONESHOT = 0
CONVERSION_MODE_CONT = 1 << BIT_OC

# Sample rate / accuracy
SAMPLE_RATE_240SPS = 0  # 12 bits
SAMPLE_RATE_60SPS = 1 << BIT_S0  # 14 bits
SAMPLE_RATE_15SPS = 1 << BIT_S1  # 16 bits

# PGA gain selection
PGA_GAIN_1 = 0
PGA_GAIN_2 = 1 << BIT_G0
PGA_GAIN_4 = 1 << BIT_G1
PGA_GAIN_8 = (1 << BIT_G1) | (1 << BIT_G0)

# Start a conversion in one shot mode
START_CONVERSION = 1 << BIT_RDY
