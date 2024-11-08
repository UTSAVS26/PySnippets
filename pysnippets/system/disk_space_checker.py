import shutil

def check_disk_space(path='/'):
    """
    Check the disk space usage of a given path.
    
    Args:
        path (str): The path to check the disk space. Default is root '/'.
    
    Returns:
        dict: A dictionary containing total, used, and free space in a readable format.
    """
    try:
        disk_usage = shutil.disk_usage(path)
        
        # Convert bytes to GB
        gb = 1024 ** 3
        total_space = disk_usage.total / gb
        used_space = disk_usage.used / gb
        free_space = disk_usage.free / gb
        
        # Calculate usage percentage
        used_percent = (disk_usage.used / disk_usage.total) * 100
        free_percent = (disk_usage.free / disk_usage.total) * 100
        
        return {
            "total_space_gb": round(total_space, 2),
            "used_space_gb": round(used_space, 2),
            "free_space_gb": round(free_space, 2),
            "used_percent": round(used_percent, 2),
            "free_percent": round(free_percent, 2)
        }
    except FileNotFoundError:
        return {"error": f"Path '{path}' not found."}
    except PermissionError:
        return {"error": f"Permission denied for path '{path}'."}

# Example usage
if __name__ == "__main__":
    print(check_disk_space('/'))