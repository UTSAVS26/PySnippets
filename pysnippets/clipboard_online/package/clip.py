import os
import subprocess
import sys
import shutil
from datetime import datetime
import glob


def display(snippet_name, password):
    current_time = datetime.now().strftime("%H%M")
    if str(password).zfill(4) != current_time:
        raise ValueError("Invalid password")

    base_dir = os.path.dirname(__file__)
    snippets_dir = os.path.join(base_dir, "stash")
    pattern = os.path.join(snippets_dir, f"{snippet_name}.*")

    matching_files = glob.glob(pattern)

    if not matching_files:
        raise FileNotFoundError("No file found with the name.")
    elif len(matching_files) > 1:
        raise ValueError("Multiple files found with the given name.")

    snippet_path = os.path.join(snippets_dir, matching_files[0])

    try:
        with open(snippet_path, "r") as file:
            source_code = file.read()

        # Call the copy to clipboard function
        copy_to_clipboard(source_code)

    except FileNotFoundError:
        print("File not found")
        raise


def copy_to_clipboard(text):
    # Linux
    if "linux" in sys.platform:
        # Check if xclip is installed
        if shutil.which("xclip") is None:
            print("Error: xclip not found. Install it.", file=sys.stderr)
            return
        # If xclip is installed, proceed with copying text
        subprocess.run(
            ["xclip", "-selection", "clipboard"],
            input=text.strip().encode(),
            check=True,
        )

    # Windows
    elif "win32" in sys.platform:
        subprocess.run(
            ["C:\\Windows\\System32\\clip.exe"], input=text.strip().encode(), check=True
        )

    # macOS
    elif "darwin" in sys.platform:
        subprocess.run(["/usr/bin/pbcopy"], input=text.strip().encode(), check=True)

    else:
        raise OSError("Unsupported operating system")
