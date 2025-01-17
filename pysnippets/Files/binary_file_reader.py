import pickle
from typing import Any, Optional

def read_binary_file(file_path: str) -> Optional[Any]:
    """
    Reads and deserializes all data from a binary file using pickle.

    Args:
        file_path (str): The path to the binary file.

    Returns:
        Optional[Any]: A list of deserialized objects from the file or None if an error occurs.
    """
    if not isinstance(file_path, str):
        raise ValueError("File path must be a string.")
    
    data_list = []
    try:
        with open(file_path, 'rb') as file:
            while True:
                try:
                    # Load each object one by one
                    data = pickle.load(file)
                    data_list.append(data)
                except EOFError:
                    # End of file reached
                    break
        return data_list
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
    result = read_binary_file(file_path)
    if result is not None:
        print("Data read successfully:")
        print(result)
    else:
        print("Failed to read data from the file.")
