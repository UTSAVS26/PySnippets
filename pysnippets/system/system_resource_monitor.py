import psutil

def get_cpu_usage(interval=1):
    """
    Get the current CPU usage as a percentage over a given interval.
    
    Args:
        interval (int): Time in seconds to calculate the CPU usage.
    
    Returns:
        float: CPU usage in percentage.
    """
    return psutil.cpu_percent(interval=interval)

def get_memory_usage():
    """
    Get the current memory usage of the system.
    
    Returns:
        dict: A dictionary with total, available, and used memory in a human-readable format.
    """
    memory = psutil.virtual_memory()
    
    # Convert bytes to MB/GB for readability
    def bytes_to_readable(byte_value):
        if byte_value >= 1 << 30:  # GB
            return round(byte_value / (1 << 30), 2), 'GB'
        elif byte_value >= 1 << 20:  # MB
            return round(byte_value / (1 << 20), 2), 'MB'
        elif byte_value >= 1 << 10:  # KB
            return round(byte_value / (1 << 10), 2), 'KB'
        return byte_value, 'Bytes'
    
    total_memory, total_unit = bytes_to_readable(memory.total)
    available_memory, available_unit = bytes_to_readable(memory.available)
    used_memory, used_unit = bytes_to_readable(memory.used)
    
    return {
        "total_memory": f"{total_memory} {total_unit}",
        "available_memory": f"{available_memory} {available_unit}",
        "used_memory": f"{used_memory} {used_unit}",
    }

# Example usage
if __name__ == "__main__":
    print(f"CPU Usage: {get_cpu_usage()}%")
    print("Memory Usage:", get_memory_usage())