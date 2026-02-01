import tkinter as tk
from tkinter import ttk

# Can we make these rows between =#=== as an external module file? 
# =#====

# defining functions =====

title = "general_instrument_ui"
# =====

# HOW TO MAKE EVERY PLACEMENT RELATIVE AND RESPECTIVE TO  WINDOW SIZE AND A VALUE???

# Main TKinter functions =====
# Main Window
root = tk.Tk()
root.title(title)
root.geometry("1760x990")
root.resizable(False, False)

# ttk Style
style = ttk.Style()
style.configure("BW.TPanedwindow", foreground="grey", background="white", relief="raised")
style.configure("TLabel", foreground="black", background="white")
style.configure("1.TLabel", foreground="black", background="white", font=("Helvetica", 16, "bold"), relief="flat", borderwidth=2)
style.configure("2.TLabel", foreground="black", background="white", font=("Helvetica", 14, "bold"), relief="flat", borderwidth=2)

# Paned Windows
paned_buttons = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_buttons.place(relx=0.01, y=80, anchor="nw")
paned_buttons.config(width=250, height=150, style="BW.TPanedwindow")

paned_info = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_info.place(relx=0.01, rely=0.5, anchor="nw")
paned_info.config(width=250, height=150, style="BW.TPanedwindow")

paned_main = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_main.place(relx=0.5, y=80, anchor="n") 
paned_main.config(width=1100, height=640, style="BW.TPanedwindow")

paned_labels = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_labels.place(relx=0.5, rely=0.95, anchor="s")
paned_labels.config(width=1100, height=150, style="BW.TPanedwindow")
# =====

# Widgets =====

# Titles
label_title = ttk.Label(root, text=f"===== {title} =====", style="1.TLabel")
label_title.place(relx=0.5, y=10, anchor='center')

label_title_paned_buttons = ttk.Label(root, text="=== Actions ===", style="2.TLabel")
label_title_paned_buttons.place(relx=0.01, y=40, anchor='nw')

label_title_paned_main = ttk.Label(root, text="=== Main Window ===", style="2.TLabel")
label_title_paned_main.place(relx=0.5, y=40, anchor='n')

label_title_paned_labels = ttk.Label(root, text="=== Status Messages ===", style="2.TLabel")
label_title_paned_labels.place(relx=0.5, rely=0.78, anchor='s')

# Texts
label1 = ttk.Label(paned_labels, text="Lid Status")
label_message = ttk.Label(paned_labels, text="Hand Refractometer Simulator")
label_value = ttk.Label(paned_main, text="What Value do you get?")

label_group1 = ttk.Label(paned_buttons, text="=== Grouped Actions 1 ===", style="TLabel")
label_group2 = ttk.Label(paned_buttons, text="=== Grouped Actions 2 ===", style="TLabel")
label_group3 = ttk.Label(paned_buttons, text="=== Grouped Actions 3 ===", style="TLabel")

# Buttons.
button1 = ttk.Button(paned_buttons, text="button1")
button2 = ttk.Button(paned_buttons, text="button2")
button3 = ttk.Button(paned_buttons, text="button3")
button4 = ttk.Button(paned_buttons, text="button4")
button5 = ttk.Button(paned_buttons, text="button5")
buttonValue = ttk.Button(paned_buttons, text="buttonValue")
# =====

# =#====

# Layouts =====

# paned_labels group
label_message.place(x=10, y=10)
label1.place(x=10, y=50)
label_value.place(relx=0.5, rely=0.5, anchor="center")

# paned_buttons group
label_group1.grid(row=0, column=0, padx=5, columnspan=3, sticky="w")
button1.grid(row=1, column=0, padx=5, pady=5)
button2.grid(row=1, column=1, padx=5, pady=5)
button3.grid(row=2, column=0, padx=5, pady=5)
button4.grid(row=2, column=1, padx=5, pady=5)
button5.grid(row=2, column=2, padx=5, pady=5)
buttonValue.grid(row=3, column=0, padx=5, pady=5)

label_group2.grid(row=4, column=0, padx=5, columnspan=3, sticky="w")
label_group3.grid(row=5, column=0, padx=5, columnspan=3, sticky="w")
# =====

root.mainloop()