import hashlib
import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class PBKDF2Hasher:
    password: str
    salt: bytes
    iterations: int = 100000
    dklen: int = 32
    hash_name: str = 'sha256'

    def hash_password(self) -> bytes:
        try:
            hashed = hashlib.pbkdf2_hmac(
                self.hash_name,
                self.password.encode(),
                self.salt,
                self.iterations,
                self.dklen
            )
            logging.info(f"Hashed password using PBKDF2: {hashed.hex()}")
            return hashed
        except Exception as e:
            logging.error(f"Error hashing password: {e}")
            raise 