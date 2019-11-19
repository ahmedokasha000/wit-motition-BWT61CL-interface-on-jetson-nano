#!/usr/bin/python
import time
import serial
import array



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

    counter=0
    start_byte=0
    packet=bytearray([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])
    while True:
        if serial_port.inWaiting() > 0:
            data = serial_port.read()
            if (data == 'U') and (counter==0)  :
                print "start byte detected"
                start_byte=1
            if start_byte==1 :
                packet[counter]=data
                counter+=1
                if counter ==11 :
                    counter =0
                    start_byte=0
                    print "packet received"
                    print packet
                    packet= bytearray([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])
                
            




except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass
