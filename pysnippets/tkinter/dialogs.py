from tkinter import messagebox

def show_confirmation(title: str, message: str) -> bool:
    """
    Displays a confirmation dialog and returns True if the user confirms, False otherwise.
    
    Args:
        title (str): The title of the dialog window.
        message (str): The message displayed in the dialog.
    
    Returns:
        bool: True if user clicks 'Yes', False if 'No'.
    """
    return messagebox.askyesno(title, message)

def show_error(title: str, message: str):
    """
    Displays an error message dialog.
    
    Args:
        title (str): The title of the error dialog.
        message (str): The error message to display.
    """
    messagebox.showerror(title, message)

def show_info(title: str, message: str):
    """
    Displays an informational message dialog.
    
    Args:
        title (str): The title of the info dialog.
        message (str): The information message to display.
    """
    messagebox.showinfo(title, message) 