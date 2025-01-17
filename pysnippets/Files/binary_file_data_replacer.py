import pickle
from typing import Any

def find_and_replace_in_binary_file(file_path: str, search_data: Any, replace_data: Any) -> bool:
    """
    Finds specific data in a binary file and replaces it with new data using pickle.

    Args:
        file_path (str): The path to the binary file.
        search_data (Any): The data to search for within the binary file.
        replace_data (Any): The new data to replace the matching data.

    Returns:
        bool: True if replacement is successful, False otherwise.
    """
    if not isinstance(file_path, str):
        raise ValueError("File path must be a string.")
    
    try:
        # Read all data from the binary file
        objects = []
        found = False
        with open(file_path, 'rb') as file:
            while True:
                try:
                    obj = pickle.load(file)
                    if obj == search_data:
                        objects.append(replace_data)  # Replace matching object
                        found = True
                    else:
                        objects.append(obj)
                except EOFError:
                    break

        if not found:
            print("No matching data found to replace.")
            return False

        # Write the updated data back to the binary file
        with open(file_path, 'wb') as file:
            for obj in objects:
                pickle.dump(obj, file)
        
        print("Data successfully replaced.")
        return True

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Please check the file path.")
    except pickle.PickleError as e:
        print(f"Error: Failed to process data. Details: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred. Details: {e}")
    return False

if __name__ == "__main__":
    # Example Usage
    file_path = r"pysnippets\Files\sample_data.pkl"
    search_data = {
        'name': 'Aryan Sharma',
        'age': 24,
        'is_student': True,
        'scores': [55, 88, 26],
        'details': {
            'course': 'Computer Science',
            'year': 2025
        }
    }
    replace_data = {
        'name': 'Aaryan Sharma',
        'age': 24,
        'is_student': True,
        'scores': [55, 88, 32],
        'details': {
            'course': 'AWS Solution Architect',
            'year': 2025
        }
    }
    
    result = find_and_replace_in_binary_file(file_path, search_data, replace_data)
    if result:
        print("Find and replace operation completed successfully.")
    else:
        print("Find and replace operation failed.")
