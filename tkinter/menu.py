from tkinter import *

window = Tk()
window.title("Menu Example")
window.minsize(width=300, height=100)
window.config(bg='lightgrey')

menubar = Menu(window)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=file_menu)

window.config(menu=menubar)

window.mainloop()

"""
    Creates a Menu for organizing commands.
    
    Output: A window with a menu bar at the top. The 'File' menu 
    includes options for 'New', 'Open', and 'Exit'.
    
"""