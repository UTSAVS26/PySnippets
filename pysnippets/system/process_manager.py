import subprocess
import psutil

def start_process(command):
    """
    Starts a process using the given shell command.
    
    Args:
        command (str): The shell command to start the process.
    
    Returns:
        subprocess.Popen: The process object.
    """
    process = subprocess.Popen(command, shell=True)
    return process

def stop_process(pid):
    """
    Stops a process by its PID.
    
    Args:
        pid (int): The process ID to terminate.
    
    Returns:
        bool: True if the process was terminated, False otherwise.
    """
    try:
        process = psutil.Process(pid)
        process.terminate()
        return True
    except psutil.NoSuchProcess:
        return False

def monitor_process(pid):
    """
    Monitors the CPU and memory usage of a process by its PID.
    
    Args:
        pid (int): The process ID to monitor.
    
    Returns:
        dict: A dictionary with CPU and memory usage of the process.
    """
    try:
        process = psutil.Process(pid)
        return {
            "cpu_usage": process.cpu_percent(interval=1),
            "memory_usage": process.memory_info().rss
        }
    except psutil.NoSuchProcess:
        return None
