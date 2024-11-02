class VigenereCipher:
    def __init__(self, key: str):
        if not key.isalpha():
            raise ValueError("Key must consist of alphabetic characters only.")
        self.key = key.upper()

    def _format_text(self, text: str) -> str:
        return ''.join(filter(str.isalpha, text)).upper()

    def _extend_key(self, text: str) -> str:
        key_length = len(self.key)
        extended_key = (self.key * (len(text) // key_length)) + self.key[:len(text) % key_length]
        return extended_key

    def encrypt(self, plaintext: str) -> str:
        formatted_text = self._format_text(plaintext)
        extended_key = self._extend_key(formatted_text)
        ciphertext = []

        for p, k in zip(formatted_text, extended_key):
            encrypted_char = chr(((ord(p) - ord('A') + ord(k) - ord('A')) % 26) + ord('A'))
            ciphertext.append(encrypted_char)

        return ''.join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        formatted_text = self._format_text(ciphertext)
        extended_key = self._extend_key(formatted_text)
        plaintext = []

        for c, k in zip(formatted_text, extended_key):
            decrypted_char = chr(((ord(c) - ord('A') - (ord(k) - ord('A'))) % 26) + ord('A'))
            plaintext.append(decrypted_char)

        return ''.join(plaintext)
