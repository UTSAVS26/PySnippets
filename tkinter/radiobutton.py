from tkinter import *

window = Tk()
window.title("Radio Button Example")
window.minsize(width=300, height=100)
window.config(bg='lightgrey')

radio_var = StringVar(value="option1")
radiobutton1 = Radiobutton(window, text="Option 1", variable=radio_var, value="option1", bg='lightpink')
radiobutton2 = Radiobutton(window, text="Option 2", variable=radio_var, value="option2", bg='lightpink')
radiobutton1.pack(pady=5)
radiobutton2.pack(pady=5)

window.mainloop()

"""
    Creates Radio buttons for selecting one option from a set.
    
    Output: A window with two radio buttons. Users can select one option, 
    and the selected option is stored in an associated variable.
    
"""