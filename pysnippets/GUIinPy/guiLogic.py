# gui_logic.py
def handle_input(user_input):
    """Handles user input and returns appropriate messages."""
    if user_input:
        return f"You entered: {user_input}"
    else:
        return "Please enter some text!"
