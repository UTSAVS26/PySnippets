import os
import logging
from dataclasses import dataclass
from typing import Optional, Dict

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class EnvVar:
    name: str
    value: str
    previous_value: Optional[str]

class EnvVarManager:
    def __init__(self):
        """Initialize the environment variable manager"""
        self.modified_vars: Dict[str, EnvVar] = {}
        logging.info("Initialized EnvVarManager")

    def set_var(self, name: str, value: str) -> EnvVar:
        """Set an environment variable, storing the previous value"""
        previous = os.environ.get(name)
        os.environ[name] = value
        
        env_var = EnvVar(
            name=name,
            value=value,
            previous_value=previous
        )
        self.modified_vars[name] = env_var
        
        logging.info(f"Set environment variable: {env_var}")
        return env_var

    def get_var(self, name: str) -> Optional[str]:
        """Get the value of an environment variable"""
        value = os.environ.get(name)
        logging.info(f"Retrieved environment variable {name}: {value}")
        return value

    def delete_var(self, name: str) -> None:
        """Delete an environment variable if it exists"""
        if name in os.environ:
            del os.environ[name]
            logging.info(f"Deleted environment variable: {name}")
        else:
            logging.info(f"Environment variable {name} does not exist")

    def restore_var(self, name: str) -> None:
        """Restore an environment variable to its previous value"""
        if name in self.modified_vars:
            env_var = self.modified_vars[name]
            if env_var.previous_value is not None:
                os.environ[name] = env_var.previous_value
                logging.info(f"Restored {name} to previous value: {env_var.previous_value}")
            else:
                self.delete_var(name)
            del self.modified_vars[name]
        else:
            logging.info(f"No previous value stored for {name}")

    def restore_all(self) -> None:
        """Restore all modified environment variables"""
        for name in list(self.modified_vars.keys()):
            self.restore_var(name)
        logging.info("Restored all modified environment variables")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.restore_all()

# Example usage
if __name__ == "__main__":
    try:
        with EnvVarManager() as manager:
            # Set some environment variables
            manager.set_var("TEST_VAR1", "value1")
            manager.set_var("TEST_VAR2", "value2")
            
            # Get values
            print(manager.get_var("TEST_VAR1"))
            
            # Delete a variable
            manager.delete_var("TEST_VAR2")
            
            # Variables are automatically restored after the with block
    except Exception as e:
        print(f"An error occurred: {e}")