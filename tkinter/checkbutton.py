from tkinter import *

window = Tk()
window.title("Check Button Example")
window.minsize(width=300, height=100)
window.config(bg='lightgrey')

check_var = IntVar()
checkbutton = Checkbutton(window, text="This is a Check Button", variable=check_var, bg='lightcoral')
checkbutton.pack(pady=20)

window.mainloop()

"""
    Creates a Checkbutton that toggles a boolean value.
    
    Output: A window with a checkbox that users can check or uncheck. 
    Its state (checked or unchecked) is stored in an associated variable.
    
"""