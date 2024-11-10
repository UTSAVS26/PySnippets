import subprocess
import psutil
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def start_process(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        logging.info(f"Process started with PID: {process.pid}")
        return process
    except Exception as e:
        logging.error(f"Failed to start process: {e}")
        raise

def stop_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        process.wait()
        logging.info(f"Process with PID {pid} terminated")
    except psutil.NoSuchProcess:
        logging.error(f"No such process with PID {pid}")
        raise
    except Exception as e:
        logging.error(f"Failed to stop process with PID {pid}: {e}")
        raise

if __name__ == "__main__":
    try:
        proc = start_process('echo "Hello World"')
        stop_process(proc.pid)
    except Exception as e:
        print(f"An error occurred: {e}")
