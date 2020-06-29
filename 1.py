
#!/usr/bin/env python
import RPi.GPIO as GPIO
import serial
import time
GPIO.setmode(GPIO.BOARD)

ser = serial.Serial(
        port='/dev/serial0',
        baudrate=9600,
        timeout=1
)

print ("Serial is open: " + str(ser.isOpen()))

print("Now Writing")
ser.write("AT".encode())

print("Did write, now read")
counter = 0
while True:
        ser.write(str.encode('Write counter: %d \n'%(counter)))
        time.sleep(1)
        counter += 1
ser.close()