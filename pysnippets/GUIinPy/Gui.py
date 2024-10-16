import tkinter as tk
from tkinter import messagebox, ttk

# Function to handle button click
def show_input():
    user_input = entry.get()  # Get the text from the entry field
    if user_input:
        messagebox.showinfo("Your Input", f"You entered: {user_input}")
    else:
        messagebox.showwarning("Input Error", "Please enter some text!")

# Create the main window
root = tk.Tk()
root.title("Modern Python GUI")  # Set the title of the window
root.geometry("500x300")  # Set window size
root.configure(bg="#f7f7f7")  # Set background color

# Create a frame for better organization
frame = tk.Frame(root, bg="#ffffff", bd=10, relief=tk.RAISED)
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)  # Add padding around the frame

# Create a title label
title_label = tk.Label(frame, text="Welcome to the Modern GUI!", font=("Helvetica Neue", 20, "bold"), bg="#ffffff", fg="#4A4A4A")
title_label.pack(pady=(10, 20))  # Add vertical padding

# Create a label for instructions
instruction_label = tk.Label(frame, text="Please enter something below:", font=("Arial", 14), bg="#ffffff", fg="#555555")
instruction_label.pack(pady=(0, 10))  # Add vertical padding

# Create an entry field for user input with styling
entry = ttk.Entry(frame, font=("Arial", 12), width=40)
entry.pack(pady=(0, 20))  # Add vertical padding

# Create a styled button
button = ttk.Button(frame, text="Submit", command=show_input)
button.pack(pady=(0, 10))  # Add vertical padding

# Configure the style of the button
style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"), padding=10, relief="flat", background="#4CAF50", foreground="white")
style.map("TButton", background=[("active", "#45a049")])  # Change color on hover

# Start the GUI event loop
root.mainloop()
