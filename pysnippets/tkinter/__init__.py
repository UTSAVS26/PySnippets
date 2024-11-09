import tkinter as tk
from tkinter import messagebox

class App:
    """
    The App class sets up the main application window and its widgets.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Example App")
        self.root.geometry("300x200")

        # Create a label widget
        self.label = tk.Label(self.root, text="Hello, Tkinter!")
        self.label.pack(pady=10)

        # Create a button widget
        self.button = tk.Button(self.root, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        """
        Callback function for button click event.
        Displays a message box when the button is clicked.
        """
        messagebox.showinfo("Information", "Button was clicked!")
