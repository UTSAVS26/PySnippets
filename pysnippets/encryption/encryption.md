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
- **Args**: 
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
- **Args**: 
  - `data (bytes)`: The data to encrypt.
- **Returns**: 
  - `str`: The encrypted data encoded in base64.

#### Decryption

To decrypt data, use the `decrypt(enc_data)` method.

```python
decrypted_data = cipher.decrypt(enc_data)
```
- **Args**: 
  - `enc_data (str)`: The encrypted data encoded in base64.
- **Returns**: 
  - `str`: The decrypted data.

---

### File and Folder Encryption

You can encrypt individual files or all files within a folder.

#### Encrypt a File

```python
encrypt_file(file_path, cipher)
```
- **Args**: 
  - `file_path (str)`: The path to the file to encrypt.
  - `cipher (AESCipher)`: The AESCipher instance used for encryption.

#### Encrypt a Folder

```python
encrypt_folder(folder_path, cipher)
```
- **Args**: 
  - `folder_path (str)`: The path to the folder containing files to encrypt.
  - `cipher (AESCipher)`: The AESCipher instance used for encryption.

## Requirements

This module requires the `pycryptodome` library. You can install it using pip:

```bash
pip install pycryptodome
```
