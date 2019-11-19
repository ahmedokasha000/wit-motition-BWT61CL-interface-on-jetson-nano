#!/usr/bin/python
import time
import serial
import array
print("UART Demonstration Program")
print("NVIDIA Jetson Nano Developer Kit")


serial_port = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
# Wait a second to let the port initialize
time.sleep(1)

try:
    # Send a simple header
    serial_port.write("UART Demonstration Program\r\n".encode())
    serial_port.write("NVIDIA Jetson Nano Developer Kit\r\n".encode())
    counter=0
    start_byte=0
    packet= array.array('i',(0 for i in range(0,11)))
    while True:
        if serial_port.inWaiting() > 0:
            data = serial_port.read()
            if data == 0x55 & counter==0  :
                start_byte=1
            if start_byte==1 :
                packet[counter]=data
                counter+=1
                if counter ==11 :
                    counter =0
                    start_byte=0
                    print(packet)
                    packet= array.array('i',(0 for i in range(0,11)))
                
            




except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass
