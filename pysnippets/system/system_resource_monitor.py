import psutil
import logging
from dataclasses import dataclass
from typing import Tuple, Dict

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class SystemResources:
    cpu_percent: float
    total_memory: str
    available_memory: str 
    used_memory: str
    memory_percent: float
    swap_total: str
    swap_used: str
    swap_free: str

def get_cpu_usage(interval: float = 1.0) -> float:
    """
    Get the current CPU usage as a percentage over a given interval.
    
    Args:
        interval (float): Time in seconds to calculate the CPU usage.
    
    Returns:
        float: CPU usage in percentage.
        
    Raises:
        ValueError: If interval is negative.
    """
    if interval < 0:
        raise ValueError("Interval must be non-negative")
        
    usage = psutil.cpu_percent(interval=interval)
    logging.info(f"CPU Usage: {usage}%")
    return usage

def bytes_to_readable(byte_value: int) -> Tuple[float, str]:
    """Convert bytes to human readable format with appropriate unit"""
    for unit in ['Bytes', 'KB', 'MB', 'GB', 'TB']:
        if byte_value < 1024.0:
            return round(byte_value, 2), unit
        byte_value /= 1024.0
    return round(byte_value * 1024, 2), 'TB'

def get_memory_usage() -> Dict[str, str]:
    """
    Get the current memory usage of the system.
    
    Returns:
        Dict[str, str]: A dictionary with total, available, used memory and swap info
        in a human-readable format.
    """
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    total_memory, total_unit = bytes_to_readable(memory.total)
    available_memory, available_unit = bytes_to_readable(memory.available)
    used_memory, used_unit = bytes_to_readable(memory.used)
    
    swap_total, swap_total_unit = bytes_to_readable(swap.total)
    swap_used, swap_used_unit = bytes_to_readable(swap.used)
    swap_free, swap_free_unit = bytes_to_readable(swap.free)
    
    resources = SystemResources(
        cpu_percent=get_cpu_usage(),
        total_memory=f"{total_memory} {total_unit}",
        available_memory=f"{available_memory} {available_unit}", 
        used_memory=f"{used_memory} {used_unit}",
        memory_percent=memory.percent,
        swap_total=f"{swap_total} {swap_total_unit}",
        swap_used=f"{swap_used} {swap_used_unit}",
        swap_free=f"{swap_free} {swap_free_unit}"
    )
    
    logging.info(f"System resources: {resources}")
    
    return {
        "total_memory": resources.total_memory,
        "available_memory": resources.available_memory,
        "used_memory": resources.used_memory,
        "memory_percent": f"{resources.memory_percent}%",
        "swap_total": resources.swap_total,
        "swap_used": resources.swap_used,
        "swap_free": resources.swap_free
    }

# Example usage
if __name__ == "__main__":
    try:
        print(f"CPU Usage: {get_cpu_usage()}%")
        print("Memory Usage:", get_memory_usage())
    except Exception as e:
        logging.error(f"Error monitoring system resources: {str(e)}")