from setuptools import setup, find_packages

setup(
    name='pysnippets',
    version='0.1.0',
    author='Utsav Singhal',
    author_email='utsavsinghal26@gmail.com',
    description='A collection of reusable Python code snippets for everyday tasks.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/UTSAVS26/PySnippets',
    packages=find_packages(),  # Automatically find all sub-packages
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)