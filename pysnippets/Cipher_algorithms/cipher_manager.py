from affine_cipher import AffineCipher
from caesar_cipher import CaesarCipher
from hill_cipher import HillCipher
from playfair_cipher import playfair_encrypt, playfair_decrypt
from Rail_Fence_Cipher import rail_fence_cipher_encrypt, rail_fence_cipher_decrypt
from Vigenère_Cipher import VigenereCipher

def encrypt_affine(plaintext, a, b):
    cipher = AffineCipher(a, b)
    return cipher.encrypt(plaintext)

def decrypt_affine(ciphertext, a, b):
    cipher = AffineCipher(a, b)
    return cipher.decrypt(ciphertext)

def encrypt_caesar(plaintext, shift):
    cipher = CaesarCipher(shift)
    return cipher.encrypt(plaintext)

def decrypt_caesar(ciphertext, shift):
    cipher = CaesarCipher(shift)
    return cipher.decrypt(ciphertext)

def encrypt_hill(plaintext, key_matrix):
    cipher = HillCipher(key_matrix)
    return cipher.encrypt(plaintext)

def decrypt_hill(ciphertext, key_matrix):
    cipher = HillCipher(key_matrix)
    return cipher.decrypt(ciphertext)

def encrypt_playfair(plaintext, key):
    return playfair_encrypt(plaintext, key)

def decrypt_playfair(ciphertext, key):
    return playfair_decrypt(ciphertext, key)

def encrypt_rail_fence(plaintext, key):
    return rail_fence_cipher_encrypt(plaintext, key)

def decrypt_rail_fence(ciphertext, key):
    return rail_fence_cipher_decrypt(ciphertext, key)

def encrypt_vigenere(plaintext, key):
    cipher = VigenereCipher(key)
    return cipher.encrypt(plaintext)

def decrypt_vigenere(ciphertext, key):
    cipher = VigenereCipher(key)
    return cipher.decrypt(ciphertext) 