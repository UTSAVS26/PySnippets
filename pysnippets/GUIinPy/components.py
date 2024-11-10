import tkinter as tk
from tkinter import ttk, Checkbutton, Radiobutton, IntVar, Scale, HORIZONTAL, Text, Spinbox, Listbox, Canvas

# Define complex components here
def create_slider(frame):
    slider = Scale(frame, from_=0, to=100, orient=HORIZONTAL, bg="#ffffff")
    slider.pack(pady=(10, 0))
    return slider

def create_checkbox(frame):
    chk_var = IntVar()
    chk = Checkbutton(frame, text="Enable Feature", variable=chk_var, bg="#ffffff")
    chk.pack(pady=(10, 0))
    return chk

def create_radiobuttons(frame):
    r_var = IntVar()
    r1 = Radiobutton(frame, text="Option 1", variable=r_var, value=1, bg="#ffffff")
    r1.pack()
    r2 = Radiobutton(frame, text="Option 2", variable=r_var, value=2, bg="#ffffff")
    r2.pack()
    return r1, r2

def create_textbox(frame):
    text_box = Text(frame, height=5, width=30)
    text_box.pack(pady=(10, 0))
    return text_box

def create_spinbox(frame):
    spinbox = Spinbox(frame, from_=0, to=10)
    spinbox.pack(pady=(10, 0))
    return spinbox

def create_listbox(frame):
    listbox = Listbox(frame)
    listbox.insert(1, "Item 1")
    listbox.insert(2, "Item 2")
    listbox.pack(pady=(10, 0))
    return listbox

def create_canvas(frame):
    canvas = Canvas(frame, width=100, height=100, bg="grey")
    canvas.pack(pady=(10, 0))
    canvas.create_oval(25, 25, 75, 75, fill="blue")
    return canvas 