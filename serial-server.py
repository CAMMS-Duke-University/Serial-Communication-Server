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

def Serial_Write_One_Time(serial_port, message,pause_time):
    serial_port.write(message)
    serial_port.reset_output_buffer()
    time.sleep(pause_time)
    print("message sent")

def Serial_Write_Continuously(serial_port, message,pause_time):
    #--------- Write loop
    while (serial_port.is_open):
        Serial_Write_One_Time(serial_port, message,pause_time)

    serial_port.write(message)
    serial_port.reset_output_buffer()
    time.sleep(pause_time)
    print("message sent")
    return 0

def Serial_Read_One_Time(serial_port):
    message = serial_port.readline()
    print("Message received: ", message)
    return message

def main():
    serial_port = Serial_Connection("/dev/ttyUSB0", 115200, 5.0)
    print("Port Status:", serial_port.is_open)
    message = b'hello2\n'
    pause_time = 1.0
    Serial_Write_Continuously(serial_port, message,pause_time)
    serial_port.close()


if __name__ == "__main__":
    main()
