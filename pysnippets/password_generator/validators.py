import re

class PasswordValidator:
    def __init__(self, min_length=8, max_length=64, require_upper=True, require_lower=True, require_digits=True, require_symbols=True):
        self.min_length = min_length
        self.max_length = max_length
        self.require_upper = require_upper
        self.require_lower = require_lower
        self.require_digits = require_digits
        self.require_symbols = require_symbols

    def validate(self, password):
        if not (self.min_length <= len(password) <= self.max_length):
            return False
        if self.require_upper and not re.search(r'[A-Z]', password):
            return False
        if self.require_lower and not re.search(r'[a-z]', password):
            return False
        if self.require_digits and not re.search(r'\d', password):
            return False
        if self.require_symbols and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False
        return True 