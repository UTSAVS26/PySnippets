# Modern Python GUI Application

## Overview

This project is a simple graphical user interface (GUI) application developed using Python's Tkinter library. The application serves as an introductory example of creating interactive applications with Tkinter, showcasing essential GUI components and event handling.

## Features

- **Main Window**: A customizable window that serves as the main interface for the application.
- **Welcome Message**: A label displaying a welcome message to the user.
- **User Input**: An entry widget allowing users to input text.
- **Interactive Button**: A button that triggers an event to display user input in a pop-up message box.
- **Stylish Design**: A modern design with thoughtful layout, spacing, and colors to enhance user experience.

## Implementation Details

### Widgets Used

1. **Tk**: The main class for creating a window in Tkinter. It is the root element of the GUI application.
   
2. **Frame**: A container widget used to organize the layout of other widgets. It provides a way to group and style a set of widgets.
   
3. **Label**: Displays static text or images. In this application, it is used for the welcome message and instructions.
   
4. **Entry**: A single-line text input field where users can type in their data. It captures user input for further processing.
   
5. **Button**: A clickable button that triggers an action when clicked. In this case, it shows a pop-up message with the user's input.

6. **MessageBox**: A pop-up dialog that displays information or alerts to the user. It is used here to provide feedback based on the user's input.

7. **Style (ttk.Style)**: A way to customize the appearance of widgets. We used it to style the button and ensure it has a modern look.

