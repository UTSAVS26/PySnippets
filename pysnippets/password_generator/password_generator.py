import random
import string
from validators import PasswordValidator
from hasher import Hasher
from logging_config import logger

class PasswordGenerator:
    def __init__(self, length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
        self.length = length
        self.use_upper = use_upper
        self.use_lower = use_lower
        self.use_digits = use_digits
        self.use_symbols = use_symbols
        self.validator = PasswordValidator()
        self.hasher = Hasher()
        logger.info("PasswordGenerator initialized with length=%d, upper=%s, lower=%s, digits=%s, symbols=%s",
                    length, use_upper, use_lower, use_digits, use_symbols)

    def generate_password(self):
        try:
            character_pool = ''
            if self.use_upper:
                character_pool += string.ascii_uppercase
            if self.use_lower:
                character_pool += string.ascii_lowercase
            if self.use_digits:
                character_pool += string.digits
            if self.use_symbols:
                character_pool += string.punctuation
            if not character_pool:
                raise ValueError("At least one character type must be selected.")
            password = ''.join(random.choice(character_pool) for _ in range(self.length))
            if not self.validator.validate(password):
                raise ValueError("Generated password does not meet validation criteria.")
            hashed_password = self.hasher.hash_password(password)
            logger.info("Password generated and hashed successfully.")
            return password, hashed_password
        except Exception as e:
            logger.error("Error generating password: %s", str(e))
            raise 