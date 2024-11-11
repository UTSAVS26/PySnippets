# file_organizer.py

import os
import shutil
import sys
import logging

logging.basicConfig(level=logging.INFO)

def organize_files_by_type(folder_path):
    """
    Organizes files in the specified folder by file type, moving them into categorized subfolders.

    Args:
        folder_path (str): The path to the folder to organize.

    Returns:
        None

    Raises:
        ValueError: If the folder_path does not exist.
    """
    if not os.path.exists(folder_path):
        raise ValueError(f"The folder path '{folder_path}' does not exist.")
    
    # Define file categories and their extensions
    file_categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.svg', '.webp'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx', '.pptx', '.ppt', '.csv'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv'],
        'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
        'Scripts': ['.py', '.js', '.html', '.css', '.c', '.cpp'],
        'Fonts': ['.ttf', '.otf', '.woff', '.woff2'],
        'System': ['.exe', '.dll', '.sys', '.bin']
    }

    uncategorized_folder = os.path.join(folder_path, "Uncategorized")
    os.makedirs(uncategorized_folder, exist_ok=True)

    # Organize files
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # Move the file to the appropriate category folder
        moved = False  # Flag to check if the file was moved
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                category_path = os.path.join(folder_path, category)
                os.makedirs(category_path, exist_ok=True)
                try:
                    shutil.move(file_path, os.path.join(category_path, filename))
                    logging.info(f"Moved: {filename} -> {category}")
                except Exception as e:
                    logging.error(f"Error moving file {filename}: {e}")
                moved = True
                break

        # Move unrecognized file to 'Uncategorized'
        if not moved:
            try:
                shutil.move(file_path, os.path.join(uncategorized_folder, filename))
                logging.warning(f"Unrecognized file type for: {filename}. Moved to 'Uncategorized'.")
            except Exception as e:
                logging.error(f"Error moving unrecognized file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder_to_organize = sys.argv[1]
    else:
        folder_to_organize = input("Enter the path to the folder you want to organize: ")

    try:
        organize_files_by_type(folder_to_organize)
    except ValueError as e:
        logging.error(e)