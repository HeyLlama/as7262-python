# AS726x Spectral Sensor

[![Build Status](https://travis-ci.com/pimoroni/as7262-python.svg?branch=master)](https://travis-ci.com/pimoroni/as7262-python)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/as7262-python/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/as7262-python?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/as7262.svg)](https://pypi.python.org/pypi/as7262)
[![Python Versions](https://img.shields.io/pypi/pyversions/as7262.svg)](https://pypi.python.org/pypi/as7262)

Forked from https://github.com/pimoroni/as7262-python
Suitable for detecting the properties of ambient light, light passing through a liquid or light reflected from an object.

# Installing

Latest/development library from GitHub:

* `git clone https://github.com/HeyLlama/as726x-python`
* `cd as726x-python`
* `sudo ./install.sh`

# Example
## AS7262
from as7262 import AS7262
as7262 = AS7262()
as7262.set_measurement_mode(2)
as7262.set_illumination_led(1)

## AS7263
from as7263 import AS7263
as7263 = AS7263()
as7263.set_measurement_mode(2)
as7263.set_illumination_led(1)

*Note: AS7262 and AS7263 shares the same I2C address. You must run these commands separately or use a MUX board*
