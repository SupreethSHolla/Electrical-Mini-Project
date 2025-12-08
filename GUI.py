import serial
import time
import tkinter as tk
import winsound   # sound for Windows

PORT = "COM6"
arduino = serial.Serial(PORT, 9600, timeout=1)
time.sleep(2)

# ---------------- GUI WINDOW ----------------
root = tk.Tk()
root.title("IR Sensor Detection")
root.geometry("500x300")
root.config(bg="#222")

label_title = tk.Label(root, text="IR Sensor Status",
                       font=("Arial", 22, "bold"),
                       fg="white", bg="#222")
label_title.pack(pady=10)

# Main detection label
status_label = tk.Label(root, text="Reading...",
                        font=("Arial", 24, "bold"),
                        fg="yellow", bg="#222")
status_label.pack(pady=10)

# Sensor 1 label
sensor1_label = tk.Label(root, text="Sensor 1: ---",
                         font=("Arial", 18, "bold"),
                         fg="cyan", bg="#222")
sensor1_label.pack(pady=5)

# Sensor 2 label
sensor2_label = tk.Label(root, text="Sensor 2: ---",
                         font=("Arial", 18, "bold"),
                         fg="cyan", bg="#222")
sensor2_label.pack(pady=5)


def play_beep():
    winsound.Beep(1000, 200)


# ---------------- READ SERIAL ----------------
def read_serial():
    try:
        line = arduino.readline().decode().strip()

        if line != "":
            print("Received:", line)

        # Example expected:  "A:1 B:0"
        if "A:" in line and "B:" in line:

            parts = line.split()
            a_val = int(parts[0].split(":")[1])   # 1 or 0
            b_val = int(parts[1].split(":")[1])   # 1 or 0

            # Update individual sensor labels
            if a_val == 1:
                sensor1_label.config(text="Sensor 1: DETECTED", fg="red")
            else:
                sensor1_label.config(text="Sensor 1: CLEAR", fg="lightgreen")

            if b_val == 1:
                sensor2_label.config(text="Sensor 2: DETECTED", fg="red")
            else:
                sensor2_label.config(text="Sensor 2: CLEAR", fg="lightgreen")

            # Overall detection
            if a_val == 1 or b_val == 1:
                status_label.config(text="OBJECT DETECTED", fg="red")
                play_beep()
            else:
                status_label.config(text="NO OBJECT", fg="green")

    except Exception as e:
        print("Error:", e)
        status_label.config(text="Error Reading", fg="white")

    root.after(50, read_serial)


read_serial()
root.mainloop()
