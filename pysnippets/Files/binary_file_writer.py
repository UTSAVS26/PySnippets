import pickle
from typing import Any

def write_binary_file(file_path: str, data: Any) -> None:
    """
    Serializes and writes data to a binary file using pickle.

    Args:
        file_path (str): The path to the binary file.
        data (Any): The data to serialize and save.

    Returns:
        None
    """
    if not isinstance(file_path, str):
        raise ValueError("File path must be a string.")
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)
        print(f"Data successfully written to '{file_path}'")
    except pickle.PickleError as e:
        print(f"Error: Failed to serialize data. Details: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred. Details: {e}")

if __name__ == "__main__":
    # Example Usage
    file_path = r"pysnippets\Files\sample_data.pkl"
    data_to_write = {
        'name': 'Aryan Sharma',
        'age': 24,
        'is_student': True,
        'scores': [55, 88, 26],
        'details': {
            'course': 'Computer Science',
            'year': 2025
        }
    }
    
    write_binary_file(file_path, data_to_write)
    print("Write operation complete.")
