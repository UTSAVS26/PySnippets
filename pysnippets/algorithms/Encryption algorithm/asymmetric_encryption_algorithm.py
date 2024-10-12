from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Generate RSA key pair
def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Encrypt data using public key
def encrypt(public_key, message):
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

# Decrypt data using private key
def decrypt(private_key, ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext

# Serialize the private key to save it to a file
def serialize_private_key(private_key, password=None):
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(password) if password else serialization.NoEncryption()
    )
    return pem

# Serialize the public key to save it to a file
def serialize_public_key(public_key):
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem

# Example usage
if __name__ == "__main__":
    message = b"Asymmetric encryption example with RSA"
    
    # Generate RSA key pair
    private_key, public_key = generate_key_pair()

    # Encrypt the message
    ciphertext = encrypt(public_key, message)
    print("Encrypted:", ciphertext)
    
    # Decrypt the message
    decrypted_message = decrypt(private_key, ciphertext)
    print("Decrypted:", decrypted_message.decode('utf-8'))

    # Optional: Serialize keys if you want to save them
    private_pem = serialize_private_key(private_key, password=b'mypassword')
    public_pem = serialize_public_key(public_key)

    print("\nPrivate Key PEM format:\n", private_pem.decode('utf-8'))
    print("\nPublic Key PEM format:\n", public_pem.decode('utf-8'))
