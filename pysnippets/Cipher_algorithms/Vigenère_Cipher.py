class VigenereCipher:
    def __init__(self, key: str):
        """Initialize the Vigenère cipher with a key.

        Args:
            key (str): The key for the cipher, must be alphabetic.

        Raises:
            ValueError: If the key is not alphabetic.
        """
        if not key.isalpha():
            raise ValueError("Key must consist of alphabetic characters only.")
        self.key = key.upper()

    def _format_text(self, text: str) -> str:
        """Format the text by filtering non-alphabetic characters and converting to uppercase.

        Args:
            text (str): The text to format.

        Returns:
            str: Formatted text containing only uppercase alphabetic characters.
        """
        return ''.join(filter(str.isalpha, text)).upper()

    def _extend_key(self, text: str) -> str:
        """Extend the key to match the length of the text.

        Args:
            text (str): The text to match the key against.

        Returns:
            str: The extended key.
        """
        if not text:  # Check for empty text
            raise ValueError("Text cannot be empty.")
        key_length = len(self.key)
        extended_key = (self.key * (len(text) // key_length)) + self.key[:len(text) % key_length]
        return extended_key

    def encrypt(self, plaintext: str) -> str:
        """Encrypt the plaintext using the Vigenère cipher.

        Args:
            plaintext (str): The plaintext to encrypt.

        Returns:
            str: The encrypted ciphertext.
        """
        formatted_text = self._format_text(plaintext)
        extended_key = self._extend_key(formatted_text)
        ciphertext = []

        for p, k in zip(formatted_text, extended_key):
            encrypted_char = chr(((ord(p) - ord('A') + ord(k) - ord('A')) % 26) + ord('A'))
            ciphertext.append(encrypted_char)

        return ''.join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        """Decrypt the ciphertext using the Vigenère cipher.

        Args:
            ciphertext (str): The ciphertext to decrypt.

        Returns:
            str: The decrypted plaintext.
        """
        formatted_text = self._format_text(ciphertext)
        extended_key = self._extend_key(formatted_text)
        plaintext = []

        for c, k in zip(formatted_text, extended_key):
            decrypted_char = chr(((ord(c) - ord('A') - (ord(k) - ord('A'))) % 26) + ord('A'))
            plaintext.append(decrypted_char)

        return ''.join(plaintext)