from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Function to pad data to fit AES block size (16 bytes)
def pad(data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data

# Function to remove padding after decryption
def unpad(data):
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(data) + unpadder.finalize()
    return unpadded_data

# Function to encrypt data
def aes_encrypt(data, key):
    iv = os.urandom(16)  # Generate a random 16-byte IV (Initialization Vector)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Pad the data to make it a multiple of the block size (16 bytes)
    padded_data = pad(data)
    
    # Encrypt the data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext  # Return the IV concatenated with the ciphertext

# Function to decrypt data
def aes_decrypt(ciphertext, key):
    iv = ciphertext[:16]  # Extract the IV from the beginning
    actual_ciphertext = ciphertext[16:]
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt the data
    padded_data = decryptor.update(actual_ciphertext) + decryptor.finalize()
    
    # Remove padding
    return unpad(padded_data)

# Example usage
if __name__ == "__main__":
    key = os.urandom(32)  # AES-256 key (32 bytes)
    data = b"Advanced Encryption Standard (AES) example"
    
    # Encrypt the data
    encrypted_data = aes_encrypt(data, key)
    print("Encrypted:", encrypted_data)
    
    # Decrypt the data
    decrypted_data = aes_decrypt(encrypted_data, key)
    print("Decrypted:", decrypted_data.decode('utf-8'))
