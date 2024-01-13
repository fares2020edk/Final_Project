import time
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
class CountdownTimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Countdown Timer")
        master.configure(bg="lightgreen")

        # Create and place widgets in the window
        Label(master, text="Enter hours:",font=(14)).grid(row=0, column=0, padx=10, pady=10)
        Label(master, text="Enter minutes:",font=(14)).grid(row=1, column=0, padx=10, pady=10)
        Label(master, text="Enter seconds:",font=(14)).grid(row=2, column=0, padx=10, pady=10)

        self.entry_hours = Entry(master)
        self.entry_hours.grid(row=0, column=1, padx=10, pady=10)

        self.entry_minutes = Entry(master)
        self.entry_minutes.grid(row=1, column=1, padx=10, pady=10)

        self.entry_seconds = Entry(master)
        self.entry_seconds.grid(row=2, column=1, padx=10, pady=10)

        self.start_button = Button(master, text="Start Timer", command=self.start_timer)
        self.start_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.timer_label = Label(master, text="")
        self.timer_label.grid(row=4, column=0, columnspan=2, pady=10)

    def hMS(self, hr, min, seconds):
        total_seconds = (seconds + (min * 60) + (hr * (60 * 60)))
        return total_seconds

    def countdown_timer(self, seconds):
        for remaining_time in range(seconds, 0, -1):
            time_str = f"Time remaining: {remaining_time} seconds"
            self.timer_label.config(text=time_str)
            self.timer_label.update()
            time.sleep(1)

        self.timer_label.config(text="Time's up! Timer expired.")
        messagebox.showinfo("Timer Expired", "Time's up! Timer expired.")

    def start_timer(self):
        try:
            hours = int(self.entry_hours.get())
            minutes = int(self.entry_minutes.get())
            seconds = int(self.entry_seconds.get())
            time_input = self.hMS(hours, minutes, seconds)
            self.countdown_timer(time_input)
        except ValueError:
            self.timer_label.config(text="Please enter valid numbers for the timer.")
            messagebox.showerror("Invalid Input", "Please enter valid numbers for the timer.")


