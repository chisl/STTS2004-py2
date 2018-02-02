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
	# nEVENT behavior upon shutdown (default) 
	# Bits TMOUT
	# bus timeout support 
	# Bits VHV
	# (VHV) high voltage support for A0 (pin 1) 
	# Bits TRES1
	# Temperature resolution 
	# Bits Wider_range
	# Bits Higher_precision
	# Bits Alarm_and_critical_trips
	# Register Configuration
	# The 16-bit configuration register stores various configuration modes that are used to set up
	#       the sensor registers and configure according to application and JEDEC requirements (see
	#       Table 9 on page 21 and Table 10 on page 21).
	#       
	#       The temperature sensor configuration register holds the control and status bits of the
	#       EVENT pin as well as general hysteresis on all limits. To avoid glitches on the EVENT
	#       output pin, users should disable EVENT or CRITICAL functions prior to programming or
	#       changing other device configuration settings.
	#       
	#       4.2.1 Event thresholds
	#       All event thresholds use hysteresis as programmed in register address 0x01 (bits 10
	#       through 9) to be set when they de-assert.
	#       
	#       4.2.2 Interrupt mode
	#       The interrupt mode allows an event to occur where software may write a '1' to the clear
	#       event bit (bit 5) to de-assert the event Interrupt output until the next trigger condition occurs.
	#       
	#       4.2.3 Comparator mode
	#       The comparator mode enables the device to be used as a thermostat. READs and WRITEs
	#       on the device registers will not affect the event output in comparator mode. The event signal
	#       will remain asserted until temperature drops outside the range or is re-programmed to make
	#       the current temperature “out of range”.
	#       
	#       4.2.4 Shutdown mode
	#       The STTS2004 features a shutdown mode which disables all power-consuming activities
	#       (e.g. temperature sampling operations), and leaves the serial interface active. This is
	#       selected by setting the shutdown bit (bit 8) to '1'. In this mode, the devices consume the
	#       minimum current (ISHDN), as shown in Table 30 on page 44.
	#       NOTE: Bit 8 cannot be set to '1' while bits 6 and 7 (the lock bits) are set to '1'.
	#       The device may be enabled for continuous operation by clearing bit 8 to '0'. In shutdown
	#       mode, all registers may be read or written to. Power recycling will also clear this bit and
	#       return the device to continuous mode as well.
	#       If the device is shut down while the EVENT pin is asserted, then the Event output will be deasserted
	#       during shutdown. It will remain de-asserted until the device is enabled for normal
	#       operation. Once the device is enabled, it takes tCONV before the device can re-assert the
	#       Event output. 
	
	
	def setConfiguration(self, val):
		"""Set register Configuration"""
		self.write(REG.Configuration, val, 16)
	
	def getConfiguration(self):
		"""Get register Configuration"""
		return self.read(REG.Configuration, 16)
	
	# Bits reserved_0
	# These bits will always read ‘0’ and writing to them will have no effect. For future
	#           compatibility, all RFU bits must be programmed as ‘0’ 
	
	# Bits Hysteresis
	# Bits Shutdown_mode
	# Bits Critical_lock_bit
	# Bits Alarm_lock_bit
	# Bits Clear_event
	# Writing to this register has no effect on overall device functioning in comparator mode. 
	#           When read, this bit will always return a logic '0' result. 
	
	# Bits Output_status
	# NOTE: The actual incident causing the event can be determined from the read temperature
	#         register. Interrupt events can be cleared by writing to the clear event bit (writing to
	#         this bit will have no effect on overall device functioning). 
	
	# Bits Event_output_control
	# Bits Critical_event_only
	# Bits Event_polarity
	# The event polarity bit controls the active state of the EVENT pin. The EVENT pin is driven to this state
	#           when it is asserted. 
	#           NOTE: As this device is used in DIMM (memory modules) applications, it is strongly recommended
	#           that only the active-low polarity (default) is used. This will provide full compatibility
	#           with the STTS2002. This is the recommended configuration for the STTS2004. 
	
	# Bits Event_mode
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
