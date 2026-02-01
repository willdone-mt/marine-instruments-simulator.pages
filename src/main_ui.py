import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import tkinter as tk
from tkinter import ttk
import subprocess as sp
import webbrowser as wb

from instruments.handrefractometer import handrefractometer_ui  

'''
Problems: 
- master.py malah menjalankan import di directorynya dan bukan directory modul2nya
- ketika handrefractometer_ui dijalankan dari master.py, handrefractometer_ui kehilangan ttk-nya
    - troubleshooted, masalahnya ada di master.py, tapi belum tau bagaimana pastinya
'''

ascii_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⠾⠿⠿⠯⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣾⠛⠁⠀⠀⠀⠀⠀⠀⠈⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠁⠀⠀⠀⢀⣤⣾⣟⣛⣛⣶⣬⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⠃⠀⠀⠀⠀⠀⣾⣿⠟⠉⠉⠉⠉⠛⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠋⠀⠀⠀⠀⠀⠀⠀⣿⡏⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣤⣤⣠⣤⣤⡤⡶⣶⢿⠟⠹⠿⠄⣿⣿⠏⠀⣀⣤⡦⠀⠀⠀⠀⣀⡄
⢀⣄⣠⣶⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠓⠚⠋⠉⠀⠀⠀⠀⠀⠀⠈⠛⡛⡻⠿⠿⠙⠓⢒⣺⡿⠋⠁
⠉⠉⠉⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀🐋
"""

def open_news():
    wb.open("https://github.com/willdone-mt/marine-instruments-simulator.pages/tree/main/docs#readme")

def open_githubissue():
    wb.open("https://github.com/willdone-mt/marine-instruments-simulator.pages/issues")

def run_handrefractometer_ui():
    handrefractometer_ui.run_ui(root)

# Main TKinter functions =====

# Main Window
root = tk.Tk()
root.title("SIRENIA - Home Menu")
root.geometry("800x600")

# ttk Style
style = ttk.Style()
style.configure("BW.TPanedwindow", foreground="grey", background="white", relief="raised")
style.configure("TLabel", foreground="black", background="white", font=("Calibri", 10, "bold"))
style.configure("1.TLabel", foreground="black", background="white", font=("Verdana", 16, "bold"), relief="flat", borderwidth=2)
style.configure("2.TLabel", foreground="black", background="white", font=("Verdana", 14, "bold"), relief="flat", borderwidth=2)

# =====

# Paned Windows

paned_home = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_home.place(relx=0.1, y=100, anchor="nw", width=300, height=200)
paned_home.config(style="BW.TPanedwindow")

paned_main = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_main.place(relx=0.9, y=100, anchor="ne", width=300, height=200)
paned_main.config(style="BW.TPanedwindow")

# Widgets =====



# Titles
label_title = ttk.Label(root, text="---====={([ SIRENIA ])}=====---", style="1.TLabel")
label_title.place(relx=0.5, y=15, anchor='center')
label_subtitle = ttk.Label(root, text="=== Home Menu ===", style="2.TLabel")
label_subtitle.place(relx=0.5, y=60, anchor='center')

# Labels
label_home = ttk.Label(paned_home, text="Welcome!", style="TLabel")
label_instruments = ttk.Label(paned_main, text="Select an Instrument to Simulate:", style="TLabel")


# Buttons
button_run_hand_refractometer = ttk.Button(paned_main, text="Hand Refractometer", command=run_handrefractometer_ui)
button_WIP = ttk.Button(paned_main, text="WIP Instrument", command=lambda: print("WIP Instrument UI not yet implemented"))

button_news = ttk.Button(paned_home, text="News↗️", command=open_news)
button_reportGitHub = ttk.Button(paned_home, text="Report via GitHub↗️", command=open_githubissue)

label_instruments.pack(anchor='n', pady=10)
button_run_hand_refractometer.pack(anchor='n', pady=10)
button_WIP.pack(anchor='n', pady=10)

label_home.pack(anchor='n', pady=10)
button_news.pack(anchor='n', pady=10)
button_reportGitHub.pack(anchor='n', pady=10)

canvas = tk.Canvas(root, width=800, height=600)
canvas.create_text(400, 300, text=ascii_art, font=("consolas", 12), anchor="s")
canvas.place(relx=0.5, rely=1, anchor="center")

#
root.mainloop()