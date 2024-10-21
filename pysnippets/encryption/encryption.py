from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import base64

class AESCipher:
    def __init__(self, key):
        self.key = key

    def pad(self, data):
        pad_length = AES.block_size - len(data) % AES.block_size
        return data + (chr(pad_length) * pad_length).encode()

    def unpad(self, data):
        pad_length = data[-1]
        return data[:-pad_length]

    def encrypt(self, data):
        data = self.pad(data)
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(data)
        return base64.b64encode(iv + encrypted_data).decode('utf-8')

    def decrypt(self, enc_data):
        enc_data = base64.b64decode(enc_data)
        iv = enc_data[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        data = cipher.decrypt(enc_data[AES.block_size:])
        return self.unpad(data).decode('utf-8')

def encrypt_file(file_path, cipher):
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = cipher.encrypt(file_data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data.encode())
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def encrypt_folder(folder_path, cipher):
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
    key = get_random_bytes(16)  # AES-128
    cipher = AESCipher(key)

    # Example usage
    file_path = 'path/to/your/file.txt'
    folder_path = 'path/to/your/folder'

    encrypt_file(file_path, cipher)
    encrypt_folder(folder_path, cipher)

if __name__ == "__main__":
    main()