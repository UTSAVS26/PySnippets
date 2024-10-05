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
    'Images': [
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', 
        '.tiff', '.tif', '.svg', '.webp', '.raw', 
        '.heif', '.heic', '.ico', '.ai', '.eps',
        '.indd', '.pdf', '.jfif', '.exif'
    ],
    'Documents': [
        '.pdf', '.docx', '.doc', '.txt', '.xls', 
        '.xlsx', '.pptx', '.ppt', '.csv', '.odt', 
        '.rtf', '.wps', '.xml', '.html', '.md', 
        '.tex', '.epub', '.xps', '.mobi', '.wps', 
        '.numbers', '.key', '.pages'
    ],
    'Videos': [
        '.mp4', '.mov', '.avi', '.mkv', '.wmv', 
        '.flv', '.webm', '.mpeg', '.mpg', '.3gp', 
        '.mpv', '.m4v', '.f4v', '.vob', '.rm', 
        '.rmvb', '.asf', '.m2ts', '.ts', '.divx', 
        '.xvid'
    ],
    'Music': [
        '.mp3', '.wav', '.flac', '.aac', '.ogg', 
        '.m4a', '.wma', '.opus', '.alac', '.aiff', 
        '.mid', '.midi', '.ra', '.3gp', '.dsf', 
        '.dff', '.wv', '.cda'
    ],
    'Archives': [
        '.zip', '.rar', '.tar', '.gz', '.7z', 
        '.bz2', '.xz', '.iso', '.dmg', '.jar', 
        '.tar.gz', '.tgz', '.z', '.ace', '.cab', 
        '.lzh', '.arj'
    ],
    'Scripts': [
        '.py', '.js', '.html', '.css', '.c', 
        '.cpp', '.rb', '.php', '.java', '.sh', 
        '.go', '.swift', '.pl', '.perl', '.sql', 
        '.dart', '.kotlin', '.xml', '.yaml', 
        '.json', '.bat', '.vbs', '.asp'
    ],
    'Fonts': [
        '.ttf', '.otf', '.woff', '.woff2', '.eot', 
        '.svg', '.fnt', '.fon', '.apk' 
    ],
    'System': [
        '.exe', '.dll', '.sys', '.bin', '.iso', 
        '.img', '.sh', '.cmd', '.bat'
    ]
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
