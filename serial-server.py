#!/usr/bin/python3

import os
import serial
import time
import sys

# Serial Port connection handling
def Serial_Connection(port_stval, baudrate_val, timeout_val):
    serial_port = None
    try:
        serial_port = serial.Serial(port= port_stval,
                            baudrate= baudrate_val,
                            timeout= timeout_val)
    except:
        print("Could not connect to the Serial Port:", port_stval)
        sys.exit(1) # returns exit 1 which is the fail
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
    # calls the [Serial_Connection] function which establish a connection to a Serial Port and return the handler
    serial_port = Serial_Connection("/dev/ttyUSB0", 115200, 5.0)
    print("Port Status:", serial_port.is_open) # print the status of the Connection if True then there is a connection

    if( serial_port.is_open): # If connection is established then Send or Receive data
        task_name = sys.argv[1]
        print(task_name)

        if method_name == 'read':
            Serial_Read_One_Time(serial_port)
        elif method_name == 'write':
            message = sys.argv[2]
            pause_time = 1.0
            Serial_Write_Continuously(serial_port, message,pause_time)

        serial_port.close()
        sys.exit(0)
    else: # If connection is not established the return exit 1
        sys.exit(1)

    message = b'hello2\n'
    pause_time = 1.0
    Serial_Write_Continuously(serial_port, message,pause_time)



if __name__ == "__main__":
    main()
