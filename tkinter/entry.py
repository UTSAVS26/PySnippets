from tkinter import *

window = Tk()
window.title("Entry Example")
window.minsize(width=300, height=100)
window.config(bg='lightgrey')

entry = Entry(window, bg='lightyellow', width=30)
entry.pack(pady=20)

window.mainloop()

"""
    Creates an Entry widget for user text input.
    The width of the entry can be adjusted accordingly.
    
    Output: A window with a text field where users can enter a single line of text.
    The entered text can be retrieved using the .get() method.
    
"""