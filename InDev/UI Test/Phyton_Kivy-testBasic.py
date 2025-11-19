# Import the Kivy base App class and UI widgets
from kivy.app import App
from kivy.uix.label import Label        # For displaying text
from kivy.uix.textinput import TextInput  # For user input
from kivy.uix.button import Button      # For clickable button
from kivy.uix.boxlayout import BoxLayout  # For arranging widgets vertically

# Define the main application class, inheriting from Kivy's App
class MyKivyApp(App):
    def build(self):
        """
        The build() method constructs the UI.
        In Kivy, you return the root widget here.
        """

        # Create a vertical layout (BoxLayout with orientation='vertical')
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create a Label widget with initial text
        self.label = Label(text="Enter your name:")

        # Create a TextInput widget for user input
        # multiline=False ensures it's a single-line field
        self.entry = TextInput(multiline=False)

        # Create a Button widget
        # Bind its on_press event to the greet() method
        button = Button(text="Greet Me")
        button.bind(on_press=self.greet)  # ✅ This is correct in Kivy

        # Add widgets to the layout in order (top to bottom)
        layout.add_widget(self.label)
        layout.add_widget(self.entry)
        layout.add_widget(button)

        # Return the layout as the root widget
        return layout

    def greet(self, instance):
        """
        Event handler for the button.
        - Reads text from the TextInput (self.entry.text).
        - Updates the Label with a greeting.
        """
        name = self.entry.text.strip()
        if name:
            self.label.text = f"Hello, {name}!"
        else:
            self.label.text = "Please enter your name first."

# Standard boilerplate to run the app
if __name__ == "__main__":
    MyKivyApp().run()
