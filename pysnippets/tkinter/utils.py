import tkinter as tk
from tkinter import filedialog

def open_file_dialog(title: str = "Open File") -> str:
    """
    Opens a file dialog for the user to select a file.
    
    Args:
        title (str): The title of the file dialog window.
    
    Returns:
        str: The path of the selected file. Returns an empty string if no file is selected.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title=title)
    root.destroy()
    return file_path

def save_file_dialog(title: str = "Save File", defaultextension: str = ".txt") -> str:
    """
    Opens a file dialog for the user to save a file.
    
    Args:
        title (str): The title of the file dialog window.
        defaultextension (str): The default file extension.
    
    Returns:
        str: The path where the file will be saved. Returns an empty string if no path is selected.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.asksaveasfilename(title=title, defaultextension=defaultextension)
    root.destroy()
    return file_path 