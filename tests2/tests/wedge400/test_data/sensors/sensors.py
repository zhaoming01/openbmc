#!/usr/bin/env python,
#
# Copyright 2019-present Facebook. All Rights Reserved.,
#
# This program file is free software; you can redistribute it and/or modify it,
# under the terms of the GNU General Public License as published by the,
# Free Software Foundation; version 2 of the License.,
#
# This program is distributed in the hope that it will be useful, but WITHOUT,
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or,
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License,
# for more details.,
#
# You should have received a copy of the GNU General Public License,
# along with this program in a file named COPYING; if not, write to the,
# Free Software Foundation, Inc.,,
# 51 Franklin Street, Fifth Floor,,
# Boston, MA 02110-1301 USA,
#

SENSORS = [
    # Sensors on SCM
    "SCM_OUTLET_TEMP",
    "SCM_INLET_TEMP",
    "SCM_HSC_VOLT",
    "SCM_HSC_CURR",
    "SCM_HSC_POWER",
    "MB_OUTLET_TEMP",
    "MB_INLET_TEMP",
    "PCH_TEMP",
    "VCCIN_VR_TEMP",
    "1V05COMB_VR_TEMP",
    "SOC_TEMP",
    "SOC_THERM_MARGIN_TEMP",
    "VDDR_VR_TEMP",
    "SOC_DIMMA_TEMP",
    "SOC_DIMMB_TEMP",
    "SOC_PACKAGE_POWER",
    "VCCIN_VR_OUT_POWER",
    "VDDR_VR_OUT_POWER",
    "SOC_TJMAX_TEMP",
    "P3V3_MB_VOLT",
    "P12V_MB_VOLT",
    "P1V05_PCH_VOLT",
    "P3V3_STBY_MB_VOLT",
    "P5V_STBY_MB_VOLT",
    "PV_BAT_VOLT",
    "PVDDR_VOLT",
    "P1V05_COMB_VOLT",
    "1V05COMB_VR_CURR",
    "VDDR_VR_CURR",
    "VCCIN_VR_CURR",
    "VCCIN_VR_VOLT",
    "VDDR_VR_VOLT",
    "1V05COMB_VR_VOLT",
    "1V05COMB_VR_OUT_POWER",
    "INA230_POWER",
    "INA230_VOLT",
    # Sensors on SMB
    "XP12R0V (12V)",
    "XP5R0V (5V)",
    "XP3R3V_BMC (3.3V)",
    "XP2R5V_BMC (2.5V)",
    "XP1R2V_BMC (1.2V)",
    "XP1R15V_BMC (1.15V)",
    "XP1R2V_TH3 (1.2V)",
    "PVDD0P8_TH3 (0.8V)",
    "XP3R3V_TH3 (3.3V)",
    "VDD_CORE_TH3 (0.75~0.9V)",
    "TRVDD0P8_TH3 (0.8V)",
    "XP1R8V_TH3 (1.8V)",
    "POWR1220 VCCA (3.3V)",
    "POWR1220 VCCINP (3.3V)",
    "TH3_SERDES_VOLT(PVDD)",
    "TH3_SERDES_CURR(PVDD)",
    "TH3_SERDES_POWER(PVDD)",
    "TH3_SERDES_VOLT(TRVDD)",
    "TH3_SERDES_CURR(TRVDD)",
    "TH3_SERDES_POWER(TRVDD)",
    "TH3_CORE_VOLT",
    "TH3_CORE_CURR",
    "TH3_CORE_POWER",
    "TH3_CORE_TEMP1",
    "SMB_TEMP1",
    "SMB_TEMP2",
    "SMB_TEMP3",
    "SMB_TEMP4",
    "SMB_TEMP5",
    "SMB_TEMP6",
    "TH3_DIE_TEMP1",
    "TH3_DIE_TEMP2",
    "FCM_TEMP1",
    "FCM_TEMP2",
    "FCM_HSC_VOLT",
    "FCM_HSC_CURR",
    "FCM_HSC_POWER",
    "FAN1_FRONT_SPEED",
    "FAN1_REAR_SPEED",
    "FAN2_FRONT_SPEED",
    "FAN2_REAR_SPEED",
    "FAN3_FRONT_SPEED",
    "FAN3_REAR_SPEED",
    "FAN4_FRONT_SPEED",
    "FAN4_REAR_SPEED",
    # Sensors on PEM1
    "PEM1_IN_VOLT",
    "PEM1_OUT_VOLT",
    "PEM1_CURR",
    "PEM1_POWER",
    "PEM1_FAN1_SPEED",
    "PEM1_FAN2_SPEED",
    "PEM1_HOT_SWAP_TEMP",
    "PEM1_AIR_INLET_TEMP",
    "PEM1_AIR_OUTLET_TEMP",
    # Sensors on PEM2
    "PEM2_IN_VOLT",
    "PEM2_OUT_VOLT",
    "PEM2_CURR",
    "PEM2_POWER",
    "PEM2_FAN1_SPEED",
    "PEM2_FAN2_SPEED",
    "PEM2_HOT_SWAP_TEMP",
    "PEM2_AIR_INLET_TEMP",
    "PEM2_AIR_OUTLET_TEMP",
    # Sensors on PSU1
    "PSU1_IN_VOLT",
    "PSU1_12V_VOLT",
    "PSU1_STBY_VOLT",
    "PSU1_IN_CURR",
    "PSU1_12V_CURR",
    "PSU1_STBY_CURR",
    "PSU1_IN_POWER",
    "PSU1_12V_POWER",
    "PSU1_STBY_POWER",
    "PSU1_FAN_SPEED",
    "PSU1_TEMP1",
    "PSU1_TEMP2",
    "PSU1_TEMP3",
    # Sensors on PSU2
    "PSU2_IN_VOLT",
    "PSU2_12V_VOLT",
    "PSU2_STBY_VOLT",
    "PSU2_IN_CURR",
    "PSU2_12V_CURR",
    "PSU2_STBY_CURR",
    "PSU2_IN_POWER",
    "PSU2_12V_POWER",
    "PSU2_STBY_POWER",
    "PSU2_FAN_SPEED",
    "PSU2_TEMP1",
    "PSU2_TEMP2",
    "PSU2_TEMP3",
]

SCM_SENSORS = [
    # Sensors on SCM
    "SCM_OUTLET_TEMP",
    "SCM_INLET_TEMP",
    "SCM_HSC_VOLT",
    "SCM_HSC_CURR",
    "SCM_HSC_POWER",
    "MB_OUTLET_TEMP",
    "MB_INLET_TEMP",
    "PCH_TEMP",
    "VCCIN_VR_TEMP",
    "1V05COMB_VR_TEMP",
    "SOC_TEMP",
    "SOC_THERM_MARGIN_TEMP",
    "VDDR_VR_TEMP",
    "SOC_DIMMA_TEMP",
    "SOC_DIMMB_TEMP",
    "SOC_PACKAGE_POWER",
    "VCCIN_VR_OUT_POWER",
    "VDDR_VR_OUT_POWER",
    "SOC_TJMAX_TEMP",
    "P3V3_MB_VOLT",
    "P12V_MB_VOLT",
    "P1V05_PCH_VOLT",
    "P3V3_STBY_MB_VOLT",
    "P5V_STBY_MB_VOLT",
    "PV_BAT_VOLT",
    "PVDDR_VOLT",
    "P1V05_COMB_VOLT",
    "1V05COMB_VR_CURR",
    "VDDR_VR_CURR",
    "VCCIN_VR_CURR",
    "VCCIN_VR_VOLT",
    "VDDR_VR_VOLT",
    "1V05COMB_VR_VOLT",
    "1V05COMB_VR_OUT_POWER",
    "INA230_POWER",
    "INA230_VOLT",
]

SMB_SENSORS = [
    # Sensors on SMB
    "XP12R0V (12V)",
    "XP5R0V (5V)",
    "XP3R3V_BMC (3.3V)",
    "XP2R5V_BMC (2.5V)",
    "XP1R2V_BMC (1.2V)",
    "XP1R15V_BMC (1.15V)",
    "XP1R2V_TH3 (1.2V)",
    "PVDD0P8_TH3 (0.8V)",
    "XP3R3V_TH3 (3.3V)",
    "VDD_CORE_TH3 (0.75~0.9V)",
    "TRVDD0P8_TH3 (0.8V)",
    "XP1R8V_TH3 (1.8V)",
    "POWR1220 VCCA (3.3V)",
    "POWR1220 VCCINP (3.3V)",
    "TH3_SERDES_VOLT(PVDD)",
    "TH3_SERDES_CURR(PVDD)",
    "TH3_SERDES_POWER(PVDD)",
    "TH3_SERDES_VOLT(TRVDD)",
    "TH3_SERDES_CURR(TRVDD)",
    "TH3_SERDES_POWER(TRVDD)",
    "TH3_CORE_VOLT",
    "TH3_CORE_CURR",
    "TH3_CORE_POWER",
    "TH3_CORE_TEMP1",
    "SMB_TEMP1",
    "SMB_TEMP2",
    "SMB_TEMP3",
    "SMB_TEMP4",
    "SMB_TEMP5",
    "SMB_TEMP6",
    "TH3_DIE_TEMP1",
    "TH3_DIE_TEMP2",
    "FCM_TEMP1",
    "FCM_TEMP2",
    "FCM_HSC_VOLT",
    "FCM_HSC_CURR",
    "FCM_HSC_POWER",
    "FAN1_FRONT_SPEED",
    "FAN1_REAR_SPEED",
    "FAN2_FRONT_SPEED",
    "FAN2_REAR_SPEED",
    "FAN3_FRONT_SPEED",
    "FAN3_REAR_SPEED",
    "FAN4_FRONT_SPEED",
    "FAN4_REAR_SPEED",
]

PEM1_SENSORS = [
    # Sensors on PEM1
    "PEM1_IN_VOLT",
    "PEM1_OUT_VOLT",
    "PEM1_CURR",
    "PEM1_POWER",
    "PEM1_FAN1_SPEED",
    "PEM1_FAN2_SPEED",
    "PEM1_HOT_SWAP_TEMP",
    "PEM1_AIR_INLET_TEMP",
    "PEM1_AIR_OUTLET_TEMP",
]

PEM2_SENSORS = [
    # Sensors on PEM2
    "PEM2_IN_VOLT",
    "PEM2_OUT_VOLT",
    "PEM2_CURR",
    "PEM2_POWER",
    "PEM2_FAN1_SPEED",
    "PEM2_FAN2_SPEED",
    "PEM2_HOT_SWAP_TEMP",
    "PEM2_AIR_INLET_TEMP",
    "PEM2_AIR_OUTLET_TEMP",
]

PSU1_SENSORS = [
    # Sensors on PSU1
    "PSU1_IN_VOLT",
    "PSU1_12V_VOLT",
    "PSU1_STBY_VOLT",
    "PSU1_IN_CURR",
    "PSU1_12V_CURR",
    "PSU1_STBY_CURR",
    "PSU1_IN_POWER",
    "PSU1_12V_POWER",
    "PSU1_STBY_POWER",
    "PSU1_FAN_SPEED",
    "PSU1_TEMP1",
    "PSU1_TEMP2",
    "PSU1_TEMP3",
]

PSU2_SENSORS = [
    # Sensors on PSU2
    "PSU2_IN_VOLT",
    "PSU2_12V_VOLT",
    "PSU2_STBY_VOLT",
    "PSU2_IN_CURR",
    "PSU2_12V_CURR",
    "PSU2_STBY_CURR",
    "PSU2_IN_POWER",
    "PSU2_12V_POWER",
    "PSU2_STBY_POWER",
    "PSU2_FAN_SPEED",
    "PSU2_TEMP1",
    "PSU2_TEMP2",
    "PSU2_TEMP3",
]