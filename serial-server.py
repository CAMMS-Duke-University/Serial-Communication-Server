#!/usr/bin/python3

import os
import serial
import time

# Serial Port STM32 receibe dataset
def Serial_Connection(port_stval, baudrate_val, timeout_val):
    serial_port = None
    try:
        serial_port = serial.Serial(port= port_stval,
                            baudrate= baudrate_val,
                            timeout= timeout_val)
    except Error as err:
        return (f"Error: '{err}'")
    return serial_port

def main():
    serial_port = Serial_Connection(serial_port, serial_baudrate, serial_timeout)
    print("Port Status:", serial_port.is_open)

    #--------- Write loop
    while (serial_port.is_open):
        serial_port.write(b'hello2\n')
        serial_port.reset_output_buffer()
        time.sleep(2)
        print("sent")
    serial_port.close()

if __name__ == "__main__":
    main()
