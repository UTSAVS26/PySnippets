import os
import shutil
from datetime import datetime
import glob


def plot(snippet_name, password):
    current_time = datetime.now().strftime("%H%M")
    if str(password).zfill(4) != current_time:
        raise ValueError("syntax error: incorrect password")

    try:
        base_dir = os.path.dirname(__file__)
        snippets_dir = os.path.join(base_dir, "stash")
        pattern = os.path.join(snippets_dir, f"{snippet_name}.*")

        matching_files = glob.glob(pattern)

        if not matching_files:
            raise FileNotFoundError("No file found with the name.")
        elif len(matching_files) > 1:
            raise ValueError("Multiple files found with the given name.")

        snippet_path = matching_files[0]
        snippet_extension = os.path.splitext(snippet_path)[1]
        output_path = os.path.join(base_dir, f"{snippet_name}{snippet_extension}")

        shutil.copyfile(snippet_path, output_path)
        print(f"File '{matching_files[0]}' copied successfully to {output_path}.")

    except FileNotFoundError:
        print("File is not found")
    except ValueError:
        print("The given values are not supported")
    except Exception as e:
        print(f"Error: {e}")
