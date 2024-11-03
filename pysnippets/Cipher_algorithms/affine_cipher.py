class AffineCipher:
    """
    A class to implement the Affine Cipher for encryption and decryption.
    """
    
    ALPHABET_LENGTH = 26  # Length of the alphabet

    def __init__(self, a, b):
        """
        Initializes the Affine Cipher with specified coefficients.

        Parameters:
        - a (int): The multiplicative key (must be coprime with ALPHABET_LENGTH).
        - b (int): The additive key.
        """
        if not self.is_valid_key(a):
            raise ValueError(f"The value of 'a' ({a}) must be coprime with {self.ALPHABET_LENGTH}.")
        
        self.a = a
        self.b = b
        self.m = self.ALPHABET_LENGTH  # Length of the alphabet

    def is_valid_key(self, a):
        """
        Checks if 'a' is coprime with the alphabet length.

        Parameters:
        - a (int): The multiplicative key.

        Returns:
        - bool: True if 'a' is coprime with ALPHABET_LENGTH, False otherwise.
        """
        return self.gcd(a, self.m) == 1

    def gcd(self, x, y):
        """Compute the greatest common divisor of x and y."""
        while y:
            x, y = y, x % y
        return x

    def encrypt(self, plaintext):
        """
        Encrypts the plaintext using the affine cipher.

        Parameters:
        - plaintext (str): The text to encrypt.

        Returns:
        - str: The encrypted ciphertext.
        """
        return ''.join(
            chr(((self.a * (ord(char) - ord('A')) + self.b) % self.m) + ord('A'))
            if char.isalpha() else char for char in plaintext.upper()
        )

    def decrypt(self, ciphertext):
        """
        Decrypts the ciphertext using the affine cipher.

        Parameters:
        - ciphertext (str): The text to decrypt.

        Returns:
        - str: The decrypted plaintext.
        """
        a_inv = pow(self.a, -1, self.m)  # Modular multiplicative inverse of a
        return ''.join(
            chr(((a_inv * ((ord(char) - ord('A')) - self.b)) % self.m) + ord('A'))
            if char.isalpha() else char for char in ciphertext.upper()
        )