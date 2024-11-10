import bcrypt
import logging
from dataclasses import dataclass
from typing import Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class BcryptHasher:
    password: str
    salt: Optional[bytes] = None
    rounds: int = 12

    def hash_password(self) -> bytes:
        try:
            if not self.salt:
                hashed = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt(self.rounds))
            else:
                hashed = bcrypt.hashpw(self.password.encode(), self.salt)
            logging.info(f"Hashed password using bcrypt: {hashed}")
            return hashed
        except Exception as e:
            logging.error(f"Error hashing password with bcrypt: {e}")
            raise

    def check_password(self, hashed: bytes) -> bool:
        try:
            result = bcrypt.checkpw(self.password.encode(), hashed)
            logging.info(f"Password verification result: {result}")
            return result
        except Exception as e:
            logging.error(f"Error verifying password with bcrypt: {e}")
            raise 