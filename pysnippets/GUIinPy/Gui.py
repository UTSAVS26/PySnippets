import tkinter as tk
from tkinter import messagebox, ttk
from gui_logic import handle_input  # Import handle_input from the logic file

# Function to handle button click
def show_input():
    user_input = entry.get()  # Get the text from the entry field
    message = handle_input(user_input)  # Use the logic function
    if user_input:
        messagebox.showinfo("Your Input", message)
    else:
        messagebox.showwarning("Input Error", message)

# Rest of the GUI code (same as before)
root = tk.Tk()
root.title("Modern Python GUI")
root.geometry("500x300")
root.configure(bg="#f7f7f7")

frame = tk.Frame(root, bg="#ffffff", bd=10, relief=tk.RAISED)
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

title_label = tk.Label(frame, text="Welcome to the Modern GUI!", font=("Helvetica Neue", 20, "bold"), bg="#ffffff", fg="#4A4A4A")
title_label.pack(pady=(10, 20))

instruction_label = tk.Label(frame, text="Please enter something below:", font=("Arial", 14), bg="#ffffff", fg="#555555")
instruction_label.pack(pady=(0, 10))

entry = ttk.Entry(frame, font=("Arial", 12), width=40)
entry.pack(pady=(0, 20))

button = ttk.Button(frame, text="Submit", command=show_input)
button.pack(pady=(0, 10))

style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"), padding=10, relief="flat", background="#4CAF50", foreground="white")
style.map("TButton", background=[("active", "#45a049")])

root.mainloop()
