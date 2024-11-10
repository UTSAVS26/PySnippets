import tkinter as tk
from tkinter import messagebox

def show_info(title, message):
    messagebox.showinfo(title, message)

def show_warning(title, message):
    messagebox.showwarning(title, message) 