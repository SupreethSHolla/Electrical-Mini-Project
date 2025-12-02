import serial
import matplotlib.pyplot as plt
import time

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

counts = []
times = []

plt.ion()
fig, ax = plt.subplots()

start = time.time()

while True:
    if arduino.in_waiting > 0:
        data = arduino.readline().decode().strip()
        if data.startswith("DETECTED:"):
            count = int(data.split(":")[1])
            counts.append(count)
            times.append(time.time() - start)

            ax.clear()
            ax.plot(times, counts)
            ax.set_xlabel("Time (s)")
            ax.set_ylabel("Count")
            ax.set_title("Real-Time Object Detection Count")
            plt.pause(0.01)
