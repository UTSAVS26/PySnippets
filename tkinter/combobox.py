from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Combobox Example")
window.minsize(width=300, height=100)
window.config(bg='lightgrey')

combobox = ttk.Combobox(window, values=["Option 1", "Option 2", "Option 3"], width=27)
combobox.pack(pady=20)

window.mainloop()

"""
    Creates a Combobox for selecting options from a dropdown list.
    
    Output: A window with a dropdown menu allowing users to select 
    from predefined options.
    
"""