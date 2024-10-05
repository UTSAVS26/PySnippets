# file_organizer.py

import os
import shutil

def organize_files_by_type(folder_path):
    """
    Organizes files in the specified folder by file type, moving them into categorized subfolders.

    Args:
        folder_path (str): The path to the folder to organize.

    Returns:
        None

    Example:
        If you have a folder with images, documents, and videos mixed together, this function will
        move them into 'Images', 'Documents', 'Videos', etc., subfolders based on their extensions.

    Raises:
        ValueError: If the folder_path does not exist.
    """
    if not os.path.exists(folder_path):
        raise ValueError(f"The folder path '{folder_path}' does not exist.")
    
    # Define file categories and their extensions
    file_categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xls', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.html', '.css', '.c'],
    }

    # Create category folders if they don't exist
    for category in file_categories:
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Organize files
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get file extension
        _, file_extension = os.path.splitext(filename)

        # Move the file to the appropriate category folder
        moved = False  # Flag to check if the file was moved
        for category, extensions in file_categories.items():
            if file_extension.lower() in extensions:
                shutil.move(file_path, os.path.join(folder_path, category, filename))
                print(f"Moved: {filename} -> {category}")
                moved = True
                break
        
        # If the file type was not recognized, print a message
        if not moved:
            print(f"Unrecognized file type for: {filename}. File not moved.")

# Example usage
if __name__ == "__main__":
    folder_to_organize = r"path_to_the_folder"  # Replace with the actual folder path
    try:
        organize_files_by_type(folder_to_organize)
    except ValueError as e:
        print(e)
