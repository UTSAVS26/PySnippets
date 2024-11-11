import hashlib
import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class SHA3Hasher:
    data: str
    variant: str = 'sha3_256'

    def hash_data(self) -> str:
        try:
            hash_func = getattr(hashlib, self.variant)
            hashed = hash_func(self.data.encode()).hexdigest()
            logging.info(f"SHA3 hashed '{self.data}' using {self.variant}: {hashed}")
            return hashed
        except AttributeError:
            logging.error(f"Unsupported SHA3 variant: {self.variant}")
            raise
        except Exception as e:
            logging.error(f"Error hashing data with SHA3: {e}")
            raise 