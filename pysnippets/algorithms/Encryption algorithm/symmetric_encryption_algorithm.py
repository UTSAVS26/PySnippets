from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Function to encrypt data
def encrypt(data, key):
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)
    # Create an AES Cipher object with the key and IV
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    # Encrypt the data
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return iv + ciphertext  # Return IV and ciphertext

# Function to decrypt data
def decrypt(ciphertext, key):
    # Extract the IV from the beginning of the ciphertext
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    # Create an AES Cipher object with the key and IV
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    # Decrypt the data
    return decryptor.update(actual_ciphertext) + decryptor.finalize()

# Example usage
if __name__ == "__main__":
    key = os.urandom(32)  # AES-256 key (32 bytes)
    data = b"Symmetric encryption example"
    
    # Encrypt the data
    encrypted_data = encrypt(data, key)
    print("Encrypted:", encrypted_data)
    
    # Decrypt the data
    decrypted_data = decrypt(encrypted_data, key)
    print("Decrypted:", decrypted_data.decode('utf-8'))
