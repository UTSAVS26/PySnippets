import os
import ast

def find_super_directory(target_dir):
    """Find the target directory by traversing upwards."""
    current_dir = os.getcwd()

    while True:
        # Check if target_dir exists in the current directory
        if os.path.basename(current_dir) == target_dir or target_dir in os.listdir(current_dir):
            return os.path.join(current_dir)
        
        # Traverse up one directory level
        parent_dir = os.path.dirname(current_dir)
        
        if parent_dir == current_dir:  # Reached the root directory
            return None
        
        current_dir = parent_dir

def get_imports_from_file(file_path):
    """Extract all imported libraries from a Python file."""
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read(), filename=file_path)
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:  # Handle cases like `from x import y`
                imports.add(node.module.split('.')[0])
    return imports

def scan_directory(directory):
    """Recursively scan all Python files in a directory and extract imports."""
    all_imports = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                all_imports.update(get_imports_from_file(file_path))
    return all_imports

def generate_requirements_file(imports, output_path="requirements.txt"):
    """Generate a requirements.txt file from a set of imports."""
    with open(output_path, "w", encoding="utf-8") as req_file:
        for imp in sorted(imports):
            req_file.write(f"{imp}\n")

if __name__ == "__main__":
    # Define the super directory name
    super_directory = "PySnippets"

    # Find the super directory by traversing upwards
    super_dir_path = find_super_directory(super_directory)

    if super_dir_path:
        # Change directory to the super directory
        os.chdir(super_dir_path)
        print(f"Changed directory to {super_dir_path}")

        # Scan all Python files in the super directory
        all_imports = scan_directory(super_dir_path)
        
        # Generate the requirements.txt file
        generate_requirements_file(all_imports)
        print("requirements.txt generated successfully.")
    else:
        print(f"Super directory '{super_directory}' not found. Please ensure it exists in the directory hierarchy.")
