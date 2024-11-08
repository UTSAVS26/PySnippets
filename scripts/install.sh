#!/bin/bash

# Check if Python is installed
if ! command -v py &> /dev/null; then
    echo "Python is not installed. Please install Python 3.10 or above."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(py --version)
REQUIRED_VERSION=(3 10 0)
if [[ "$PYTHON_VERSION" < "${REQUIRED_VERSION[*]}" ]]; then
    echo "Python version must be 3.10 or higher. Current version is $PYTHON_VERSION."
    exit 1
else
    echo "Python version is $PYTHON_VERSION - OK"
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip is not installed. Installing pip..."
    python3 -m ensurepip --upgrade
else
    echo "pip is already installed - OK"
fi

# Prompt user for upgrading to the latest pip version
read -p "Do you want to upgrade to the latest pip version? (y/n): " answer
if [[ "$answer" == [Yy]* ]]; then
    echo "Upgrading pip to the latest version..."
    python3 -m pip install --upgrade pip
fi

# Upgrade setuptools, pip, and wheel
echo "Upgrading setuptools, pip, and wheel..."
python3 -m pip install --upgrade setuptools pip wheel

# Install tqdm
echo "Installing tqdm..."
python3 -m pip install tqdm

# Install twine with the --user flag
echo "Installing twine with the --user flag..."
python3 -m pip install --user twine

echo "Installation complete!"
