from tkinter import *

window = Tk()
window.title("Scale Example")
window.minsize(width=300, height=100)
window.config(bg='lightgrey')

scale = Scale(window, from_=0, to=100, bg='lightgoldenrodyellow')
scale.pack(pady=20)

window.mainloop()

"""
    Creates a Scale for selecting a numeric value.
    
    Output: A window with a slider that allows users to select 
    a value from a specified range (0 to 100).
        
"""