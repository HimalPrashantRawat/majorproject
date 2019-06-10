import RPi.GPIO as GPIO
import serial
import time,sys

SERIAL_PORT = "/dev/ttyS0"
ser =serial.Serial(SERIAL_PORT,buadrate = 9600, timeout = 5)
ser.write("AT+CMGF=1\r")
print("Text mode enable...")
time.sleep(1)
ser.write('AT+CMGS="Phone Number"\r')
msg = "Put your message"
print("sending message...")
time.sleep(1)
ser.write(msg+chr(26))
time.sleep(1)
print("message sent...")