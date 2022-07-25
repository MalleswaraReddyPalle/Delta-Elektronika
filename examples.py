# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:29:56 2022

@author: Aleksander
"""
import DeltaPowerSupply as dps
import numpy as np
import time


def ramp_up(start_voltage, stop_voltage, dx):
    arr = np.arange(start_voltage, stop_voltage, dx)
    dt = dx
    for i in arr:
        delta.set_voltage(i)
        time.sleep(dt)
        
def ramp_down(start_voltage, stop_voltage, dx):
    arr = np.arange(stop_voltage, start_voltage, dx)[::-1]
    dt = dx
    for i in arr:
        delta.set_voltage(i)
        time.sleep(dt)

delta = dps.Instrument("192.168.xx.xxx", 8462)
delta.set_output(True)
ramp_up(start_voltage=0, stop_voltage=10, duration=1)
ramp_down(start_voltage=10, stop_voltage=0, dx=0.1)
delta.set_output(False)
delta.close_instrument()

