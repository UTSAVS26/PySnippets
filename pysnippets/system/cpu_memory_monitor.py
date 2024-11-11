import psutil
import logging
from dataclasses import dataclass

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class SystemUsage:
    cpu_percent: float
    memory_total_gb: float
    memory_used_gb: float
    memory_free_gb: float
    memory_percent: float

def monitor_system():
    try:
        # Get CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        
        # Get memory usage
        memory = psutil.virtual_memory()
        gb = 1024 ** 3
        
        memory_total = memory.total / gb
        memory_used = memory.used / gb
        memory_free = memory.available / gb
        memory_percent = memory.percent

        system_usage = SystemUsage(
            cpu_percent=round(cpu_percent, 2),
            memory_total_gb=round(memory_total, 2),
            memory_used_gb=round(memory_used, 2),
            memory_free_gb=round(memory_free, 2),
            memory_percent=round(memory_percent, 2)
        )

        logging.info(f"System usage checked: {system_usage}")
        return system_usage

    except Exception as e:
        logging.error(f"Error monitoring system: {str(e)}")
        raise