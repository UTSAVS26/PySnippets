import os
import tempfile
import logging
from dataclasses import dataclass
from typing import Optional
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class TempFile:
    path: Path
    name: str
    size_bytes: int

class TempFileHandler:
    def __init__(self, base_dir: Optional[str] = None):
        """Initialize the temp file handler with optional base directory"""
        self.base_dir = base_dir
        self.temp_files: list[TempFile] = []
        logging.info(f"Initialized TempFileHandler with base dir: {base_dir}")

    def create_temp_file(self, content: str = "", suffix: Optional[str] = None, prefix: Optional[str] = None) -> TempFile:
        """Create a temporary file with optional content and naming"""
        try:
            with tempfile.NamedTemporaryFile(mode='w', 
                                           delete=False,
                                           suffix=suffix,
                                           prefix=prefix,
                                           dir=self.base_dir) as temp:
                if content:
                    temp.write(content)
                
                temp_path = Path(temp.name)
                temp_file = TempFile(
                    path=temp_path,
                    name=temp_path.name,
                    size_bytes=len(content)
                )
                self.temp_files.append(temp_file)
                
                logging.info(f"Created temporary file: {temp_file}")
                return temp_file

        except Exception as e:
            logging.error(f"Error creating temporary file: {str(e)}")
            raise

    def cleanup(self) -> None:
        """Remove all temporary files created by this handler"""
        for temp_file in self.temp_files:
            try:
                os.unlink(temp_file.path)
                logging.info(f"Removed temporary file: {temp_file.path}")
            except Exception as e:
                logging.error(f"Error removing temporary file {temp_file.path}: {str(e)}")
        
        self.temp_files.clear()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()

# Example usage
if __name__ == "__main__":
    try:
        with TempFileHandler() as handler:
            # Create a temp file with content
            temp1 = handler.create_temp_file("Hello World!", suffix=".txt")
            print(f"Created temp file at: {temp1.path}")
            
            # Create an empty temp file
            temp2 = handler.create_temp_file(prefix="test_", suffix=".tmp")
            print(f"Created empty temp file at: {temp2.path}")
            
        # Files are automatically cleaned up after the with block
    except Exception as e:
        print(f"An error occurred: {e}")