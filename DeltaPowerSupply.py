# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:34:21 2022

@author: Aleksander
"""

import socket

class Instrument:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as instrument:
        self.instrument = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.instrument.connect((self.host, self.port))
    def close_instrument(self):
        self.instrument.close()

    def set_voltage(self, voltage):
        self.instrument.send(f'SOURce:VOLTage {voltage}\n'.encode())
    
    def get_voltage(self):
        self.instrument.send(b'MEASure:VOLTage?\n')
        return self.instrument.recv(1024).decode("utf-8")
    
    def set_current(self, current):
        self.instrument.send(f'SOURce:CURRent {current}\n'.encode())
    
    def get_current(self):
        self.instrument.send(b'MEASure:CURRent?\n')
        return self.instrument.recv(1024).decode("utf-8")
        
    def set_output(self, output:bool):
        if output:
            output=1
        else:
            output=0
        self.instrument.send(f'OUTPut {output}\n'.encode())
    
    def get_and_clear_errors(self):
        # Five reads should clear the register
        errors = []
        for i in range(5):
            self.instrument.send(b'*SYSTem:ERRor?\n')
            error = self.instrument.recv(1024).decode("utf-8") 
            errors.append(error)
            return errors
            
    def get_error(self):
        self.instrument.send(b'*SYSTem:ERRor?\n')
        return self.instrument.recv(1024).decode("utf-8") 
    
    def clear_all(self):
        self.instrument.send(b'*CLS\n')



