#!/usr/bin/python
from __future__ import print_function

from wifi import Cell, Scheme

# get all cells from the air
ssids = [cell.ssid for cell in Cell.all('wlan0')]

schemes = list(Scheme.all())

for scheme in schemes:
    ssid = scheme.options.get('wpa-ssid', scheme.options.get('wireless-essid'))
    if ssid in ssids:
        print('Connecting to %s' % ssid)
        scheme.activate()
        break