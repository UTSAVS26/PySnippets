import tkinter as tk
from tkinter import ttk
from gui_logic import handle_input
from components import create_slider, create_checkbox, create_radiobuttons, create_textbox, create_spinbox, create_listbox, create_canvas
from menus import create_menu
from dialogs import show_info, show_warning

# Function to handle button click
def show_input():
    user_input = entry.get()
    message = handle_input(user_input)
    if user_input:
        show_info("Your Input", message)
    else:
        show_warning("Input Error", message)

# Setup the main GUI window
root = tk.Tk()
root.title("Modern Python GUI")
root.geometry("500x300")
root.configure(bg="#f7f7f7")

frame = tk.Frame(root, bg="#ffffff", bd=10, relief=tk.RAISED)
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Adding components
slider = create_slider(frame)
checkbox = create_checkbox(frame)
radiobuttons = create_radiobuttons(frame)
textbox = create_textbox(frame)
spinbox = create_spinbox(frame)
listbox = create_listbox(frame)
canvas = create_canvas(frame)

# Menu
menu = create_menu(root)

# Entry and button
entry = ttk.Entry(frame, font=("Arial", 12), width=40)
entry.pack(pady=(0, 20))
button = ttk.Button(frame, text="Submit", command=show_input)
button.pack(pady=(0, 10))

root.mainloop()
