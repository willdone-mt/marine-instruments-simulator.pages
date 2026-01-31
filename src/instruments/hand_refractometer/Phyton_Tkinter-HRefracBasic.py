import tkinter as tk
from tkinter import ttk
import command_definitions as cd
import value_generator as vg

# Can we make these rows between =#=== as an external module file? 
# =#====

# defining functions =====
def open_lid():
    message, closedLid = cd.open_lid()
    label_message.config(text=f"{message}")

def close_lid():
    message, closedLid = cd.close_lid()
    label_message.config(text=f"{message}")

def calibration():
    message, closedLid, calibrated, wiped = cd.calibrate()
    label_message.config(text=message)

def wipe_lens():
    message = cd.wipe()
    label_message.config(text=message)

def sample():
    message = cd.sample()
    label_message.config(text=message)

def peek():
    cd.peek()
    message, value = cd.peek()
    label_message.config(text=message)
    label_value.config(text=f"You got the number {value}")

# =====

# Main TKinter functions =====
# Windows
root = tk.Tk()
# Window Title
root.title("HandRefractometer Tkinter Example")

# ttk Style
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
# =====

# Widgets =====
# Texts
label_message = ttk.Label(root, text="Hand Refractometer Simulator")
# label_lid = ttk.Label(root, text="Hand Refractometer Lid Status")
# label_calibration = ttk.Label(root, text="Calibration Status")
label_value = ttk.Label(root, text="What Value do you got?")

# Buttons.
button_open_lid = ttk.Button(root, text="Open Lid", command=open_lid)
button_close_lid = ttk.Button(root, text="Close Lid", command=close_lid)
button_calibrate = ttk.Button(root, text="Calibrate", command=calibration)
button_wipe = ttk.Button(root, text="Wipe Lens", command=wipe_lens)
button_sample = ttk.Button(root, text="Sample", command=sample)
button_peek = ttk.Button(root, text="Peek", command=peek)
# =====

# =#====

# Layouts =====
# Lay out the Label in the window using the "pack" geometry manager.
# - pack() places the widget sequentially (top to bottom by default).
# - Tkinter has three geometry managers: pack, grid, and place.

label_message.pack(side='left')
# label_lid.pack(side='left')
label_value.pack(side='right')

button_open_lid.pack()
button_close_lid.pack() 
button_calibrate.pack()
button_wipe.pack()
button_sample.pack()
button_peek.pack()

# =====


# Debug Window =====
'''
debug = tk.Tk()
debug.title("Debug Window")

debugLabel_lid = ttk.Label(debug, text=(f"closedLid:{cd.close_lid}"))

debugLabel_lid.pack()


# =====

debug.mainloop()
'''
root.mainloop()