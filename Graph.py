import serial
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PORT = "COM6"
arduino = serial.Serial(PORT, 9600, timeout=1)
time.sleep(2)

detection_times = []
detection_counts = []

start_time = time.time()
last_detected = False   # <-- NEW FLAG

plt.style.use("ggplot")
fig, ax = plt.subplots()

scatter = ax.scatter([], [], s=80)
ax.set_xlabel("Detection Number")
ax.set_ylabel("Time (sec)")
ax.set_title("IR Sensor Live Detection")


def update(frame):
    global scatter, last_detected

    line = arduino.readline().decode(errors="ignore").strip()

    if line != "":
        print("Received:", repr(line))

    # Parse "A:1 B:0"
    if line.startswith("A:") and "B:" in line:
        try:
            parts = line.split()
            A = int(parts[0].split(":")[1])
            B = int(parts[1].split(":")[1])
        except:
            return scatter,

        # ---------------------------
        # ONLY count when switching from NO OBJECT → OBJECT
        # ---------------------------
        if (A == 1 or B == 1) and (not last_detected):
            last_detected = True  # mark ONCE

            current_time = time.time() - start_time

            detection_times.append(current_time)
            detection_counts.append(len(detection_times))

            points = list(zip(detection_counts, detection_times))
            scatter.set_offsets(points)

            colors = plt.cm.rainbow([i / len(points)
                                    for i in range(len(points))])
            scatter.set_color(colors)

            ax.set_xlim(0, max(5, len(points) + 1))
            ax.set_ylim(0, max(detection_times) + 2)

            ax.set_title(f"IR Sensor Live Detection • Total: {len(points)}")

        # If no object → reset
        if A == 0 and B == 0:
            last_detected = False

    return scatter,


ani = FuncAnimation(fig, update, interval=100, cache_frame_data=False)
plt.show()
