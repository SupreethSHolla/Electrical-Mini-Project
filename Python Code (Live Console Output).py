import serial
import time

# Change COM port (Windows: COM3, Linux/Mac: /dev/ttyUSB0 or /dev/ttyACM0)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # wait for Arduino to reset

print("Connected to Arduino. Listening for sensor data...\n")

while True:
    if arduino.in_waiting > 0:
        data = arduino.readline().decode().strip()
        print("Arduino:", data)
