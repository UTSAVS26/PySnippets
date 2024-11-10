import hashlib
import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class MD5Hasher:
    data: str

    def hash(self) -> str:
        try:
            hashed = hashlib.md5(self.data.encode()).hexdigest()
            logging.info(f"MD5 hashed '{self.data}' to '{hashed}'")
            return hashed
        except Exception as e:
            logging.error(f"Error hashing data: {e}")
            raise 