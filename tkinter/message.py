from tkinter import *

window = Tk()
window.title("Message Example")
window.minsize(width=300, height=100)
window.config(bg='lightgrey')

message = Message(window, text="This is a Message widget to display multi-line text.", bg='lightpink')
message.pack(pady=20)

window.mainloop()

"""
    Creates a Message widget for displaying multi-line text.
    
    Output: A window displaying a message with the capability 
    to wrap text across multiple lines.
    
"""