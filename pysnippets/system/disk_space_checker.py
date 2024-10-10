import shutil

def check_disk_space(path='/'):
    """
    Check the disk space usage of a given path.
    
    Args:
        path (str): The path to check the disk space. Default is root '/'.
    
    Returns:
        dict: A dictionary containing total, used, and free space in bytes.
    """
    disk_usage = shutil.disk_usage(path)
    return {
        "total_space": disk_usage.total,
        "used_space": disk_usage.used,
        "free_space": disk_usage.free
    }
