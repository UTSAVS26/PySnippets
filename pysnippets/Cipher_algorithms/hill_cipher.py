import numpy as np

class HillCipher:
    def __init__(self, key_matrix):
        self.key_matrix = np.array(key_matrix)
        self.modulus = 26
        self.check_key_matrix()

    def check_key_matrix(self):
        if self.key_matrix.shape[0] != self.key_matrix.shape[1]:
            raise ValueError("Key matrix must be square")
        if np.linalg.det(self.key_matrix) == 0:
            raise ValueError("Key matrix must be invertible")

    def encrypt(self, plaintext):
        plaintext = plaintext.upper().replace(" ", "")
        if len(plaintext) % self.key_matrix.shape[0] != 0:
            raise ValueError("Plaintext length must be a multiple of key matrix size")
        
        plaintext_vector = [ord(char) - ord('A') for char in plaintext]
        plaintext_matrix = np.array(plaintext_vector).reshape(-1, self.key_matrix.shape[0])
        
        encrypted_matrix = np.dot(plaintext_matrix, self.key_matrix) % self.modulus
        encrypted_text = ''.join(chr(int(num) + ord('A')) for num in encrypted_matrix.flatten())
        
        return encrypted_text

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper().replace(" ", "")
        if len(ciphertext) % self.key_matrix.shape[0] != 0:
            raise ValueError("Ciphertext length must be a multiple of key matrix size")
        
        ciphertext_vector = [ord(char) - ord('A') for char in ciphertext]
        ciphertext_matrix = np.array(ciphertext_vector).reshape(-1, self.key_matrix.shape[0])
        
        inverse_key_matrix = np.linalg.inv(self.key_matrix)
        adjugate_matrix = np.round(inverse_key_matrix * np.linalg.det(self.key_matrix)).astype(int) % self.modulus
        determinant = int(np.round(np.linalg.det(self.key_matrix))) % self.modulus
        determinant_inv = pow(determinant, -1, self.modulus)
        inverse_key_matrix_mod = (determinant_inv * adjugate_matrix) % self.modulus
        
        decrypted_matrix = np.dot(ciphertext_matrix, inverse_key_matrix_mod) % self.modulus
        decrypted_text = ''.join(chr(int(num) + ord('A')) for num in decrypted_matrix.flatten())
        
        return decrypted_text
