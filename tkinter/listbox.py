from tkinter import *

window = Tk()
window.title("Listbox Example")
window.minsize(width=300, height=200)
window.config(bg='lightgrey')

listbox = Listbox(window, bg='lightgray', height=5)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")
listbox.pack(pady=20)

window.mainloop()

"""
    Creates a Listbox for selecting items from a list.
    
    Output: A window displaying a list of items. Users can select one or more 
    items from the list.
    
"""