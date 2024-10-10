import psutil

def get_cpu_usage():
    """
    Get the current CPU usage as a percentage.
    
    Returns:
        float: CPU usage in percentage.
    """
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """
    Get the current memory usage of the system.
    
    Returns:
        dict: A dictionary with total, available, and used memory information.
    """
    memory = psutil.virtual_memory()
    return {
        "total_memory": memory.total,
        "available_memory": memory.available,
        "used_memory": memory.used
    }
