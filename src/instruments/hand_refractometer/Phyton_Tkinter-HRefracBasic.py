import tkinter as tk
from tkinter import ttk
import command_definitions as cd
import value_generator as vg

# Can we make these rows between =#=== as an external module file? 
# =#====

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

# =====

# Main TKinter functions =====
# Main Window
root = tk.Tk()
root.title("HandRefractometer MVP Simulator")
root.geometry("600x300")
root.resizable(False, False)

# ttk Style
style = ttk.Style()
style.configure("BW.TPanedwindow", foreground="grey", background="white", relief="raised")
style.configure("TLabel", foreground="black", background="white")

# Paned Windows
paned_labels = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_labels.place(relx=1, anchor="ne") 
paned_labels.config(width=300, height=150, style="BW.TPanedwindow")

paned_buttons = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_buttons.place(relx=0, anchor="nw")
paned_buttons.config(width=250, height=150, style="BW.TPanedwindow")
# =====

# Widgets =====

# Texts
label_message = ttk.Label(paned_labels, text="Hand Refractometer Simulator")
label_lid = ttk.Label(paned_labels, text="Lid Status")
label_value = ttk.Label(paned_labels, text="What Value do you get?")

label_group_func = ttk.Label(paned_buttons, text="=== Instrument Functionality ===", style="TLabel")
label_group_drop = ttk.Label(paned_buttons, text="=== Drops ===", style="TLabel")
label_group_value = ttk.Label(paned_buttons, text="=== View Value ===", style="TLabel")

# Buttons.
button_open_lid = ttk.Button(paned_buttons, text="Open Lid", command=open_lid)
button_close_lid = ttk.Button(paned_buttons, text="Close Lid", command=close_lid)
button_calibrate = ttk.Button(paned_buttons, text="Calibrate", command=calibration)
button_wipe = ttk.Button(paned_buttons, text="Wipe Lens", command=wipe_lens)
button_sample = ttk.Button(paned_buttons, text="Sample", command=sample)
button_peek = ttk.Button(paned_buttons, text="Peek", command=peek)
# =====

# =#====

# Layouts =====

# paned_labels group
label_message.place(x=10, y=10)
label_lid.place(x=10, y=50)
label_value.place(x=10, y=70)

# paned_buttons group
label_group_func.grid(row=0, column=0, padx=5, columnspan=3)
button_open_lid.grid(row=1, column=0, padx=5, pady=5)
button_close_lid.grid(row=1, column=1, padx=5, pady=5)
button_wipe.grid(row=3, column=2, padx=5, pady=5)

label_group_drop.grid(row=2, column=0, padx=5, columnspan=3)
button_calibrate.grid(row=3, column=0, padx=5, pady=5)
button_sample.grid(row=3, column=1, padx=5, pady=5)

label_group_value.grid(row=4, column=0, padx=5, columnspan=3)
button_peek.grid(row=5, column=0, padx=5, pady=10)
# =====

root.mainloop()