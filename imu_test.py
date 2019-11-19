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
    Temp=0.0
    acc=[0.0]*3
    angVel=[0.0]*3
    angle=[0.0]*3
    packet= [0]*11
    while True:
            if serial_port.inWaiting() > 0:
                data =ord( serial_port.read())
                #print(data)
                if (data ==0x55) and (counter==0)  :
                    print "start byte detected"
                    start_byte=1
                if start_byte==1 :
                    packet[counter]=data
                    counter+=1
                    if counter ==11 :
                        counter =0
                        start_byte=0
                        #print "packet received"
                        #print packet
                        decodePacket()
                        packet= [0]*11







except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass


def decodePacket() :
    global packet,angle,angVel,acc,Temp
    if packet[1]==0x51 :
          acc[0] = (packet [3] << 8 | packet [2]) / 32768.0 * 16
          acc[1] = (packet [5] << 8 | packet [4]) / 32768.0 * 16
          acc[2] = (packet [7] << 8 | packet [6]) / 32768.0 * 16
          Temp =   (packet [9] << 8 | packet [8]) / 340.0 + 36.25
    elif packet[1]==0x52:
          angVel[0] = (packet [3] << 8 | packet [2]) / 32768.0 * 2000
          angVel[1] = (packet [5] << 8 | packet [4]) / 32768.0 * 2000
          angVel[2] = (packet [7] << 8 | packet [6]) / 32768.0 * 2000
          Temp = (packet [9] << 8 | packet [8]) / 340.0 + 36.25        
        
    elif packet[1]==0x53:
          angle[0] = (packet [3] << 8 | packet [2]) / 32768.0 * 180
          angle[1] = (packet [5] << 8 | packet [4]) / 32768.0 * 180
          angle[2] = (packet [7] << 8 | packet [6]) / 32768.0 * 180
          Temp = (packet [9] << 8 | packet [8]) / 340.0 + 36.25
          print("a :",acc,"w :",angVel,"angle :",angle,"Temp :",Temp)



