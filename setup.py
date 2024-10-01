from setuptools import setup, find_packages
import codecs
import os

# Get the absolute path of the current directory
here = os.path.abspath(os.path.dirname(__file__))

# Open and read the README.md file to use as the long description
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# Define the package version, description, and other metadata
VERSION = '0.1.0'
DESCRIPTION = 'A collection of reusable Python code snippets for everyday tasks'
LONG_DESCRIPTION = 'PySnippets is a library that provides reusable Python code snippets for common programming challenges, categorized for easy navigation.'

# Setup function for packaging
setup(
    name="pysnippets",  # Package name
    version=VERSION,    # Current version of the package
    author="Utsav Singhal",
    author_email="utsavsinghal26@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/UTSAVS26/PySnippets",  # Project's GitHub URL
    packages=find_packages(),  # Automatically find and include all sub-packages
    keywords=['python', 'snippets', 'code', 'utilities', 'reusable', 'beginner-friendly'],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Update based on your package maturity
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version required
)