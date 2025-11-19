# Import the necessary PyQt5 modules
# QApplication → manages the GUI application's control flow and main settings
# QWidget → the base class for all UI objects (a blank window)
# QLabel → displays text
# QLineEdit → single-line text input field
# QPushButton → clickable button
# QVBoxLayout → vertical layout manager to arrange widgets top-to-bottom
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys  # Needed to handle command-line arguments for QApplication

# Define the main window class, inheriting from QWidget
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()  # Initialize the QWidget base class

        # Set window properties
        self.setWindowTitle("PyQt Interactive Example")
        self.setGeometry(100, 100, 300, 150)  # x, y, width, height

        # Create widgets
        self.label = QLabel("Enter your name:")   # Static text label
        self.entry = QLineEdit()                  # Text input field
        self.button = QPushButton("Greet Me")     # Button

        # Connect button click event to a function
        self.button.clicked.connect(self.greet)

        # Create a vertical layout and add widgets in order
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.button)

        # Apply the layout to the main window
        self.setLayout(layout)

    # Define the function triggered when the button is clicked
    def greet(self):
        # Update the label text with the user’s input
        name = self.entry.text()
        self.label.setText(f"Hello, {name}!")

# Standard boilerplate to run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)   # Create the application object
    window = MyWindow()            # Create an instance of our window
    window.show()                  # Show the window
    sys.exit(app.exec_())          # Enter the main event loop
