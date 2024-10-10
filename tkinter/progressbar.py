from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Progress Bar Example")
window.minsize(width=300, height=100)
window.config(bg='lightgrey')

progress_bar = ttk.Progressbar(window, length=200, mode='determinate')
progress_bar.pack(pady=20)

window.mainloop()

"""
    Creates a Progressbar for indicating progress of a task.
    
    Output: A window with a progress bar that visually represents 
    the completion of a task. It can be updated programmatically.
    
"""