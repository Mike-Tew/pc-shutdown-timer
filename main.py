import os
from datetime import datetime, timedelta

from customtkinter import CTk, CTkButton, CTkEntry, CTkFrame, CTkLabel


class Gui(CTk):
    def __init__(self):
        super().__init__()

        self.set_appearance_mode("dark")
        self.title("PC Shutdown Timer")
        self.geometry("455x170")
        self.resizable(False, False)

        display_frame = CTkFrame(self)
        display_frame.pack(pady=10)
        self.time_label = CTkLabel(display_frame, width=300, text="00:00.00", text_font=("Roboto Medium", 20))
        self.time_label.pack(ipady=10)

        input_frame = CTkFrame(self, fg_color="grey12")
        input_frame.pack(padx=20, pady=20)
        self.time_entry = CTkEntry(input_frame, placeholder_text="Minutes")
        self.time_entry.grid(row=0, column=0, padx=10)
        self.set_button = CTkButton(input_frame, text="SET", command=self._on_start)
        self.set_button.grid(row=0, column=1, padx=10)
        self.reset_button = CTkButton(input_frame, text="RESET", command=self._on_reset)
        self.reset_button.grid(row=0, column=2, padx=10)
        self.reset_button.config(state="disabled")

    def _on_start(self):
        try:
            minutes = int(self.time_entry.get())
        except:
            self.time_label.config(text="Invalid Time")
            return

        self.shutdown_time = datetime.now() + timedelta(minutes=minutes)
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
        self.time_label.config(text="Shutdown")
        os.system("shutdown /s /t 0")


if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()
