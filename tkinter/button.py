from tkinter import *

window = Tk()
window.title("Button Example")
window.minsize(width=300, height=100)
window.config(bg='lightgrey')

button = Button(window, text="This is a Button", bg='lightgreen', command=lambda: print("Button Pressed"))
button.pack(pady=20)

window.mainloop()

"""
    Creates a Button widget that prints a message when clicked.
    The height and width of the button can be adjusted accordingly.
    
    Output: A window with a button labeled 'This is a Button'. 
    Clicking the button prints 'Button Pressed' to the console.
    
"""