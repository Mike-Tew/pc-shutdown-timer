import os
from datetime import datetime, timedelta

from customtkinter import CTk, CTkButton, CTkEntry, CTkFrame, CTkLabel


class Gui(CTk):
    def __init__(self):
        super().__init__()

        self.title("PC Shutdown Timer")
        self.geometry("400x400+900+300")

        display_frame = CTkFrame(self)
        display_frame.pack()
        self.time_label = CTkLabel(display_frame, text="00:00.00")
        self.time_label.pack()

        input_frame = CTkFrame(self)
        input_frame.pack(ipadx=10, ipady=10)
        self.time_entry = CTkEntry(input_frame, placeholder_text="Minutes")
        self.time_entry.grid(row=0, column=0)
        self.set_button = CTkButton(input_frame, text="SET", command=self._on_start)
        self.set_button.grid(row=0, column=1)
        self.reset_button = CTkButton(input_frame, text="RESET", command=self._on_reset)
        self.reset_button.grid(row=0, column=2)
        self.reset_button.config(state="disabled")

    def _on_start(self):
        minutes = int(self.time_entry.get())
        self.shutdown_time = datetime.now() + timedelta(seconds=minutes)
        self.set_button.config(state="disabled")
        self.reset_button.config(state="normal")
        self.update_display()

    def update_display(self):
        remaining_time = self.shutdown_time - datetime.now()
        display_string = str(remaining_time).split(".")[0]
        self.time_label.config(text=display_string)
        self.running_id = self.after(1000, self.update_display)

        if self.shutdown_time < datetime.now():
            self.shutdown()
            self.after_cancel(self.running_id)

    def _on_reset(self):
        self.after_cancel(self.running_id)
        self.set_button.config(state="normal")
        self.time_label.config(text="00:00.00")

    def shutdown(self):
        print("Shutting Down")
        self.time_label.config(text="Shutdown")
        # os.system("shutdown /s /t 0")


if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()
