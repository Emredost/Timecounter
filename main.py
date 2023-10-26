import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        self.master.geometry("300x200")

        self.label = tk.Label(self.master, text="Set Countdown (seconds):")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.start_button = tk.Button(self.master, text="Start Countdown", command=self.start_countdown)
        self.start_button.pack()

        self.stop_button = tk.Button(self.master, text="Stop Countdown", command=self.stop_countdown, state=tk.DISABLED)
        self.stop_button.pack()

        self.remaining_time = 0
        self.countdown_active = False

    def start_countdown(self):
        try:
            self.remaining_time = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of seconds.")
            return

        self.countdown_active = True
        self.start_button["state"] = tk.DISABLED
        self.stop_button["state"] = tk.NORMAL
        self.update_countdown()

    def stop_countdown(self):
        self.countdown_active = False
        self.start_button["state"] = tk.NORMAL
        self.stop_button["state"] = tk.DISABLED

    def update_countdown(self):
        if self.countdown_active and self.remaining_time > 0:
            self.label.config(text=f"Time Left: {self.remaining_time} seconds")
            self.remaining_time -= 1
            self.master.after(1000, self.update_countdown)
        elif self.countdown_active:
            self.label.config(text="Time's up!")
            self.stop_countdown()

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
