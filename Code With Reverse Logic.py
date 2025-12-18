# ---------- IMPORT MODULES ----------
import serial
import time
import tkinter as tk
import winsound
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ---------- SERIAL SETUP ----------
PORT = "COM6"
arduino = serial.Serial(PORT, 9600, timeout=1)
time.sleep(2)


# ---------- DATA ----------
detection_times = []
detection_counts = []
start_time = time.time()
last_detected = False


# ---------- GUI ----------
root = tk.Tk()
root.title("IR Sensor Detection System (Reversed Logic)")
root.attributes("-fullscreen", True)
root.config(bg="#0f1115")
root.bind("<Escape>", lambda e: root.destroy())


# ---------- STYLES ----------
TITLE_FONT = ("Segoe UI", 26, "bold")
STATUS_FONT = ("Segoe UI", 28, "bold")
LABEL_FONT = ("Segoe UI", 18, "bold")

BG = "#0f1115"
PANEL = "#1a1d23"
TEXT = "#e6e6e6"
OK = "#00ff99"
WARN = "#ff3b3b"
INFO = "#4da6ff"


# ---------- LABELS ----------
tk.Label(root, text="IR Sensor Status",
         font=TITLE_FONT, fg=TEXT, bg=BG).pack(pady=20)

status_label = tk.Label(root, text="Reading...",
                        font=STATUS_FONT, fg=INFO, bg=BG)
status_label.pack(pady=10)

sensor1_label = tk.Label(root, text="Sensor 1: ---",
                         font=LABEL_FONT, fg=INFO, bg=BG)
sensor1_label.pack()

sensor2_label = tk.Label(root, text="Sensor 2: ---",
                         font=LABEL_FONT, fg=INFO, bg=BG)
sensor2_label.pack()


# ---------- SOUND ----------
def play_beep():
    winsound.Beep(1000, 200)


# ---------- GRAPH ----------
plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PANEL)

scatter = ax.scatter([], [], s=80)
line_plot, = ax.plot([], [], linewidth=2, alpha=0.8)

ax.set_xlabel("Detection Number", color=TEXT)
ax.set_ylabel("Time (sec)", color=TEXT)
ax.tick_params(colors=TEXT)
ax.set_title("IR Sensor Live Detection", color=TEXT)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=20)


# ---------- SERIAL READ ----------
def read_serial():
    global last_detected

    try:
        line = arduino.readline().decode(errors="ignore").strip()

        if line and "A:" in line and "B:" in line:
            parts = line.split()
            A = int(parts[0].split(":")[1])
            B = int(parts[1].split(":")[1])

            # Sensor display (actual hardware state)
            sensor1_label.config(
                text="Sensor 1: CLEAR" if A else "Sensor 1: DETECTED",
                fg=WARN if A else OK
            )

            sensor2_label.config(
                text="Sensor 2: CLEAR" if B else "Sensor 2: DETECTED",
                fg=WARN if B else OK
            )

            # ---------- REVERSED LOGIC ----------
            # BOTH detected → NO OBJECT
            # Anything else → DETECTED
            detected = not (A == 1 and B == 1)

            if detected:
                status_label.config(text="ANIMAL DETECTED", fg=WARN)
                play_beep()
            else:
                status_label.config(text="NO OBJECT", fg=OK)

            # ---------- GRAPH (count only when DETECTED) ----------
            if detected and not last_detected:
                last_detected = True

                t = time.time() - start_time
                detection_times.append(t)
                detection_counts.append(len(detection_times))

                points = list(zip(detection_counts, detection_times))
                scatter.set_offsets(points)

                colors = plt.cm.plasma(
                    [i / len(points) for i in range(len(points))]
                )
                scatter.set_color(colors)

                line_plot.set_data(detection_counts, detection_times)

                ax.set_xlim(0, max(5, len(points) + 1))
                ax.set_ylim(0, max(detection_times) + 2)

                ax.set_title(
                    f"IR Sensor Live Detection • Total: {len(points)}",
                    color=TEXT
                )

                canvas.draw()

            # Reset when BOTH sensors detect (new NO OBJECT state)
            if A == 1 and B == 1:
                last_detected = False

    except Exception as e:
        print("Error:", e)
        status_label.config(text="ERROR READING", fg=TEXT)

    root.after(50, read_serial)


# ---------- START ----------
read_serial()
root.mainloop()
