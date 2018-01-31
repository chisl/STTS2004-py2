#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""STTS2004: 2.2 V memory module temperature sensor with a 4 Kb SPD EEPROM"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["ST Microelectronics"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

class REG:
	Pointer = 255
	Capability = 0
	Configuration = 1
	Alarm_Upper = 2
	Alarm_Lower = 3
	Critical_Temperature_Trip = 4
	Temperature = 5
	ID = 6
	Device_Id = 7
	Temperature_Resolution = 8
