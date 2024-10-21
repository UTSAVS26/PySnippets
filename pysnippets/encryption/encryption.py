from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import base64


class AESCipher:
    """
    A class to perform AES encryption and decryption.

    Attributes:
        key (bytes): The AES key used for encryption and decryption.
    """

    def __init__(self, key):
        """
        Initializes the AESCipher with a given key.

        Args:
            key (bytes): The AES key (should be either 16, 24, or 32 bytes long).
        """
        self.key = key

    def pad(self, data):
        """
        Pads the data to make its length a multiple of the AES block size.

        Args:
            data (bytes): The data to pad.

        Returns:
            bytes: The padded data.
        """
        pad_length = AES.block_size - len(data) % AES.block_size
        return data + (chr(pad_length) * pad_length).encode()

    def unpad(self, data):
        """
        Removes padding from the decrypted data.

        Args:
            data (bytes): The padded data.

        Returns:
            bytes: The unpadded data.
        """
        pad_length = data[-1]
        return data[:-pad_length]

    def encrypt(self, data):
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

    def decrypt(self, enc_data):
        """
        Decrypts the given encrypted data using AES decryption.

        Args:
            enc_data (str): The encrypted data encoded in base64.

        Returns:
            str: The decrypted data.
        """
        enc_data = base64.b64decode(enc_data)
        iv = enc_data[: AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        data = cipher.decrypt(enc_data[AES.block_size :])
        return self.unpad(data).decode("utf-8")


def encrypt_file(file_path, cipher):
    """
    Encrypts the contents of a file.

    Args:
        file_path (str): The path to the file to encrypt.
        cipher (AESCipher): The AESCipher instance used for encryption.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
        encrypted_data = cipher.encrypt(file_data)
        with open(file_path, "wb") as file:
            file.write(encrypted_data.encode())
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def encrypt_folder(folder_path, cipher):
    """
    Encrypts all files in a specified folder.

    Args:
        folder_path (str): The path to the folder containing files to encrypt.
        cipher (AESCipher): The AESCipher instance used for encryption.

    Raises:
        FileNotFoundError: If the specified folder does not exist.
    """
    try:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                encrypt_file(file_path, cipher)
    except FileNotFoundError:
        print(f"Folder {folder_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    The main function that initializes the AESCipher and encrypts specified files and folders.
    """
    key = get_random_bytes(16)  # AES-128
    cipher = AESCipher(key)

    # Example usage
    file_path = "path/to/your/file.txt"
    folder_path = "path/to/your/folder"

    encrypt_file(file_path, cipher)
    encrypt_folder(folder_path, cipher)


if __name__ == "__main__":
    main()
