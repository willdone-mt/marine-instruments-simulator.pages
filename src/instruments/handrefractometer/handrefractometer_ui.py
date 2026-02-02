import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from main import general_instrument_ui

try:
    from .handrefractometer_module import command_definitions as cd
except ImportError:
    from handrefractometer_module import command_definitions as cd

def run_ui(parent_root=None):

    # defining functions =====
    def open_lid():
        message, closedLid = cd.open_lid()
        label_lid.config(text=f"Lid is Closed: {closedLid}")
        label_message.config(text=f"{message}")

    def close_lid():
        message, closedLid = cd.close_lid()
        label_lid.config(text=f"Lid is Closed: {closedLid}")
        label_message.config(text=f"{message}")

    def calibration():
        message, closedLid, calibrated, wiped = cd.calibrate()
        label_lid.config(text=f"Lid is Closed: {closedLid}")
        label_message.config(text=message)

    def wipe_lens():
        message = cd.wipe()
        label_message.config(text=message)

    def sample():
        message = cd.sample()
        label_message.config(text=message)

    def peek():
        message, value = cd.peek()
        label_message.config(text=message)
        if value == False and value != 0:
            label_lid.config(text="Lid is still opened")
        else:
            label_value.config(text=f"You got the number {value}")

    def test_run():
        print("hand_refractometer is running")

    # =====

    # HOW TO MAKE EVERY PLACEMENT RELATIVE AND RESPECTIVE TO  WINDOW SIZE AND A VALUE???

    # Main TKinter functions =====
    # Main Window

    # Can we make these rows between =#=== as an external module file? 
    # =#====
    if parent_root is None:
        ui_root = ThemedTk(theme="scidblue")
    else:
        ui_root = tk.Toplevel(parent_root)

    ui_root.title("HandRefractometer MVP Simulator")
    ui_root.geometry("1760x990")

    title = "Hand Refractometer"
    paned_buttons, paned_HRmain, paned_info, paned_labels = general_instrument_ui.run_instrument_ui(ui_root, title)

    # Widgets ===== Some of the widgets can be modulized

    # Titles




    label_title_paned_HRmain = ttk.Label(ui_root, text="=== Main Window ===", style="2.TLabel")
    label_title_paned_HRmain.place(relx=0.5, y=40, anchor='n')

    label_title_paned_labels = ttk.Label(ui_root, text="=== Status Messages ===", style="2.TLabel")
    label_title_paned_labels.place(relx=0.5, rely=0.78, anchor='s')

    # Texts
    label_message = ttk.Label(paned_labels, text="Hand Refractometer Simulator")
    label_lid = ttk.Label(paned_labels, text="Lid Status")
    label_value = ttk.Label(paned_HRmain, text="What Value do you get?")

    label_group_func = ttk.Label(paned_buttons, text="Instrument Mechanism ===", style="TLabel")
    label_group_drop = ttk.Label(paned_buttons, text="Drops ===", style="TLabel")
    label_group_value = ttk.Label(paned_buttons, text="View Value ===", style="TLabel")

    # Buttons.
    button_open_lid = ttk.Button(paned_buttons, text="Open Lid", command=open_lid)
    button_close_lid = ttk.Button(paned_buttons, text="Close Lid", command=close_lid)
    button_calibrate = ttk.Button(paned_buttons, text="Calibrate", command=calibration)
    button_wipe = ttk.Button(paned_buttons, text="Wipe Lens", command=wipe_lens)
    button_sample = ttk.Button(paned_buttons, text="Sample", command=sample)
    button_peek = ttk.Button(paned_buttons, text="Peek", command=peek)
    # =====


    # Layouts ===== maybe these parameter layouts can be modulized

    # paned_HRmain group
    label_message.place(x=10, y=10)
    label_lid.place(x=10, y=50)
    label_value.place(relx=0.5, rely=0.5, anchor="center")

    # paned_buttons group 

    label_group_func.grid(row=0, column=0, padx=5, columnspan=3, sticky="w")
    button_open_lid.grid(row=1, column=0, padx=5, pady=5)
    button_close_lid.grid(row=1, column=1, padx=5, pady=5)
    button_wipe.grid(row=3, column=2, padx=5, pady=5)

    label_group_drop.grid(row=2, column=0, padx=5, columnspan=3, sticky="w")
    button_calibrate.grid(row=3, column=0, padx=5, pady=5)
    button_sample.grid(row=3, column=1, padx=5, pady=5)

    label_group_value.grid(row=4, column=0, padx=5, columnspan=3, sticky="w")
    button_peek.grid(row=5, column=0, padx=5, pady=10)
    # =====

    ui_root.mainloop()

if __name__ == "__main__": 
    run_ui()