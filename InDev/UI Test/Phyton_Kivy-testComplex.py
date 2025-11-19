"""
Complex Kivy GUI Example
This program demonstrates:
- ActionBar "menu" (About, Exit)
- Status bar (message label at the bottom)
- Form inputs: TextInput (Name), Spinner (Language), ToggleButtons (Mode), CheckBox (Subscribe)
- Buttons with actions (Greet, Clear)
- Interactive canvas: tap/drag to draw red dots; right-click (desktop) clears

Notes for non-coders:
- Kivy runs a main application loop via App.run()
- The UI is built using layout widgets (BoxLayout, GridLayout) that arrange child widgets
- Events (button presses, touches) call Python methods you define
"""

# ----- Imports -----
# Core Kivy application base class
from kivy.app import App
# UI widgets used for building the interface
from kivy.uix.label import Label              # display text
from kivy.uix.textinput import TextInput      # single-line input
from kivy.uix.checkbox import CheckBox        # boolean checkbox
from kivy.uix.button import Button            # clickable button
from kivy.uix.boxlayout import BoxLayout      # vertical/horizontal arrangement
from kivy.uix.gridlayout import GridLayout    # grid (rows x columns)
from kivy.uix.spinner import Spinner          # dropdown selection
from kivy.uix.togglebutton import ToggleButton  # radio-like mode selection
from kivy.uix.popup import Popup              # simple dialogs (for About)
from kivy.uix.widget import Widget            # base widget for custom canvas
from kivy.core.window import Window           # access window and mouse events
from kivy.graphics import Color, Ellipse      # drawing primitives

# Optional: Give the window a title and size
Window.title = "Complex Kivy Example"
# Window.size = (900, 650)  # uncomment to force a window size


# ----- Custom Canvas Widget -----
class DrawingCanvas(Widget):
    """
    A custom widget that acts like a canvas.
    - Touch down: draw a dot at the touch position
    - Touch move (drag with left mouse / finger): draw continuous dots (paintbrush effect)
    - Right-click (on desktop): clear the canvas

    How drawing works in Kivy:
    - You enter a 'with self.canvas:' block to issue drawing instructions
    - Color(r, g, b, a) sets the current drawing color
    - Ellipse(pos=(x, y), size=(w, h)) draws a circle/ellipse
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # We can store brush settings here (color, radius)
        self.brush_color = (1, 0, 0, 1)  # red in RGBA
        self.brush_radius = 4

        # For desktop: listen to keyboard/mouse state if needed
        # But for simplicity, we only use touch info (which also maps mouse events)

    def on_touch_down(self, touch):
        """
        Called when the user presses the mouse/finger inside the widget.

        'touch' contains:
        - touch.pos → (x, y) coordinates relative to this widget
        - touch.button → 'left', 'right', etc. (only on desktop mouse)
        """
        # Ensure the touch is inside this widget (not on other UI elements)
        if not self.collide_point(*touch.pos):
            return False  # let other widgets handle the touch

        # If right-click on desktop, clear the canvas
        if hasattr(touch, "button") and touch.button == "right":
            self.clear_canvas()
            return True

        # Draw a dot at the touch position
        self.draw_dot(touch.pos)
        return True  # we consumed the touch

    def on_touch_move(self, touch):
        """
        Called continuously when the user drags with finger/mouse.
        We draw a dot at each move event to create a trail.
        """
        if not self.collide_point(*touch.pos):
            return False

        # Only draw when dragging with left button or finger
        if not hasattr(touch, "button") or touch.button == "left":
            self.draw_dot(touch.pos)
            return True

        return False

    def draw_dot(self, pos):
        """
        Draw a small circle centered at position 'pos' (x, y).
        Kivy's Ellipse uses top-left corner + size, so we offset by radius.
        """
        x, y = pos
        r = self.brush_radius
        with self.canvas:
            Color(*self.brush_color)            # set drawing color (red)
            Ellipse(pos=(x - r, y - r), size=(2 * r, 2 * r))  # small circle

    def clear_canvas(self):
        """
        Remove all drawing instructions from this widget's canvas.
        """
        self.canvas.clear()


# ----- Main App Class -----
class ComplexKivyApp(App):
    """
    The main application class. It builds the UI and wires events (button presses) to methods.
    """

    def build(self):
        """
        Construct the interface and return the root widget.
        Kivy calls this method once when the app starts.
        """

        # Top-level vertical layout:
        # - "ActionBar" menu row (simulated with a horizontal BoxLayout)
        # - Form group box (GridLayout inside a BoxLayout)
        # - Result label
        # - Canvas group
        # - Status bar
        root = BoxLayout(orientation="vertical", padding=8, spacing=8)

        # ----- Simulated Menu (ActionBar-like row) -----
        # Kivy doesn't have a native desktop menu bar; we simulate with buttons.
        menu_bar = BoxLayout(orientation="horizontal", size_hint_y=None, height=40, spacing=8)

        # About button → shows a Popup
        about_btn = Button(text="About", size_hint_x=None, width=100)
        about_btn.bind(on_press=self.show_about_popup)

        # Exit button → stops the app
        exit_btn = Button(text="Exit", size_hint_x=None, width=100)
        exit_btn.bind(on_press=lambda *_: self.stop())

        # Add menu buttons to the row
        menu_bar.add_widget(about_btn)
        menu_bar.add_widget(exit_btn)
        root.add_widget(menu_bar)

        # ----- Form Section -----
        # We'll use a container BoxLayout to hold a titled area (title via a Label)
        form_box = BoxLayout(orientation="vertical", spacing=6)

        # Title label for the form area
        form_title = Label(text="[b]Profile Setup[/b]", markup=True, size_hint_y=None, height=28)
        form_box.add_widget(form_title)

        # Grid layout with 2 columns: labels on the left, inputs on the right
        form_grid = GridLayout(cols=2, row_default_height=40, spacing=6, size_hint_y=None)
        form_grid.bind(minimum_height=form_grid.setter("height"))  # auto-fit rows

        # Row 0: Name
        form_grid.add_widget(Label(text="Name:", halign="left"))
        self.name_input = TextInput(text="", multiline=False)  # single-line input
        form_grid.add_widget(self.name_input)

        # Row 1: Favorite language (Spinner is Kivy's dropdown)
        form_grid.add_widget(Label(text="Favorite language:", halign="left"))
        self.lang_spinner = Spinner(text="Python", values=("Python", "JavaScript", "Go", "Rust", "Java", "C#"))
        form_grid.add_widget(self.lang_spinner)

        # Row 2: Mode (three ToggleButtons behaving like radio buttons)
        # We put the toggles in a horizontal row with the same 'group' name
        form_grid.add_widget(Label(text="Mode:", halign="left"))
        mode_row = BoxLayout(orientation="horizontal", spacing=6)
        self.mode_beginner = ToggleButton(text="Beginner", group="mode", state="down")  # default selected
        self.mode_intermediate = ToggleButton(text="Intermediate", group="mode")
        self.mode_advanced = ToggleButton(text="Advanced", group="mode")
        mode_row.add_widget(self.mode_beginner)
        mode_row.add_widget(self.mode_intermediate)
        mode_row.add_widget(self.mode_advanced)
        form_grid.add_widget(mode_row)

        # Row 3: Subscribe (CheckBox)
        form_grid.add_widget(Label(text="Subscribe to tips:", halign="left"))
        subscribe_row = BoxLayout(orientation="horizontal", spacing=6)
        self.subscribe_checkbox = CheckBox(active=True)
        subscribe_row.add_widget(self.subscribe_checkbox)
        form_grid.add_widget(subscribe_row)

        # Row 4: Buttons (Greet, Clear)
        # We'll place both buttons in a horizontal row spanning both columns
        # Trick: add an empty label to fill left cell, then a box with buttons on the right
        form_grid.add_widget(Label(text=""))
        buttons_row = BoxLayout(orientation="horizontal", spacing=6)

        greet_btn = Button(text="Greet")
        greet_btn.bind(on_press=self.on_greet)

        clear_btn = Button(text="Clear")
        clear_btn.bind(on_press=self.on_clear)

        buttons_row.add_widget(greet_btn)
        buttons_row.add_widget(clear_btn)
        form_grid.add_widget(buttons_row)

        # Add the grid into the form box
        form_box.add_widget(form_grid)
        root.add_widget(form_box)

        # ----- Result Label -----
        # Shows status messages related to the form (like greeting)
        self.result_label = Label(text="Welcome! Adjust settings and click Greet.")
        root.add_widget(self.result_label)

        # ----- Canvas Section -----
        canvas_box = BoxLayout(orientation="vertical", spacing=6)
        canvas_title = Label(text="[b]Canvas Playground[/b]", markup=True, size_hint_y=None, height=28)
        canvas_box.add_widget(canvas_title)

        # Our custom interactive canvas widget
        self.canvas_widget = DrawingCanvas()
        # Give it a nice minimum height so it feels like a drawing area
        self.canvas_widget.size_hint_y = 1
        canvas_box.add_widget(self.canvas_widget)

        root.add_widget(canvas_box)

        # ----- Status Bar -----
        # A bottom label to show app-wide messages
        self.status_bar = Label(text="Ready", size_hint_y=None, height=30)
        root.add_widget(self.status_bar)

        # Return the assembled root layout to Kivy
        return root

    # ----- Event Handlers -----

    def show_about_popup(self, *_):
        """
        Shows an 'About' popup with app information.
        Popup is Kivy's simple dialog widget.
        """
        content = Label(text="Complex Kivy Example\n\nFeatures: forms, status bar, and interactive canvas.")
        popup = Popup(title="About", content=content, size_hint=(0.5, 0.5))
        popup.open()

    def on_greet(self, *_):
        """
        Called when the Greet button is pressed.
        Validates name and builds a message using current settings.
        """
        name = self.name_input.text.strip()
        if not name:
            self.status_bar.text = "Name is empty. Please type your name."
            self.result_label.text = "Please enter a name first."
            return

        lang = self.lang_spinner.text

        # Determine selected mode based on which ToggleButton is 'down'
        if self.mode_beginner.state == "down":
            mode = "Beginner"
        elif self.mode_intermediate.state == "down":
            mode = "Intermediate"
        else:
            mode = "Advanced"

        subscribed = "Subscribed" if self.subscribe_checkbox.active else "Not subscribed"

        msg = f"Hello, {name}! You’re exploring {lang} ({mode}). {subscribed}."
        self.result_label.text = msg
        self.status_bar.text = "Greeted successfully."

    def on_clear(self, *_):
        """
        Called when the Clear button is pressed.
        Resets the form inputs and clears the canvas.
        """
        self.name_input.text = ""
        self.lang_spinner.text = "Python"
        self.mode_beginner.state = "down"
        self.mode_intermediate.state = "normal"
        self.mode_advanced.state = "normal"
        self.subscribe_checkbox.active = True

        self.result_label.text = "Cleared. Ready."
        self.canvas_widget.clear_canvas()
        self.status_bar.text = "Form cleared."


# ----- Run the App -----
if __name__ == "__main__":
    # Create and run the Kivy application
    ComplexKivyApp().run()
