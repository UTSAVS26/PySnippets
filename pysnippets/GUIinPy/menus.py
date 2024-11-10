import tkinter as tk
from tkinter import Menu

def create_menu(root):
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=lambda: None)
    filemenu.add_command(label="Save", command=lambda: None)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)
    return menubar 