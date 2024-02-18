import os
import time
import tkinter as tk
from tkinter import messagebox

# Global variables to track the remaining time and whether the timer is paused
remaining_time = 0
paused = False
canceled = False

def clear_entries():
    entry_hours.delete(0, tk.END)
    entry_minutes.delete(0, tk.END)

def shutdown_timer():
    global remaining_time
    try:
        hours = int(entry_hours.get()) if entry_hours.get() else 0
        minutes = int(entry_minutes.get()) if entry_minutes.get() else 0
        total_seconds = hours * 3600 + minutes * 60
        if total_seconds == 0:
            clear_entries()  # Clear input fields
            return
        remaining_time = total_seconds
        clear_entries()  # Clear input fields
        countdown()
    except ValueError:
        clear_entries()  # Clear input fields

def countdown():
    global remaining_time, paused, canceled
    canceled = False
    while remaining_time > 0:
        if not paused:
            # Calculate hours, minutes, and seconds
            hours = remaining_time // 3600
            minutes = (remaining_time % 3600) // 60
            seconds = remaining_time % 60
            # Update label to show remaining time
            time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
            label_timer.config(text=time_str)
            root.update()
            time.sleep(1)
            remaining_time -= 1
        else:
            # If paused, just update the GUI
            root.update()
            time.sleep(0.1)

    # When time is up, shut down the computer
    if canceled == False:
        os.system("shutdown /s /t 1")

def pause_timer():
    global paused
    paused = not paused

def cancel_timer():
    global remaining_time, canceled
    canceled = True
    remaining_time = 0
    label_timer.config(text="00:00:00")

# Create the main window
root = tk.Tk()
root.title("Shutdown Timer")

# Create and pack widgets
label_title = tk.Label(root, text="Shut Down Timer\nby Triro", font=("Helvetica", 16))
label_title.grid(row=0, columnspan=2, padx=20, pady=(5,20))

label_hours = tk.Label(root, text="Hours:")
label_hours.grid(row=0+1, column=0, padx=(20,5), pady=5, sticky='w')
entry_hours = tk.Entry(root, width=5)
entry_hours.grid(row=0+1, column=1, padx=(5,20), pady=5, sticky='w')

label_minutes = tk.Label(root, text="Minutes:")
label_minutes.grid(row=1+1, column=0, padx=(20,5), pady=5, sticky='w')
entry_minutes = tk.Entry(root, width=5)
entry_minutes.grid(row=1+1, column=1, padx=(5,20), pady=5, sticky='w')

button_start = tk.Button(root, text="Start Timer", command=shutdown_timer, bg="#4CAF50", fg="white", relief=tk.GROOVE, padx=10, pady=5, width=10, bd=0)
button_start.grid(row=3+1, columnspan=2, padx=20, pady=(20,5))

button_pause = tk.Button(root, text="Pause/Resume", command=pause_timer, bg="#FFC107", fg="white", relief=tk.GROOVE, padx=10, pady=5, width=10, bd=0)
button_pause.grid(row=4+1, columnspan=2, padx=20, pady=5)

button_cancel = tk.Button(root, text="Cancel", command=cancel_timer, bg="#F44336", fg="white", relief=tk.GROOVE, padx=10, pady=5, width=10, bd=0)
button_cancel.grid(row=5+1, columnspan=2, padx=20, pady=5)

label_timer = tk.Label(root, text="00:00:00", font=("Helvetica", 24))
label_timer.grid(row=6+1, columnspan=2, padx=20, pady=(5,20))

# Run the application
root.mainloop()
