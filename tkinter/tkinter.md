# Tkinter - the most popular Python library for creating GUI Applications

The Tkinter module in Python is a standard GUI (Graphical User Interface) toolkit that is easy to use and comes with Python. It provides a powerful object-oriented interface to the Tk GUI toolkit shipped with Python.

Tkinter is a wrapper around Tk, which is a graphical user interface toolkit that is used to create desktop applications. Tkinter provides a wide variety of ready-made dialog boxes and widgets, which can be used to build complex and attractive GUIs.

By default `tkinter` comes pre installed with python.

## Creating first GUI Application
There are two main methods used which the user needs to remember while creating the Python application with GUI.

#### Tk()
To create a main window, tkinter offers a method ‘Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)’. To change the name of the window, we can change the className to the desired one. This is the basic code used to create the main window of the application.

#### mainloop()
There is a method known by the name mainloop() is used when the application is ready to run. mainloop() is an infinite loop used to run the application, wait for an event to occur, and process the event as long as the window is not closed.

```python
import tkinter
m = tkinter.Tk()
'''
widgets are added here
'''
m.mainloop()
```

## Widgets
Widgets are the building blocks of the interface. Each widget serves a specific purpose and provides a way for users to interact with the application. Here’s a brief overview of some common widgets along with coding snippets demonstrating their use with specified dimensions.

###### Note :
+ All heights and widths are in pixels. 
+ The `pack()` method is used to display the widget on the tkinter interface. We will cover this mathod later.

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24"> Label
A label widget is used to display text or images in a window. It is often used for providing information to the user.

```python
import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="This is a Label", width=your_desired_value, height=your_desired_value)
label.pack()
root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  Button
The button widget is a clickable element that performs an action when clicked. It can also change state or update other widgets.

```python
import tkinter as tk

root = tk.Tk()
button = tk.Button(root, text="Click Me", width=your_desired_value, height=your_desired_value)
button.pack()
root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  Entry
The entry widget allows users to input a single line of text. It is useful for getting short text inputs such as names or search queries.

```python
import tkinter as tk

root = tk.Tk()
entry = tk.Entry(root, width=your_desired_value)
entry.pack()
root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  Check button
A checkbutton allows users to toggle a setting on or off. It can hold a binary state (checked or unchecked).

```python
import tkinter as tk

root = tk.Tk()
var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Check Me", variable=var)
checkbutton.pack()
root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  Radio button
Radio buttons allow the user to select one option from a group. Only one radio button in a group can be selected at a time.

```python
import tkinter as tk

root = tk.Tk()
var = tk.StringVar(value="Option 1")

radio1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2")
radio1.pack()
radio2.pack()
root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  Listbox

A Listbox widget displays a list of items from which a user can select one or more items. The items can be strings or other types of data.

```python
import tkinter as tk

root = tk.Tk()
listbox = tk.Listbox(root)
listbox.pack()

for item in ["Apple", "Banana", "Cherry"]:
    listbox.insert(tk.END, item)

root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  Scrollbar

A Scrollbar widget is used to provide scrolling capabilities for other widgets such as Listbox, Text, or Canvas. It can be oriented vertically or horizontally.

```python
import tkinter as tk

root = tk.Tk()

listbox = tk.Listbox(root)
for i in range(50):
    listbox.insert(tk.END, f"Item {i+1}")
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  Menu

A Menu widget creates a menu bar that allows users to access commands and options. Menus can have multiple submenus and can be attached to the main application window.

```python
import tkinter as tk

def exit_app():
    root.quit()

root = tk.Tk()
menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)

root.config(menu=menubar)
root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  Canvas

A Canvas widget is used for drawing shapes, images, and other graphics. It provides a flexible area for custom graphics and can also contain other widgets.

```python
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=your_desired_value, height=your_desired value, bg='white')
canvas.pack()

root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  Combobox
A Combobox is a drop-down list that allows users to select from a list of options or enter their own input. It combines a dropdown list and an entry field. Users can either select an option or type their own value.
Supports autocomplete functionality.

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
combo = ttk.Combobox(root, values=["Apple", "Banana", "Cherry"])
combo.pack()
combo.current(0)  # Set default selection

root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  Scale

A Scale widget allows users to select a numeric value from a specified range using a slider. It supports both horizontal and vertical orientation. It can be configured to show ticks and labels.

```python
import tkinter as tk

root = tk.Tk()
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  Toplevel
A Toplevel widget creates a new window that is separate from the main application window. It is useful for creating dialogs or secondary windows. It can contain any widgets like frames, buttons, etc.

```python
import tkinter as tk

def open_toplevel():
    top = tk.Toplevel(root)
    top.title("New Window")
    tk.Label(top, text="This is a Toplevel window").pack()

root = tk.Tk()
button = tk.Button(root, text="Open Toplevel", command=open_toplevel)
button.pack()

root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  Message

A Message widget is similar to a Label, but it can display multi-line text and wraps text automatically. It automatically wraps text to fit within the widget.It is useful for displaying informational text or instructions.

```python
import tkinter as tk

root = tk.Tk()
message = tk.Message(root, text="This is a message widget.")
message.pack()

root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  Menubutton

A Menubutton displays a menu when clicked. It is a button that can show a dropdown menu. It can be used to create context menus or dropdowns. It can contain multiple options.

```python
import tkinter as tk

def show_selection(value):
    print(f"You selected: {value}")

root = tk.Tk()
menubutton = tk.Menubutton(root, text="Menu")
menubutton.pack()

menu = tk.Menu(menubutton, tearoff=0)
menu.add_command(label="Option 1", command=lambda: show_selection("Option 1"))
menu.add_command(label="Option 2", command=lambda: show_selection("Option 2"))
menubutton.config(menu=menu)
menubutton.pack()

root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  Progressbar
A Progressbar widget visually represents the progress of a task. It can be determinate (shows progress) or indeterminate (shows that a task is ongoing). It can display progress in a bar format. It supports both vertical and horizontal orientations.

```python
import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
progress = ttk.Progressbar(root, length=200, mode='determinate')
progress.pack()

def start_progress():
    for i in range(101):
        progress['value'] = i
        root.update()
        time.sleep(0.05)

button = tk.Button(root, text="Start", command=start_progress)
button.pack()

root.mainloop()
```
### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  Spinbox

A Spinbox allows users to select from a range of values using up and down arrows. It can also accept user input. It can be configured with a range and step size. It allows direct input or selection.

```python
import tkinter as tk

root = tk.Tk()
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

root.mainloop()
```

## Geometry Management

Efficiently managing the geometry of tkinter windows and widgets is essential for creating polished user interfaces. Here, we’ll explore methods like place(), grid(), and pack() to help set dimensions and create organized and responsive layouts.

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  pack()

The pack() method is a geometry manager that organizes widgets in blocks before placing them in the parent widget. It is the simplest method for layout management. Widgets can be packed in a vertical (side=tk.TOP, side=tk.BOTTOM) or horizontal (side=tk.LEFT, side=tk.RIGHT) direction.

We can specify whether the widget should fill the available space (fill parameter) and whether it should expand to fill any extra space in the parent widget (expand parameter).

Widgets are packed in the order they are created. The last widget packed will appear on top.

```python
import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1")
label1.pack(side=tk.TOP, fill=tk.X)

label2 = tk.Label(root, text="Label 2")
label2.pack(side=tk.TOP, fill=tk.X)

button = tk.Button(root, text="Click Me")
button.pack(side=tk.BOTTOM)

root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  place()

The place() method allows you to specify the exact position of a widget in the parent widget. This method provides more control over widget placement than pack() and grid(). We can specify the x and y coordinates for the widget's position.

It also supports relative positioning using the relx and rely parameters (values between 0.0 and 1.0).

We can explicitly set the widget’s width and height.

```python
import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="I'm placed at (50, 50)")
label.place(x=50, y=50)

button = tk.Button(root, text="Button")
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
```

### <img src="https://media1.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" height="24">  grid()
The grid() method organizes widgets in a table-like structure using rows and columns. This method provides a flexible way to manage complex layouts. Each widget can be placed in a specific row and column using the row and column parameters.
We can span a widget across multiple rows or columns using the rowspan and columnspan parameters.
We can specify which sides of the cell the widget should stick to (north, south, east, west) using the sticky parameter.

```python
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Name:").grid(row=0, column=0, sticky=tk.W)
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0, sticky=tk.W)
tk.Entry(root).grid(row=1, column=1)

tk.Button(root, text="Submit").grid(row=2, columnspan=2)

root.mainloop()
```
<hr>