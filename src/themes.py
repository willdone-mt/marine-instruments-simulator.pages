def apply_theme(debug=None):
    import tkinter as tk
    from tkinter import ttk

    style = ttk.Style()

    if debug is None:
        style.configure("BW.TPanedwindow", foreground="grey", background="white", relief="raised")
    else:
        style.configure("BW.TPanedwindow", foreground="grey", background="black", relief="raised")

    style.configure("TLabel", foreground="black", background="white", font=("Tahoma", 10, "bold"))
    style.configure("1.TLabel", foreground="black", background="white", font=("Tahoma", 16, "bold"), relief="flat", borderwidth=2)
    style.configure("2.TLabel", foreground="black", background="white", font=("Tahoma", 14, "bold"), relief="flat", borderwidth=2)