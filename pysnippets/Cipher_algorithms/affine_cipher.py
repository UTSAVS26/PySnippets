class AffineCipher:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.m = 26  # Length of the alphabet

    def encrypt(self, plaintext):
        return ''.join(
            chr(((self.a * (ord(char) - ord('A')) + self.b) % self.m) + ord('A'))
            if char.isalpha() else char for char in plaintext.upper()
        )

    def decrypt(self, ciphertext):
        a_inv = pow(self.a, -1, self.m)
        return ''.join(
            chr(((a_inv * ((ord(char) - ord('A')) - self.b)) % self.m) + ord('A'))
            if char.isalpha() else char for char in ciphertext.upper()
        )
