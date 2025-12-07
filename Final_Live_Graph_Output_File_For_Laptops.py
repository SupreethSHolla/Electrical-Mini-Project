import serial
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PORT = "COM6"
arduino = serial.Serial(PORT, 9600, timeout=1)
time.sleep(2)

detection_times = []   # store time only when object detected

plt.style.use("ggplot")

fig, ax = plt.subplots()
scatter = ax.scatter([], [], s=60, c='red')

start_time = time.time()

ax.set_xlabel("Time (s)")
ax.set_ylabel("Object Detection")
ax.set_title("IR Sensor Live Detection (Only Plots When Object Detected)")
ax.set_ylim(0, 1)
ax.set_yticks([])  # remove Y-axis ticks (only 1 level)


def update(frame):
    line = arduino.readline().decode().strip()

    if line == "Object Detected!":
        t = time.time() - start_time
        detection_times.append(t)

        # keep only last 50 points
        detection_times_trim = detection_times[-50:]

        scatter.set_offsets([[ti, 1] for ti in detection_times_trim])
        ax.set_xlim(max(0, detection_times_trim[0] - 1),
                    detection_times_trim[-1] + 1)

    # If "No Object Detected" → do nothing (no plotting)

    return scatter,


ani = FuncAnimation(fig, update, interval=100)
plt.show()
