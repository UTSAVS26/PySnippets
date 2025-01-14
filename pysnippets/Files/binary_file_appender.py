import pickle
from typing import Any

def append_binary_file(file_path: str, data: Any) -> None:
    """
    Appends data to an existing binary file using pickle.

    Args:
        file_path (str): The path to the binary file.
        data (Any): The data to serialize and append.

    Returns:
        None
    """
    if not isinstance(file_path, str):
        raise ValueError("File path must be a string.")
    
    try:
        # Open the file in append-binary mode
        with open(file_path, 'ab') as file:
            pickle.dump(data, file)
        print(f"Data successfully appended to '{file_path}'")
    except pickle.PickleError as e:
        print(f"Error: Failed to serialize data. Details: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred. Details: {e}")

if __name__ == "__main__":
    # Example Usage
    file_path = r"pysnippets\Files\sample_data.pkl"
    data_to_append = {
        'name': 'Jaya Mehra',
        'age': 25,
        'is_student': True,
        'scores': [85, 90, 92],
        'details': {
            'course': 'Data Science',
            'year': 2026
        }
    }
    
    append_binary_file(file_path, data_to_append)
    print("Append operation complete.")
