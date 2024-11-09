import tkinter as tk
from pysnippets.tkinter.widgets import CustomEntry
from pysnippets.tkinter.dialogs import show_confirmation

def main():
    """
    The main function initializes the Tkinter root window and starts the application.
    """
    root = tk.Tk()
    root.title("Custom Entry Example")
    
    entry = CustomEntry(root, placeholder="Enter your name")
    entry.pack(pady=20, padx=20)
    
    def on_exit():
        if show_confirmation("Exit", "Are you sure you want to exit?"):
            root.destroy()
    
    exit_button = tk.Button(root, text="Exit", command=on_exit)
    exit_button.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
