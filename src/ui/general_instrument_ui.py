import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import tkinter as tk
from tkinter import ttk
from src import themes as th

def run_instrument_ui(root, title):
    # ttk Style
    th.apply_theme()

    # Paned Windows
    
    paned_buttons = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
    paned_buttons.place(relx=0.01, y=80, anchor="nw", relwidth=0.17, relheight=0.5,  bordermode="outside")
    paned_buttons.config(style="BW.TPanedwindow")

    paned_info = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
    paned_info.place(relx=0.01, rely=0.65, anchor="nw", relwidth=0.17, relheight=0.3)
    paned_info.config( style="BW.TPanedwindow")

    paned_HRmain = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
    paned_HRmain.place(relx=0.2, y=80, anchor="nw", relwidth=0.65, relheight=0.65, bordermode="outside") 
    paned_HRmain.config(style="BW.TPanedwindow")

    paned_labels = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
    paned_labels.place(relx=0.2, rely=0.8, anchor="nw", relwidth=0.65, relheight=0.15)
    paned_labels.config(style="BW.TPanedwindow")
    # =====

    title_ALLCAPS = title.upper()
    label_title = ttk.Label(root, text=f"===== {title_ALLCAPS} =====", style="1.TLabel")
    label_title.place(relx=0.5, y=10, anchor='center')

    label_title_paned_buttons = ttk.Label(root, text="=== Actions ===", style="2.TLabel")
    label_title_paned_buttons.place(relx=0.01, y=40, anchor='nw')

    label_title_paned_HRmain = ttk.Label(root, text="=== Main Window ===", style="2.TLabel")
    label_title_paned_HRmain.place(relx=0.5, y=40, anchor='n')

    return paned_buttons, paned_HRmain, paned_info, paned_labels

if __name__ == "__main__": 
    root = tk.Tk()
    root.title("HandRefractometer MVP Simulator")
    root.geometry("1760x990")

    run_instrument_ui(root, "test")
    root.mainloop()