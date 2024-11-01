import string

class CaesarCipher:
    def __init__(self, shift=3):
        self.shift = shift % 26
        self.encrypt_table = self._create_translation_table(self.shift)
        self.decrypt_table = self._create_translation_table(-self.shift)
    
    def _create_translation_table(self, shift):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        lower_shifted = lower[shift:] + lower[:shift]
        upper_shifted = upper[shift:] + upper[:shift]
        trans_table = str.maketrans(
            lower + upper,
            lower_shifted + upper_shifted
        )
        return trans_table
    
    def encrypt(self, message):
        if not isinstance(message, str):
            raise TypeError("Message must be a string")
        return message.translate(self.encrypt_table)
    
    def decrypt(self, encrypted_message):
        if not isinstance(encrypted_message, str):
            raise TypeError("Encrypted message must be a string")
        return encrypted_message.translate(self.decrypt_table)
    
    def brute_force_decrypt(self, encrypted_message):
        possible_decryptions = []
        for potential_shift in range(26):
            temp_cipher = CaesarCipher(shift=potential_shift)
            decrypted = temp_cipher.decrypt(encrypted_message)
            possible_decryptions.append((potential_shift, decrypted))
        return possible_decryptions

def main():
    cipher = CaesarCipher()
    original_message = "Hello, World!"
    print("Original Message:", original_message)
    encrypted_message = cipher.encrypt(original_message)
    print("Encrypted Message:", encrypted_message)
    decrypted_message = cipher.decrypt(encrypted_message)
    print("Decrypted Message:", decrypted_message)
    print("\nBrute Force Decryption:")
    possible_decryptions = cipher.brute_force_decrypt(encrypted_message)
    for shift, decryption in possible_decryptions:
        print(f"Shift {shift}: {decryption}")