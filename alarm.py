# Import Required Libraries
from tkinter import *
import datetime
import time
import subprocess
from threading import Thread

# Create Window
root = Tk()
root.title("Alarm Clock")
root.geometry("400x200")

# Alarm Thread
def start_alarm_thread():
    t1 = Thread(target=alarm, daemon=True)
    t1.start()

import subprocess

def play_sound():
    subprocess.run([
        "afplay",
        "/System/Library/Sounds/Glass.aiff"
    ])

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        time.sleep(1)

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        if current_time == set_alarm_time:
            print("Time to Wake Up!")

            # Play alarm sound
            play_sound()
            break

# UI Elements
Label(
    root,
    text="Alarm Clock",
    font=("Helvetica", 20, "bold"),
    fg="red"
).pack(pady=10)

Label(
    root,
    text="Set Time",
    font=("Helvetica", 15, "bold")
).pack()

frame = Frame(root)
frame.pack()

# Hours
hour = StringVar(root)
hours = [f"{i:02d}" for i in range(24)]
hour.set(hours[0])

OptionMenu(frame, hour, *hours).pack(side=LEFT)

# Minutes
minute = StringVar(root)
minutes = [f"{i:02d}" for i in range(60)]
minute.set(minutes[0])

OptionMenu(frame, minute, *minutes).pack(side=LEFT)

# Seconds
second = StringVar(root)
seconds = [f"{i:02d}" for i in range(60)]
second.set(seconds[0])

OptionMenu(frame, second, *seconds).pack(side=LEFT)

Button(
    root,
    text="Set Alarm",
    font=("Helvetica", 15),
    command=start_alarm_thread
).pack(pady=20)

root.mainloop()