import serial
import time
import tkinter as tk
import winsound   # <-- sound module for Windows

PORT = "COM6"
arduino = serial.Serial(PORT, 9600, timeout=1)
time.sleep(2)

# GUI Window
root = tk.Tk()
root.title("IR Sensor Detection")
root.geometry("350x180")
root.config(bg="#222")

label_title = tk.Label(root, text="IR Sensor Status",
                       font=("Arial", 18, "bold"), fg="white", bg="#222")
label_title.pack(pady=10)

status_label = tk.Label(root, text="Reading...",
                        font=("Arial", 22, "bold"),
                        fg="yellow", bg="#222")
status_label.pack(pady=10)


def play_beep():
    # frequency, duration (ms)
    winsound.Beep(1000, 200)   # 1000 Hz for 200 ms


def read_serial():
    try:
        line = arduino.readline().decode().strip()

        if line == "Object Detected!":
            status_label.config(text="OBJECT DETECTED", fg="red")
            print("Object Detected!")
            play_beep()  # <<--- Play sound here!

        elif line == "No Object Detected":
            status_label.config(text="NO OBJECT", fg="green")
            print("No Object Detected")

    except:
        status_label.config(text="Error Reading", fg="white")
        print("Error Reading")

    root.after(100, read_serial)


read_serial()
root.mainloop()
