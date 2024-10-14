from tkinter import *

def open_top_level():
    top = Toplevel(window)
    top.title("Top Level")
    top.config(bg='lightgrey')
    label = Label(top, text="This is a Top Level window", bg='lightsteelblue')
    label.pack(padx=20, pady=20)

window = Tk()
window.title("Top Level Example")
window.minsize(width=300, height=100)
window.config(bg='lightgrey')

top_button = Button(window, text="Open Top Level", command=open_top_level, bg='lightseagreen')
top_button.pack(pady=20)

window.mainloop()

"""
    Creates a new Top Level window for additional dialogs.
    
    Output: Opens a new window displaying a message when a button 
    in the main window is clicked.
    
"""