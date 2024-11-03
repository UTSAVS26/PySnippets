import string

ALPHABET_LENGTH = 26

class CaesarCipher:
    """
    A Caesar Cipher class that supports encryption, decryption, and brute-force decryption.
    """
    
    def __init__(self, shift=3):
        """
        Initializes the Caesar cipher with a given shift value.

        Parameters:
        - shift (int): The number of positions each letter is shifted in the alphabet.
        """
        self.shift = shift % ALPHABET_LENGTH
        self.encrypt_table = self._create_translation_table(self.shift)
        self.decrypt_table = self._create_translation_table(-self.shift)
    
    def _create_translation_table(self, shift):
        """
        Creates a translation table for encryption or decryption.

        Parameters:
        - shift (int): The number of positions each letter is shifted in the alphabet.

        Returns:
        - dict: A translation table for str.translate().
        """
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
        """
        Encrypts a message using the Caesar cipher.

        Parameters:
        - message (str): The plaintext message to encrypt.

        Returns:
        - str: The encrypted message.
        """
        if not isinstance(message, str):
            raise TypeError("Message must be a string")
        return message.translate(self.encrypt_table)
    
    def decrypt(self, encrypted_message):
        """
        Decrypts a message using the Caesar cipher.

        Parameters:
        - encrypted_message (str): The encrypted message to decrypt.

        Returns:
        - str: The decrypted message.
        """
        if not isinstance(encrypted_message, str):
            raise TypeError("Encrypted message must be a string")
        return encrypted_message.translate(self.decrypt_table)
    
    def brute_force_decrypt(self, encrypted_message):
        """
        Attempts to brute-force decrypt an encrypted message by trying all possible shifts.

        Parameters:
        - encrypted_message (str): The encrypted message to decrypt.

        Returns:
        - list: A list of tuples with shift values and corresponding decrypted messages.
        """
        possible_decryptions = []
        for potential_shift in range(ALPHABET_LENGTH):
            temp_table = self._create_translation_table(-potential_shift)
            decrypted = encrypted_message.translate(temp_table)
            possible_decryptions.append((potential_shift, decrypted))
        return possible_decryptions

def main():
    cipher = CaesarCipher(shift=3)
    original_message = "Hello, World!"
    print("Original Message:", original_message)
    
    # Encrypt the message
    encrypted_message = cipher.encrypt(original_message)
    print("Encrypted Message:", encrypted_message)
    
    # Decrypt the message
    decrypted_message = cipher.decrypt(encrypted_message)
    print("Decrypted Message:", decrypted_message)
    
    # Brute-force decryption
    print("\nBrute Force Decryption:")
    possible_decryptions = cipher.brute_force_decrypt(encrypted_message)
    for shift, decryption in possible_decryptions:
        print(f"Shift {shift}: {decryption}")
        print("-" * 30)

# Run the main function if this file is executed
if __name__ == "__main__":
    main()