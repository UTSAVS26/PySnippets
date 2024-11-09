import bcrypt
from logging_config import logger

class Hasher:
    def hash_password(self, password):
        try:
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
            return hashed.decode('utf-8')
        except Exception as e:
            logger.error("Error hashing password: %s", str(e))
            raise

    def verify_password(self, password, hashed):
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
        except Exception as e:
            logger.error("Error verifying password: %s", str(e))
            raise 