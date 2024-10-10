import tempfile
import os

def create_temp_file(data, suffix=".txt"):
    """
    Create a temporary file with the given data.
    
    Args:
        data (str): The data to write into the temporary file.
        suffix (str): The file extension for the temporary file (default is ".txt").
    
    Returns:
        str: The path to the temporary file.
    """
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    with open(temp_file.name, 'w') as f:
        f.write(data)
    return temp_file.name

def read_temp_file(file_path):
    """
    Read the content from a temporary file.
    
    Args:
        file_path (str): The path to the temporary file.
    
    Returns:
        str: The content of the temporary file.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return f.read()
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
    except FileNotFoundError:
        return False
