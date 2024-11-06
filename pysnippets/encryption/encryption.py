import os
import base64
import logging
from dataclasses import dataclass
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class EncryptionResult:
    file_path: str
    success: bool
    message: str

class AESCipher:
    """
    A class to perform AES encryption and decryption.

    Attributes:
        key (bytes): The AES key used for encryption and decryption.
    """

    def __init__(self, key: bytes):
        """
        Initializes the AESCipher with a given key.

        Args:
            key (bytes): The AES key (should be either 16, 24, or 32 bytes long).
        """
        self.key = key

    @staticmethod
    def generate_key(passphrase: str, salt: bytes) -> bytes:
        """
        Generates a secure AES key from a passphrase and salt using PBKDF2.

        Args:
            passphrase (str): The user's passphrase.
            salt (bytes): A unique salt for the key derivation.

        Returns:
            bytes: The derived AES key.
        """
        return PBKDF2(passphrase, salt, dkLen=32, count=1000000)

    def pad(self, data: bytes) -> bytes:
        """
        Pads the data to make its length a multiple of the AES block size.

        Args:
            data (bytes): The data to pad.

        Returns:
            bytes: The padded data.
        """
        pad_length = AES.block_size - len(data) % AES.block_size
        return data + (chr(pad_length) * pad_length).encode()

    def unpad(self, data: bytes) -> bytes:
        """
        Removes padding from the decrypted data.

        Args:
            data (bytes): The padded data.

        Returns:
            bytes: The unpadded data.
        """
        pad_length = data[-1]
        return data[:-pad_length]

    def encrypt(self, data: bytes) -> str:
        """
        Encrypts the given data using AES encryption.

        Args:
            data (bytes): The data to encrypt.

        Returns:
            str: The encrypted data encoded in base64.
        """
        data = self.pad(data)
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(data)
        return base64.b64encode(iv + encrypted_data).decode("utf-8")

    def decrypt(self, enc_data: str) -> str:
        """
        Decrypts the given encrypted data using AES decryption.

        Args:
            enc_data (str): The encrypted data encoded in base64.

        Returns:
            str: The decrypted data.
        """
        enc_data = base64.b64decode(enc_data)
        iv = enc_data[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        data = cipher.decrypt(enc_data[AES.block_size:])
        return self.unpad(data).decode("utf-8")

    def encrypt_file(self, file_path: str) -> EncryptionResult:
        """
        Encrypts the contents of a file.

        Args:
            file_path (str): The path to the file to encrypt.

        Returns:
            EncryptionResult: Result of the encryption operation.
        """
        try:
            with open(file_path, "rb") as file:
                file_data = file.read()
            encrypted_data = self.encrypt(file_data)
            with open(file_path, "wb") as file:
                file.write(encrypted_data.encode())
            logging.info(f"Successfully encrypted: {file_path}")
            return EncryptionResult(file_path, True, "Encryption successful.")
        except FileNotFoundError:
            logging.error(f"File {file_path} not found.")
            return EncryptionResult(file_path, False, "File not found.")
        except Exception as e:
            logging.error(f"An error occurred while encrypting {file_path}: {e}")
            return EncryptionResult(file_path, False, str(e))

    def decrypt_file(self, file_path: str) -> EncryptionResult:
        """
        Decrypts the contents of a file.

        Args:
            file_path (str): The path to the file to decrypt.

        Returns:
            EncryptionResult: Result of the decryption operation.
        """
        try:
            with open(file_path, "rb") as file:
                encrypted_data = file.read()
            decrypted_data = self.decrypt(encrypted_data.decode())
            with open(file_path, "wb") as file:
                file.write(decrypted_data.encode())
            logging.info(f"Successfully decrypted: {file_path}")
            return EncryptionResult(file_path, True, "Decryption successful.")
        except FileNotFoundError:
            logging.error(f"File {file_path} not found.")
            return EncryptionResult(file_path, False, "File not found.")
        except Exception as e:
            logging.error(f"An error occurred while decrypting {file_path}: {e}")
            return EncryptionResult(file_path, False, str(e))

    def encrypt_folder(self, folder_path: str) -> None:
        """
        Encrypts all files in a specified folder.

        Args:
            folder_path (str): The path to the folder containing files to encrypt.
        """
        try:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    self.encrypt_file(file_path)
        except FileNotFoundError:
            logging.error(f"Folder {folder_path} not found.")
        except Exception as e:
            logging.error(f"An error occurred while encrypting files in {folder_path}: {e}")

    def decrypt_folder(self, folder_path: str) -> None:
        """
        Decrypts all files in a specified folder.

        Args:
            folder_path (str): The path to the folder containing files to decrypt.
        """
        try:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    self.decrypt_file(file_path)
        except FileNotFoundError:
            logging.error(f"Folder {folder_path} not found.")
        except Exception as e:
            logging.error(f"An error occurred while decrypting files in {folder_path}: {e}")

def main() -> None:
    """
    The main function that initializes the AESCipher and encrypts/decrypts specified files and folders.
    """
    passphrase = input("Enter a passphrase for encryption/decryption: ")
    salt = get_random_bytes(16)  # This should be securely stored to decrypt later
    key = AESCipher.generate_key(passphrase, salt)
    cipher = AESCipher(key)

    operation = input("Would you like to (e)ncrypt or (d)ecrypt? ").strip().lower()
    
    if operation == 'e':
        file_path = input("Enter the path to the file to encrypt: ")
        folder_path = input("Enter the path to the folder to encrypt (or leave blank): ")
        cipher.encrypt_file(file_path)
        if folder_path:
            cipher.encrypt_folder(folder_path)
    elif operation == 'd':
        file_path = input("Enter the path to the file to decrypt: ")
        folder_path = input("Enter the path to the folder to decrypt (or leave blank): ")
        cipher.decrypt_file(file_path)
        if folder_path:
            cipher.decrypt_folder(folder_path)
    else:
        logging.error("Invalid operation selected.")

if __name__ == "__main__":
    main()