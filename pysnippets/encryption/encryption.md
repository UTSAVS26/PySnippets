# Encryption Module

## Overview

This module provides a robust and secure way to encrypt and decrypt files and folders using AES encryption, ensuring data confidentiality. It supports both file and folder encryption, making it suitable for various use cases. This module uses the `pycryptodome` library, which is a self-contained Python package of low-level cryptographic primitives.

## Table of Contents

- [Introduction](#introduction)
- [Functionality](#functionality)
  - [AESCipher](#aes-cipher)
    - [Initialization](#initialization)
    - [Padding](#padding)
    - [Encryption](#encryption)
    - [Decryption](#decryption)
    - [File and Folder Encryption](#file-and-folder-encryption)
- [Usage Examples](#usage-examples)
- [Requirements](#requirements)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

The **Encryption Module** provides a robust and secure way to encrypt and decrypt files and folders using AES encryption. This module uses the `pycryptodome` library, which is a self-contained Python package of low-level cryptographic primitives.

---

## Functionality

### AESCipher

The `AESCipher` class implements AES encryption and decryption.

#### Initialization

To initialize an `AESCipher`, you need to provide a key.

```python
cipher = AESCipher(key)
```

### Args:

- `key (bytes)`: A byte string (16, 24, or 32 bytes long) used for AES encryption.

#### Padding

The `pad(data)` method ensures the data is a multiple of the AES block size.

```python
padded_data = cipher.pad(data)
```

#### Encryption

To encrypt data, use the `encrypt(data)` method.

```python
encrypted_data = cipher.encrypt(data)
```

### Args:

- `data (bytes)`: The data to encrypt.

### Returns:

- `str`: The encrypted data encoded in base64.

#### Decryption

To decrypt data, use the `decrypt(enc_data)` method.

```python
decrypted_data = cipher.decrypt(enc_data)
```

### Args:

- `enc_data (str)`: The encrypted data encoded in base64.

### Returns:

- `str`: The decrypted data.

#### File and Folder Encryption

You can encrypt individual files or all files within a folder.

```python
encrypt_file(file_path, cipher)
```

### Args:

- `file_path (str)`: The path to the file to encrypt.
- `cipher (AESCipher)`: The AESCipher instance used for encryption.

```python
encrypt_folder(folder_path, cipher)
```

### Args:

- `folder_path (str)`: The path to the folder containing files to encrypt.
- `cipher (AESCipher)`: The AESCipher instance used for encryption.

## Usage Examples

Here is a basic example of how to use the Encryption Module:

```python
from Crypto.Random import get_random_bytes

from encryption import AESCipher, encrypt_file, decrypt_file

# Generate a key (use a secure method in production)
key = get_random_bytes(16)  # Example for AES-128
cipher = AESCipher(key)

# Encrypt a file
encrypt_file('path/to/your/file.txt', cipher)

# Decrypt the file
decrypt_file('path/to/your/file.txt', cipher)
```

### Instructions

1. **Install Dependencies**: Ensure you have the `pycryptodome` library installed. You can install it using pip:

   ```bash
   pip install pycryptodome
   ```

2. **Generate a Key**: Use a secure method to generate a key. The key should be either 16, 24, or 32 bytes long.

3. **Initialize the AESCipher**: Create an instance of the `AESCipher` class with the generated key.

4. **Encrypt/Decrypt Files**: Use the `encrypt_file` and `decrypt_file` functions to encrypt and decrypt files, respectively.

5. **Encrypt/Decrypt Folders**: Use the `encrypt_folder` and `decrypt_folder` functions to encrypt and decrypt all files within a specified folder.

## Requirements

This module requires the `pycryptodome` library. You can install it using pip:

```bash
pip install pycryptodome
```

## Testing

To run the tests for the `AESCipher` class, execute the following command in the terminal:

```bash
python -m unittest test_encryption.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
