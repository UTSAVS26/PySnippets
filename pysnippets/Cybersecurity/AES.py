from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import base64

def generate_key():
    # Generate a random 256-bit (32-byte) key
    return os.urandom(32)

def encrypt(plaintext, key):
    # Generate a random 16-byte IV (initialization vector)
    iv = os.urandom(16)
    
    # Create a Cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Create an encryptor
    encryptor = cipher.encryptor()
    
    # Pad the plaintext to be a multiple of 16 bytes
    pad_length = 16 - len(plaintext) % 16
    padded_plaintext = plaintext + bytes([pad_length] * pad_length)
    
    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    # Return IV and ciphertext, both encoded in base64 for easier handling
    return base64.b64encode(iv + ciphertext).decode()

def decrypt(ciphertext_b64, key):
    # Decode the base64 encoded ciphertext
    ciphertext = base64.b64decode(ciphertext_b64)
    
    # Extract the IV from the ciphertext
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    
    # Create a Cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Create a decryptor
    decryptor = cipher.decryptor()
    
    # Decrypt the ciphertext
    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()
    
    # Remove padding
    pad_length = padded_plaintext[-1]
    return padded_plaintext[:-pad_length]

# Example usage
if __name__ == "__main__":
    key = generate_key()
    plaintext = input("Enter the plaintext (string to encrypt): ").encode()
    
    print("Original:", plaintext)

    # Encrypt
    ciphertext = encrypt(plaintext, key)
    print("Encrypted:", ciphertext)

    # Decrypt
    decrypted_plaintext = decrypt(ciphertext, key)
    print("Decrypted:", decrypted_plaintext)
