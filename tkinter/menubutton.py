from tkinter import *

window = Tk()
window.title("Menu Button Example")
window.minsize(width=300, height=100)
window.config(bg='lightgrey')

menu_button = Menubutton(window, text="Menu Button", bg='lightyellow')
menu_button.menu = Menu(menu_button, tearoff=0)
menu_button.menu.add_command(label="Option 1")
menu_button.menu.add_command(label="Option 2")
menu_button['menu'] = menu_button.menu
menu_button.pack(pady=20)

window.mainloop()

"""
    Creates a Menu Button that displays a dropdown menu.
    
    Output: A window with a button that, when clicked, shows 
    a menu with options that can be selected.
    
"""