from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.asymmetric import padding
import os

# Generate ECC private and public key pair
def generate_ecc_key_pair():
    private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

# Encrypt a message using the recipient's public key
def encrypt_message(public_key, message):
    # Generate a shared secret using ECDH (Elliptic Curve Diffie-Hellman)
    shared_key = public_key.exchange(ec.ECDH())
    
    # Derive a key from the shared secret using HKDF (Key derivation function)
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
        backend=default_backend()
    ).derive(shared_key)
    
    # Encrypt the message using derived symmetric key (AES encryption can be used here)
    iv = os.urandom(16)
    ciphertext = iv + derived_key  # Simplified placeholder, use symmetric encryption in practice
    return ciphertext

# Decrypt a message using the private key
def decrypt_message(private_key, ciphertext):
    # Extract IV and the actual ciphertext
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    
    # Generate shared secret using ECDH
    shared_key = private_key.exchange(ec.ECDH())
    
    # Derive the symmetric key using the shared secret
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
        backend=default_backend()
    ).derive(shared_key)
    
    # Decrypt using the derived symmetric key (AES decryption can be used)
    decrypted_message = actual_ciphertext  # Placeholder for actual decryption logic
    return decrypted_message

# Serialize private and public keys
def serialize_private_key(private_key):
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    return pem

def serialize_public_key(public_key):
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem

# Example usage
if __name__ == "__main__":
    message = b"Elliptic Curve Cryptography (ECC) example"
    
    # Generate ECC key pair
    private_key, public_key = generate_ecc_key_pair()

    # Encrypt the message
    encrypted_message = encrypt_message(public_key, message)
    print("Encrypted:", encrypted_message)
    
    # Decrypt the message
    decrypted_message = decrypt_message(private_key, encrypted_message)
    print("Decrypted:", decrypted_message.decode('utf-8'))

    # Serialize keys (optional)
    private_pem = serialize_private_key(private_key)
    public_pem = serialize_public_key(public_key)

    print("\nPrivate Key PEM format:\n", private_pem.decode('utf-8'))
    print("\nPublic Key PEM format:\n", public_pem.decode('utf-8'))
