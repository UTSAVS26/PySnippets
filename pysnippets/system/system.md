# System Utilities Snippets

A collection of Python snippets for managing system resources, processes, environment variables, and more. These reusable code snippets can help you streamline common system-level tasks like monitoring system resource usage, managing environment variables, handling temporary files, and more.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [1. Process Manager](#1-process-manager)
  - [2. System Resource Monitor](#2-system-resource-monitor)
  - [3. Disk Space Checker](#3-disk-space-checker)
  - [4. Environment Variable Manager](#4-environment-variable-manager)
  - [5. Temporary File Handler](#5-temporary-file-handler)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Process Manager**: Start, stop, and monitor system processes.
- **System Resource Monitor**: Check CPU and memory usage.
- **Disk Space Checker**: Get disk space information for a specified directory.
- **Environment Variable Manager**: Get, set, and delete environment variables.
- **Temporary File Handler**: Create, read, and delete temporary files.

## Getting Started

### Prerequisites

- Python 3.x
- psutil library for monitoring system resources
- shutil and tempfile (both part of Python standard library)

### Installation

Install the required dependencies:

```bash
pip install psutil
```

Clone the repository or copy the code snippets to your project.

## Usage

### 1. Process Manager

Manage system processes by starting, stopping, and monitoring their resource usage.

```python
from process_manager import start_process, stop_process, monitor_process

# Start a process
process = start_process('python -m http.server')

# Monitor process CPU and memory usage
print(monitor_process(process.pid))

# Stop the process
stop_process(process.pid)
```

### 2. System Resource Monitor

Monitor CPU and memory usage of the entire system.

```python
from system_resource_monitor import get_cpu_usage, get_memory_usage

# Get CPU usage percentage
cpu_usage = get_cpu_usage()
print(f"CPU Usage: {cpu_usage}%")

# Get memory usage details
memory_info = get_memory_usage()
print(f"Total Memory: {memory_info['total_memory']}, Used: {memory_info['used_memory']}")
```

### 3. Disk Space Checker

Check the total, used, and free space on a given path (default is root).

```python
from disk_space_checker import check_disk_space

# Get disk space details for root directory
disk_info = check_disk_space('/')
print(f"Total: {disk_info['total_space']}, Free: {disk_info['free_space']}, Used: {disk_info['used_space']}")
```

### 4. Environment Variable Manager

Manage environment variables by setting, getting, and deleting them.

```python
from env_variable_manager import get_env_variable, set_env_variable, delete_env_variable

# Set an environment variable
set_env_variable('MY_VAR', 'my_value')

# Get the value of an environment variable
value = get_env_variable('MY_VAR')
print(f"MY_VAR: {value}")

# Delete the environment variable
delete_env_variable('MY_VAR')
```

### 5. Temporary File Handler

Create, read, and delete temporary files.

```python
from temp_file_handler import create_temp_file, read_temp_file, delete_temp_file

# Create a temporary file with data
file_path = create_temp_file("Hello, World!")

# Read the content of the temporary file
content = read_temp_file(file_path)
print(f"Content: {content}")

# Delete the temporary file
delete_temp_file(file_path)
```
