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

from STTS2004_constants import *

# name:        STTS2004
# description: 2.2 V memory module temperature sensor with a 4 Kb SPD EEPROM
# manuf:       ST Microelectronics
# version:     Version 0.1
# url:         http://www.st.com/resource/en/datasheet/stts2004.pdf
# date:        2018-01-31


# Derive from this class and implement read and write
class STTS2004_Base:
	"""2.2 V memory module temperature sensor with a 4 Kb SPD EEPROM"""
	# Register Pointer
	
	
	def setPointer(self, val):
		"""Set register Pointer"""
		self.write(REG.Pointer, val, 16)
	
	def getPointer(self):
		"""Get register Pointer"""
		return self.read(REG.Pointer, 16)
	
	# Bits unused_0
	# must always be written to '0', not setting these bits to '0' may keep the device from performing to specifications. 
	# Bits Pointer
	# Register Capability
	# This 16-bit register is read-only, and provides the TS capabilities which comply with the
	#       minimum JEDEC TSE2004av specifications (see Table 7 and Table 8 on page 19). The
	#       STTS2004 resolution is programmable via writing to pointer 08 register. The power-on
	#       default value is 0.25 °C/LSB (10-bit). 
	
	
	def setCapability(self, val):
		"""Set register Capability"""
		self.write(REG.Capability, val, 16)
	
	def getCapability(self):
		"""Get register Capability"""
		return self.read(REG.Capability, 16)
	
	# Bits reserved_0
	# These values must be set to '0'. 
	# Bits EVSD
	# Bits TMOUT
	# Bits VHV
	# Bits TRES1
	# Bits Wider_range
	# Bits Higher_precision
	# Bits Alarm_and_critical_trips
	# Register Configuration
	
	
	def setConfiguration(self, val):
		"""Set register Configuration"""
		self.write(REG.Configuration, val, 16)
	
	def getConfiguration(self):
		"""Get register Configuration"""
		return self.read(REG.Configuration, 16)
	
	# Bits Configuration
	# Register Alarm_Upper
	# Alarm temperature upper boundary trip 
	
	def setAlarm_Upper(self, val):
		"""Set register Alarm_Upper"""
		self.write(REG.Alarm_Upper, val, 16)
	
	def getAlarm_Upper(self):
		"""Get register Alarm_Upper"""
		return self.read(REG.Alarm_Upper, 16)
	
	# Bits Alarm_Upper
	# Register Alarm_Lower
	# Alarm temperature lower boundary trip 
	
	def setAlarm_Lower(self, val):
		"""Set register Alarm_Lower"""
		self.write(REG.Alarm_Lower, val, 16)
	
	def getAlarm_Lower(self):
		"""Get register Alarm_Lower"""
		return self.read(REG.Alarm_Lower, 16)
	
	# Bits Alarm_Lower
	# Register Critical_Temperature_Trip
	
	
	def setCritical_Temperature_Trip(self, val):
		"""Set register Critical_Temperature_Trip"""
		self.write(REG.Critical_Temperature_Trip, val, 16)
	
	def getCritical_Temperature_Trip(self):
		"""Get register Critical_Temperature_Trip"""
		return self.read(REG.Critical_Temperature_Trip, 16)
	
	# Bits Critical_Temperature_Trip
	# Register Temperature
	# Undefined 
	
	def setTemperature(self, val):
		"""Set register Temperature"""
		self.write(REG.Temperature, val, 16)
	
	def getTemperature(self):
		"""Get register Temperature"""
		return self.read(REG.Temperature, 16)
	
	# Bits Temperature
	# Register ID
	# Manufacturer’s ID 
	
	def setID(self, val):
		"""Set register ID"""
		self.write(REG.ID, val, 16)
	
	def getID(self):
		"""Get register ID"""
		return self.read(REG.ID, 16)
	
	# Bits ID
	# Register Device_Id
	# Device ID/revision 
	
	def setDevice_Id(self, val):
		"""Set register Device_Id"""
		self.write(REG.Device_Id, val, 16)
	
	def getDevice_Id(self):
		"""Get register Device_Id"""
		return self.read(REG.Device_Id, 16)
	
	# Bits Device_Id
	# Register Temperature_Resolution
	# Temperature resolution register 
	
	def setTemperature_Resolution(self, val):
		"""Set register Temperature_Resolution"""
		self.write(REG.Temperature_Resolution, val, 16)
	
	def getTemperature_Resolution(self):
		"""Get register Temperature_Resolution"""
		return self.read(REG.Temperature_Resolution, 16)
	
	# Bits Temperature_Resolution
