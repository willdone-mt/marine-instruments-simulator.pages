"""
A fully interactive Tkinter app demonstrating:
- Window, frames, layout (pack + grid)
- Menus, status bar
- Form inputs (Entry, Radiobutton, Checkbutton, Combobox)
- Buttons with commands
- Validation and dynamic state updates
- Canvas drawing
- Keyboard and mouse event bindings
- Message boxes and file dialogs
"""

import tkinter as tk                 # Core Tkinter module
from tkinter import ttk              # Themed widgets (modern look)
from tkinter import messagebox       # Standard message dialogs
from tkinter import filedialog       # Open/save file dialogs

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # ----- Window basics -----
        self.title("Interactive Tkinter Demo")
        self.geometry("700x500")     # Width x Height (in pixels)
        self.minsize(600, 450)       # Prevent overly small window

        # Keep a simple app state dictionary (shared across handlers)
        self.state = {
            "name": "",
            "language": tk.StringVar(value="Python"),
            "subscribe": tk.BooleanVar(value=True),
            "mode": tk.StringVar(value="Beginner"),
            "status": tk.StringVar(value="Ready"),
        }

        # ----- Configure global styles for ttk -----
        style = ttk.Style(self)
        # Use a built-in theme for a modern baseline (e.g., "clam")
        style.theme_use("clam")
        style.configure("TButton", padding=6)
        style.configure("TLabel", padding=3)
        style.configure("TCheckbutton", padding=3)
        style.configure("TRadiobutton", padding=3)

        # ----- Build UI -----
        self._build_menu()
        self._build_main()
        self._build_statusbar()

        # ----- Bind global events -----
        # Keyboard shortcut: Ctrl+S to "Save" (simulate saving state)
        self.bind_all("<Control-s>", self.on_save_shortcut)
        # Press Enter to trigger greet button
        self.bind_all("<Return>", self.on_enter_key)
        # Update status on window resize (shows interactivity with events)
        self.bind("<Configure>", self.on_window_resize)

    # ------------------ Menu bar ------------------
    def _build_menu(self):
        # Top-level menu container
        menubar = tk.Menu(self)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label="Open...", command=self.on_open_file)
        file_menu.add_command(label="Save", command=self.on_save)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_exit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=False)
        help_menu.add_command(label="About", command=self.on_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        # Attach to window
        self.config(menu=menubar)

    # ------------------ Main content ------------------
    def _build_main(self):
        # Root container frame with padding
        container = ttk.Frame(self, padding=12)
        container.pack(fill="both", expand=True)

        # Split the UI into left (form) and right (canvas) panels
        left = ttk.Frame(container)
        right = ttk.Frame(container)
        left.pack(side="left", fill="both", expand=True)
        right.pack(side="right", fill="both", expand=True)

        # ----- LEFT: Form panel -----
        # We’ll use grid for tidy alignment in the form
        form = ttk.LabelFrame(left, text="Profile setup", padding=10)
        form.pack(fill="x", padx=6, pady=6)

        # Row 0: Name label + entry
        ttk.Label(form, text="Name").grid(row=0, column=0, sticky="w")
        # StringVar to mirror entry text; storing also in self.state for easy access
        self.name_var = tk.StringVar()
        name_entry = ttk.Entry(form, textvariable=self.name_var, width=30)
        name_entry.grid(row=0, column=1, sticky="we", padx=6)
        # Status hint (dynamic label)
        self.name_hint = ttk.Label(form, text="Type your name and press Enter")
        self.name_hint.grid(row=0, column=2, sticky="w")

        # Make column 1 grow as window expands (nice responsive layout)
        form.columnconfigure(1, weight=1)

        # Row 1: Language selection (Combobox)
        ttk.Label(form, text="Favorite language").grid(row=1, column=0, sticky="w", pady=(6, 0))
        self.lang_combo = ttk.Combobox(
            form,
            textvariable=self.state["language"],
            values=["Python", "JavaScript", "Go", "Rust", "Java", "C#"],
            state="readonly"
        )
        self.lang_combo.grid(row=1, column=1, sticky="we", padx=6, pady=(6, 0))
        # Bind selection change to update status
        self.lang_combo.bind("<<ComboboxSelected>>", self.on_language_changed)

        # Row 2: Mode (Radiobuttons)
        ttk.Label(form, text="Mode").grid(row=2, column=0, sticky="w", pady=(6, 0))
        modes = ["Beginner", "Intermediate", "Advanced"]
        mode_frame = ttk.Frame(form)
        mode_frame.grid(row=2, column=1, sticky="w", padx=6, pady=(6, 0))
        for i, m in enumerate(modes):
            ttk.Radiobutton(
                mode_frame, text=m, value=m, variable=self.state["mode"], command=self.on_mode_changed
            ).grid(row=0, column=i, padx=4)

        # Row 3: Subscribe (Checkbutton)
        subscribe_btn = ttk.Checkbutton(
            form,
            text="Subscribe to tips",
            variable=self.state["subscribe"],
            command=self.on_subscribe_toggled
        )
        subscribe_btn.grid(row=3, column=1, sticky="w", padx=6, pady=(6, 0))

        # Row 4: Buttons
        button_frame = ttk.Frame(form)
        button_frame.grid(row=4, column=0, columnspan=3, sticky="we", pady=10)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)

        self.greet_btn = ttk.Button(button_frame, text="Greet", command=self.on_greet)
        self.greet_btn.grid(row=0, column=0, sticky="we", padx=6)

        self.clear_btn = ttk.Button(button_frame, text="Clear", command=self.on_clear)
        self.clear_btn.grid(row=0, column=1, sticky="we", padx=6)

        self.draw_btn = ttk.Button(button_frame, text="Draw on canvas", command=self.on_draw_canvas)
        self.draw_btn.grid(row=0, column=2, sticky="we", padx=6)

        # A result area to show messages (dynamic label)
        self.result_label = ttk.Label(left, text="Welcome! Adjust settings and click Greet.", anchor="w")
        self.result_label.pack(fill="x", padx=6, pady=(0, 6))

        # ----- RIGHT: Canvas panel -----
        canvas_frame = ttk.LabelFrame(right, text="Canvas playground", padding=10)
        canvas_frame.pack(fill="both", expand=True, padx=6, pady=6)

        # Create a resizable canvas
        self.canvas = tk.Canvas(canvas_frame, background="#fafafa")
        self.canvas.pack(fill="both", expand=True)

        # Bind mouse interactions on canvas
        # Left-click draws a small dot; drag draws continuous dots
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        # Right-click clears the canvas
        self.canvas.bind("<Button-3>", self.on_canvas_clear)

    # ------------------ Status bar ------------------
    def _build_statusbar(self):
        # A small status area at the bottom using StringVar for live updates
        status = ttk.Frame(self, padding=(8, 4))
        status.pack(side="bottom", fill="x")
        ttk.Label(status, textvariable=self.state["status"]).pack(side="left")

    # ------------------ Handlers: menu ------------------
    def on_open_file(self):
        # Show a file open dialog and update status based on selection
        path = filedialog.askopenfilename(
            title="Open a text file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if path:
            self.state["status"].set(f"Opened: {path}")
        else:
            self.state["status"].set("Open canceled")

    def on_save(self):
        # Simulate saving current state to a file path chosen by user
        path = filedialog.asksaveasfilename(
            title="Save your profile",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )
        if path:
            # In a real app, you'd write the state to file here
            self.state["status"].set(f"Saved to: {path}")
            messagebox.showinfo("Saved", "Profile saved successfully.")
        else:
            self.state["status"].set("Save canceled")

    def on_exit(self):
        # Confirm before closing; messagebox returns True/False
        if messagebox.askyesno("Exit", "Do you really want to quit?"):
            self.destroy()

    def on_about(self):
        # Simple info dialog
        messagebox.showinfo(
            "About",
            "Interactive Tkinter Demo\n\nFeatures: forms, canvas, menus, validation, events."
        )

    # ------------------ Handlers: buttons & form logic ------------------
    def on_greet(self):
        # Read current name and validate
        name = self.name_var.get().strip()
        if not name:
            # Basic validation feedback and UI hint update
            self.state["status"].set("Name is empty. Please type your name.")
            self.name_hint.configure(text="Name required", foreground="red")
            # Flash the result label for visual cue
            self._flash_label(self.result_label, "Please enter a name first.")
            return

        # Persist validated name into shared app state
        self.state["name"] = name

        # Compose a personalized message using current selections
        lang = self.state["language"].get()
        mode = self.state["mode"].get()
        subscribed = "Subscribed" if self.state["subscribe"].get() else "Not subscribed"

        msg = f"Hello, {name}! You’re exploring {lang} ({mode}). {subscribed}."
        self.result_label.configure(text=msg)
        self.state["status"].set("Greeted successfully.")
        self.name_hint.configure(text="Looks good!", foreground="green")

    def on_clear(self):
        # Reset all interactive elements to defaults
        self.name_var.set("")
        self.state["language"].set("Python")
        self.state["mode"].set("Beginner")
        self.state["subscribe"].set(True)
        self.result_label.configure(text="Cleared. Ready.")
        self.name_hint.configure(text="Type your name and press Enter", foreground="black")
        self.state["status"].set("Form cleared.")
        # Also clear the canvas for a complete reset
        self.canvas.delete("all")

    def on_draw_canvas(self):
        # Draw a simple demonstration: a rectangle and some text
        self.canvas.delete("all")
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        # Draw centered rectangle
        margin = 30
        self.canvas.create_rectangle(
            margin, margin, w - margin, h - margin,
            outline="#333", width=2, fill="#e6f2ff"
        )
        # Draw centered text (uses canvas coordinates, not grid/pack)
        self.canvas.create_text(
            w // 2, h // 2,
            text="Canvas ready.\nLeft-click: dot\nDrag: trail\nRight-click: clear",
            fill="#222", font=("Segoe UI", 11), justify="center"
        )
        self.state["status"].set("Canvas drawn.")

    # ------------------ Handlers: combobox, radio, check ------------------
    def on_language_changed(self, event=None):
        lang = self.state["language"].get()
        self.state["status"].set(f"Language set to {lang}")

    def on_mode_changed(self):
        mode = self.state["mode"].get()
        self.state["status"].set(f"Mode set to {mode}")

    def on_subscribe_toggled(self):
        status = "Subscribed to tips" if self.state["subscribe"].get() else "Unsubscribed"
        self.state["status"].set(status)

    # ------------------ Handlers: canvas mouse events ------------------
    def on_canvas_click(self, event):
        # Draw a small filled circle at click position
        r = 3
        self.canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r, fill="#0078d4", outline="")
        self.state["status"].set(f"Dot at ({event.x}, {event.y})")

    def on_canvas_drag(self, event):
        # Continuous trail while left mouse is held
        r = 2
        self.canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r, fill="#ff6f00", outline="")

    def on_canvas_clear(self, event):
        # Right-click clears the canvas completely
        self.canvas.delete("all")
        self.state["status"].set("Canvas cleared")

    # ------------------ Handlers: global events ------------------
    def on_save_shortcut(self, event):
        # Ctrl+S triggers save (same as menu Save)
        self.on_save()

    def on_enter_key(self, event):
        # Enter triggers greeting for quick keyboard flow
        self.on_greet()

    def on_window_resize(self, event):
        # Window resize events fire often; keep status succinct
        # Only update if the event is for the root window to avoid noise
        if event.widget == self:
            self.state["status"].set(f"Resized: {self.winfo_width()}x{self.winfo_height()}")

    # ------------------ Utility: label flash ------------------
    def _flash_label(self, label, text, duration_ms=700):
        """
        Temporarily change label text and foreground color for feedback.
        Then restore the previous state after a short delay.
        """
        prev_text = label.cget("text")
        prev_fg = label.cget("foreground") or "#000000"
        label.configure(text=text, foreground="red")
        # after() schedules a callback without blocking the GUI loop
        self.after(duration_ms, lambda: label.configure(text=prev_text, foreground=prev_fg))


if __name__ == "__main__":
    # Launch the application
    app = App()
    app.mainloop()
