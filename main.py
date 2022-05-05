import datetime
import time
import tkinter as tk

from customtkinter import CTk, CTkButton, CTkEntry, CTkFrame, CTkLabel


class Gui(CTk):
    def __init__(self):
        super().__init__()

        self.title("PC Shutdown Timer")
        self.geometry("400x400+900+300")
        self.completion_time = 0

        display_frame = CTkFrame(self)
        display_frame.pack()
        self.time_label = CTkLabel(display_frame, text="00:00.00")
        self.time_label.pack()

        input_frame = CTkFrame(self)
        input_frame.pack(ipadx=10, ipady=10)
        time_entry = CTkEntry(input_frame, placeholder_text="Minutes")
        time_entry.grid(row=0, column=0)
        CTkButton(input_frame, text="SET", command=self.display_time).grid(
            row=0, column=1
        )
        CTkButton(input_frame, text="RESET", command=self._on_reset).grid(
            row=0, column=2
        )

    def display_time(self):
        self.completion_time = time.time() + 200
        print(self.completion_time.strftime("%H:%M:%S"))
        self.update_display()

    def update_display(self):
        remaining_time = self.completion_time -  time.time()
        display_string = "123"
        self.time_label["text"] = remaining_time
        self.completion_time += 1
        self.after(1000, self.update_display)

    def _on_reset(self):
        print("Reset")


if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()
