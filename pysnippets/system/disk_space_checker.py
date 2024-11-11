import shutil
import logging
from dataclasses import dataclass

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class DiskSpace:
    total_space_gb: float
    used_space_gb: float
    free_space_gb: float
    used_percent: float
    free_percent: float

def check_disk_space(path='/'):
    try:
        disk_usage = shutil.disk_usage(path)
        gb = 1024 ** 3
        total_space = disk_usage.total / gb
        used_space = disk_usage.used / gb
        free_space = disk_usage.free / gb
        used_percent = (disk_usage.used / disk_usage.total) * 100
        free_percent = (disk_usage.free / disk_usage.total) * 100

        disk_space = DiskSpace(
            total_space_gb=round(total_space, 2),
            used_space_gb=round(used_space, 2),
            free_space_gb=round(free_space, 2),
            used_percent=round(used_percent, 2),
            free_percent=round(free_percent, 2)
        )
        logging.info(f"Disk space checked: {disk_space}")
        return disk_space
    except FileNotFoundError:
        logging.error(f"Path '{path}' not found.")
        raise
    except PermissionError:
        logging.error(f"Permission denied for path '{path}'.")
        raise

# Example usage
if __name__ == "__main__":
    try:
        disk_info = check_disk_space('/')
        print(disk_info)
    except Exception as e:
        print(f"An error occurred: {e}")
