import pickle
from typing import Any, Optional

def find_data_in_binary_file(file_path: str, search_data: Any) -> Optional[Any]:
    """
    Searches for a specific data object in a binary file using pickle.

    Args:
        file_path (str): The path to the binary file.
        search_data (Any): The data to search for within the binary file.

    Returns:
        Optional[Any]: The first matching object from the file or None if no match is found.
    """
    if not isinstance(file_path, str):
        raise ValueError("File path must be a string.")
    
    try:
        with open(file_path, 'rb') as file:
            while True:
                try:
                    # Load each object one by one
                    data = pickle.load(file)
                    if data == search_data:
                        return data
                except EOFError:
                    # End of file reached
                    break
        print("No matching data found.")
        return None
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Please check the file path.")
    except pickle.PickleError as e:
        print(f"Error: Failed to deserialize data. Details: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred. Details: {e}")
        return None

if __name__ == "__main__":
    # Example Usage
    file_path = r"pysnippets\Files\sample_data.pkl"
    search_data = {'name': 'Aryan Sharma',
        'age': 24,
        'is_student': True,
        'scores': [55, 88, 26],
        'details': {
            'course': 'Computer Science',
            'year': 2025
        }}
    
    result = find_data_in_binary_file(file_path, search_data)
    if result is not None:
        print("Matching data found:")
        print(result)
    else:
        print("No matching data found.")
