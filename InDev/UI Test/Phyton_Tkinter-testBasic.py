# Import the Tkinter module from the Python standard library.
# We alias it as "tk" for concise access to widget classes and functions (e.g., tk.Label, tk.Entry).
import tkinter as tk

# Define a callback function that will be executed when the button is clicked.
# - It reads the current text from the Entry widget (entry.get()).
# - It updates the Label widget's text using label.config(...).
# Note:
# - Widgets are Python objects; we can modify their properties at runtime.
# - f-string is used to interpolate the user's input into the greeting.
def greet():
    label.config(text=f"Hello, {entry.get()}!")

# Create the main application window (the "root" of all Tkinter widgets).
# - tk.Tk() initializes the Tk interpreter and creates a top-level window.
# - This window hosts all other widgets we add.
root = tk.Tk()

# Set the window's title (displayed in the title bar by the OS).
root.title("Interactive Tkinter Example")

# Create a Label widget to show static text initially.
# - Parent is "root", meaning the label will be placed inside the main window.
# - The "text" parameter sets the initial content displayed.
label = tk.Label(root, text="Enter your name:")

# Lay out the Label in the window using the "pack" geometry manager.
# - pack() places the widget sequentially (top to bottom by default).
# - Tkinter has three geometry managers: pack, grid, and place.
label.pack()

# Create an Entry widget to accept user input (single line text field).
# - Parent is "root".
entry = tk.Entry(root)

# Lay out the Entry below the Label (because pack stacks them in creation order).
entry.pack()

# Create a Button widget that the user can click to trigger the "greet" function.
# - "text" sets the label shown on the button.
# - "command=greet" wires the button's click event to our greet() callback.
button = tk.Button(root, text="Greet Me", command=greet)

# Lay out the Button below the Entry.
button.pack()

# Start Tkinter's event loop (also called the "main loop").
# - This loop listens for events (mouse clicks, key presses, window actions).
# - It keeps the window responsive until the user closes it or the program exits.
# - Without mainloop(), the window would appear and immediately close.
root.mainloop()
