import tempfile
import os
import time

def create_temp_file(data, suffix=".txt"):
    """
    Create a temporary file with the given data.
    
    Args:
        data (str): The data to write into the temporary file.
        suffix (str): The file extension for the temporary file (default is ".txt").
    
    Returns:
        str: The path to the temporary file.
    """
    # Generate a unique filename using the current time
    temp_filename = f"temp_{int(time.time())}{suffix}"
    
    # Using NamedTemporaryFile in a context manager to ensure file is closed
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix, mode='w', name=temp_filename) as temp_file:
        temp_file.write(data)
        return temp_file.name

def read_temp_file(file_path):
    """
    Read the content from a temporary file.
    
    Args:
        file_path (str): The path to the temporary file.
    
    Returns:
        str: The content of the temporary file or None if not found or readable.
    """
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def delete_temp_file(file_path):
    """
    Delete a temporary file.
    
    Args:
        file_path (str): The path to the temporary file.
    
    Returns:
        bool: True if the file was deleted, False otherwise.
    """
    try:
        os.remove(file_path)
        return True
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error deleting file {file_path}: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Create a temporary file with data
    file_path = create_temp_file("This is some test data.")
    print(f"Temporary file created at: {file_path}")
    
    # Read content from the temporary file
    content = read_temp_file(file_path)
    print(f"Content of the temporary file: {content}")
    
    # Delete the temporary file
    if delete_temp_file(file_path):
        print(f"Temporary file {file_path} deleted.")
    else:
        print(f"Failed to delete {file_path}.")