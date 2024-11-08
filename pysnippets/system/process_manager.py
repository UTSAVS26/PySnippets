import subprocess
import psutil
import time

def start_process(command):
    """
    Starts a process using the given shell command.
    
    Args:
        command (str or list): The shell command to start the process. If a string, it will be split into a list.
    
    Returns:
        subprocess.Popen: The process object.
    """
    if isinstance(command, str):
        # Split the command string into a list of arguments
        command = command.split()

    process = subprocess.Popen(command)
    return process

def stop_process(pid, force=False):
    """
    Stops a process by its PID.
    
    Args:
        pid (int): The process ID to terminate.
        force (bool): If True, forcefully kill the process; otherwise, attempt graceful termination.
    
    Returns:
        bool: True if the process was terminated, False otherwise.
    """
    try:
        process = psutil.Process(pid)
        if force:
            process.kill()  # Force kill the process
        else:
            process.terminate()  # Graceful termination
        return True
    except psutil.NoSuchProcess:
        print(f"Process with PID {pid} does not exist.")
        return False
    except psutil.AccessDenied:
        print(f"Access denied to terminate process with PID {pid}.")
        return False

def monitor_process(pid, timeout=10):
    """
    Monitors the CPU and memory usage of a process by its PID.
    
    Args:
        pid (int): The process ID to monitor.
        timeout (int): Timeout in seconds for monitoring.
    
    Returns:
        dict: A dictionary with CPU and memory usage of the process, or None if the process is not found.
    """
    try:
        process = psutil.Process(pid)
        cpu_usage = process.cpu_percent(interval=timeout)
        memory_usage = process.memory_info().rss  # in bytes

        return {
            "cpu_usage": cpu_usage,
            "memory_usage": memory_usage
        }
    except psutil.NoSuchProcess:
        print(f"Process with PID {pid} does not exist.")
        return None
    except psutil.AccessDenied:
        print(f"Access denied to monitor process with PID {pid}.")
        return None
    except psutil.TimeoutExpired:
        print(f"Monitoring process with PID {pid} timed out.")
        return None

# Example usage
if __name__ == "__main__":
    # Start a process
    process = start_process("python -m http.server 8080")
    
    # Monitor the process for a while
    time.sleep(2)  # Give the process time to start
    pid = process.pid
    print(monitor_process(pid))

    # Stop the process gracefully
    stop_process(pid)