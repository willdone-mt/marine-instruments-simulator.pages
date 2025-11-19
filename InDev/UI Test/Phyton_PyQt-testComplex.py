"""
Complex PyQt5 GUI Example
This program demonstrates:
- Menu bar and status bar
- Form inputs (QLineEdit, QComboBox, QRadioButton, QCheckBox)
- Buttons with actions (Greet, Clear)
- Interactive canvas (click and drag to draw dots, right-click to clear)
"""

import sys
# Import core PyQt5 widgets
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QComboBox,
    QRadioButton, QCheckBox, QPushButton, QVBoxLayout, QHBoxLayout,
    QGridLayout, QGroupBox, QGraphicsScene, QGraphicsView, QAction, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPen


# ------------------ Custom Canvas ------------------
class DrawingCanvas(QGraphicsView):
    """
    A subclass of QGraphicsView that allows interactive drawing.
    - Left-click: draw a dot
    - Drag with left mouse: draw continuous trail of dots
    - Right-click: clear the canvas
    """

    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        self.scene = scene
        # Define the visible area of the scene
        self.scene.setSceneRect(0, 0, 400, 300)
        # Enable mouse tracking so we can capture movement
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        """Triggered when the mouse is clicked."""
        scene_pos = self.mapToScene(event.pos())  # Convert view coords → scene coords
        if event.button() == Qt.LeftButton:
            self.draw_dot(scene_pos)
        elif event.button() == Qt.RightButton:
            self.scene.clear()

    def mouseMoveEvent(self, event):
        """Triggered when the mouse moves inside the view."""
        if event.buttons() & Qt.LeftButton:  # Check if left button is held
            scene_pos = self.mapToScene(event.pos())
            self.draw_dot(scene_pos)

    def draw_dot(self, scene_pos):
        """Helper function to draw a small circle at given position."""
        r = 4  # radius of dot
        self.scene.addEllipse(scene_pos.x() - r, scene_pos.y() - r,
                              2*r, 2*r, QPen(Qt.black), QBrush(Qt.red))


# ------------------ Main Window ------------------
class MyWindow(QMainWindow):
    """
    Main application window.
    Contains:
    - Menu bar
    - Status bar
    - Form inputs (name, language, mode, subscription)
    - Buttons (Greet, Clear)
    - Interactive canvas
    """

    def __init__(self):
        super().__init__()

        # ----- Window basics -----
        self.setWindowTitle("Complex PyQt Example")
        self.setGeometry(100, 100, 800, 600)

        # Central widget (everything goes inside this)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main vertical layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # ----- Menu bar -----
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)  # Close window when clicked
        file_menu.addAction(exit_action)

        # Help menu
        help_menu = menubar.addMenu("Help")
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

        # ----- Status bar -----
        self.statusBar().showMessage("Ready")

        # ----- Form section -----
        form_group = QGroupBox("Profile Setup")  # Group box for form
        form_layout = QGridLayout()

        # Row 0: Name entry
        form_layout.addWidget(QLabel("Name:"), 0, 0)
        self.name_entry = QLineEdit()
        form_layout.addWidget(self.name_entry, 0, 1)

        # Row 1: Language selection (ComboBox)
        form_layout.addWidget(QLabel("Favorite language:"), 1, 0)
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["Python", "JavaScript", "Go", "Rust", "Java", "C#"])
        form_layout.addWidget(self.lang_combo, 1, 1)

        # Row 2: Mode selection (RadioButtons)
        form_layout.addWidget(QLabel("Mode:"), 2, 0)
        self.radio_beginner = QRadioButton("Beginner")
        self.radio_intermediate = QRadioButton("Intermediate")
        self.radio_advanced = QRadioButton("Advanced")
        self.radio_beginner.setChecked(True)  # Default selection
        mode_layout = QHBoxLayout()
        mode_layout.addWidget(self.radio_beginner)
        mode_layout.addWidget(self.radio_intermediate)
        mode_layout.addWidget(self.radio_advanced)
        form_layout.addLayout(mode_layout, 2, 1)

        # Row 3: Subscription checkbox
        self.subscribe_check = QCheckBox("Subscribe to tips")
        self.subscribe_check.setChecked(True)
        form_layout.addWidget(self.subscribe_check, 3, 1)

        # Row 4: Buttons
        self.greet_btn = QPushButton("Greet")
        self.clear_btn = QPushButton("Clear")
        self.greet_btn.clicked.connect(self.on_greet)
        self.clear_btn.clicked.connect(self.on_clear)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.greet_btn)
        button_layout.addWidget(self.clear_btn)
        form_layout.addLayout(button_layout, 4, 0, 1, 2)

        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)

        # Result label
        self.result_label = QLabel("Welcome! Adjust settings and click Greet.")
        main_layout.addWidget(self.result_label)

        # ----- Canvas section -----
        canvas_group = QGroupBox("Canvas Playground")
        canvas_layout = QVBoxLayout()
        self.scene = QGraphicsScene()
        self.canvas = DrawingCanvas(self.scene)
        canvas_layout.addWidget(self.canvas)
        canvas_group.setLayout(canvas_layout)
        main_layout.addWidget(canvas_group)

    # ------------------ Handlers ------------------
    def on_greet(self):
        """Triggered when Greet button is clicked."""
        name = self.name_entry.text().strip()
        if not name:
            self.statusBar().showMessage("Name is empty. Please type your name.")
            self.result_label.setText("Please enter a name first.")
            return

        lang = self.lang_combo.currentText()
        if self.radio_beginner.isChecked():
            mode = "Beginner"
        elif self.radio_intermediate.isChecked():
            mode = "Intermediate"
        else:
            mode = "Advanced"

        subscribed = "Subscribed" if self.subscribe_check.isChecked() else "Not subscribed"
        msg = f"Hello, {name}! You’re exploring {lang} ({mode}). {subscribed}."
        self.result_label.setText(msg)
        self.statusBar().showMessage("Greeted successfully.")

    def on_clear(self):
        """Triggered when Clear button is clicked."""
        self.name_entry.clear()
        self.lang_combo.setCurrentIndex(0)
        self.radio_beginner.setChecked(True)
        self.subscribe_check.setChecked(True)
        self.result_label.setText("Cleared. Ready.")
        self.scene.clear()
        self.statusBar().showMessage("Form cleared.")

    def show_about(self):
        """Triggered when About menu is clicked."""
        QMessageBox.information(self, "About",
            "Complex PyQt Example\n\nFeatures: forms, menus, status bar, and interactive canvas.")


# ------------------ Boilerplate ------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create application object
    window = MyWindow()           # Create main window
    window.show()                 # Show window
    sys.exit(app.exec_())         # Enter event loop
