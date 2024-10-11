from tkinter import *

window = Tk()
window.title("Scrollbar Example")
window.minsize(width=300, height=200)
window.config(bg='lightgrey')

listbox = Listbox(window, bg='lightgray', height=5)
for i in range(20):
    listbox.insert(END, f"Item {i+1}")
listbox.pack(side=LEFT, fill=BOTH, pady=20)

scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

window.mainloop()

"""
    Creates a Listbox with a Scrollbar for navigating items.
    
    Output: A window with a list of items that can be scrolled through 
    using a scrollbar on the side.
    
"""