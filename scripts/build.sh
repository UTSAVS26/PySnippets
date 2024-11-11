#!/bin/bash

# Add ing Colors for better output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

check_command() {
    if ! command -v "$1" &> /dev/null; then
        echo -e "${RED}Error: $1 is not installed. Please install it first.${NC}"
        exit 1
    fi
}

check_command "python"
check_command "pip"

# Check if Python packages are present
echo -e "${YELLOW}Checking and installing required Python packages...${NC}"
pip install twine wheel setuptools --quiet

prompt_for_input() {
    local prompt_text=$1
    local required=$2
    local value=""
    
    while true; do
        read -p "$prompt_text: " value
        
        if [[ -z "$value" && "$required" == "true" ]]; then
            echo -e "${RED}This field is required. Please enter a value.${NC}"
            continue
        fi
        
        echo "$value"
        break
    done
}

echo -e "${GREEN}Please provide the following information for your Python package:${NC}"

# Taking input from the user
PACKAGE_NAME=$(prompt_for_input "Enter package name" "true")
VERSION=$(prompt_for_input "Enter version (e.g., 1.0.0)" "true")
AUTHOR_NAME=$(prompt_for_input "Enter author name" "true")
AUTHOR_EMAIL=$(prompt_for_input "Enter author email" "true")
DESCRIPTION=$(prompt_for_input "Enter package description (press Enter to skip)" "false")

echo -e "${YELLOW}You'll need a PyPI token to upload your package.${NC}"
echo -e "${YELLOW}If you don't have one, you can create it at https://pypi.org/manage/account/token/${NC}"
PYPI_TOKEN=$(prompt_for_input "Enter your PyPI token" "true")

echo -e "${YELLOW}Creating .pypirc file...${NC}"
cat > ~/.pypirc << EOL
[pypi]
username = __token__
password = ${PYPI_TOKEN}
EOL

chmod 600 ~/.pypirc

echo -e "${YELLOW}Creating setup.py file...${NC}"
cat > setup.py << EOL
from setuptools import setup, find_packages

setup(
    name="${PACKAGE_NAME}",
    version="${VERSION}",
    packages=find_packages(),
    description="${DESCRIPTION}",
    author="${AUTHOR_NAME}",
    author_email="${AUTHOR_EMAIL}",
    license="GPL 3.0",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
EOL

echo -e "${GREEN}setup.py file created successfully!${NC}"

# Checking if required files exist
if [ ! -d "${PACKAGE_NAME}" ]; then
    echo -e "${YELLOW}Creating package directory structure...${NC}"
    mkdir -p "${PACKAGE_NAME}"
    touch "${PACKAGE_NAME}/__init__.py"
fi

# Cleaning the previous builds if they exist
if [ -d "dist" ]; then
    echo -e "${YELLOW}Cleaning previous builds...${NC}"
    rm -rf dist build *.egg-info
fi

echo -e "${GREEN}Building the package...${NC}"
if python setup.py sdist bdist_wheel; then
    echo -e "${GREEN}Package built successfully!${NC}"
else
    echo -e "${RED}Package build failed!${NC}"
    exit 1
fi

echo -e "${GREEN}Uploading package to PyPI...${NC}"
if python -m twine upload dist/*; then
    echo -e "${GREEN}Package successfully uploaded to PyPI!${NC}"
else
    echo -e "${RED}Package upload failed!${NC}"
    exit 1
fi

echo -e "${YELLOW}Cleaning up...${NC}"
rm -f ~/.pypirc

echo -e "${GREEN}Package deployment complete! Your package can be installed using:${NC}"
echo -e "${YELLOW}pip install ${PACKAGE_NAME}${NC}"