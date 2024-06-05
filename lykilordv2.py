import os
import hashlib
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def aes256_encrypt(plaintext: str, key: str) -> bytes:
    # Generate a 256-bit (32-byte) key from the string using SHA-256
    key = hashlib.sha256(key.encode()).digest()
    
    # Fixed IV to ensure deterministic output (for demonstration purposes, in practice, IV should be random)
    iv = b'1234567890123456'
    
    # Pad the plaintext to be compatible with block size (128 bits for AES)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext.encode()) + padder.finalize()
    
    # Create AES cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    # Return the IV concatenated with the ciphertext (to be used together for decryption)
    return iv + ciphertext

def ensure_password_requirements(password: str) -> str:
    # Ensure the password contains at least one uppercase letter, one lowercase letter, and one symbol
    if not any(c.isupper() for c in password):
        password = 'A' + password[1:]
    if not any(c.islower() for c in password):
        password = password[:1] + 'a' + password[2:]
    if not any(c in '!@#$%^&*()_+-=[]{}|\\' for c in password):
        password = password[:2] + '!' + password[3:]
    
    return password

def main():
    four_digit_number = input("Enter a four-digit number: ")
    string = input("Enter a string: ")
    
    if not (four_digit_number.isdigit() and len(four_digit_number) == 4):
        print("Error: The input must be a four-digit number.")
        return
    
    encrypted_result = aes256_encrypt(four_digit_number, string)
    
    # Convert the encrypted result to a base64 string to ensure it is printable
    base64_encoded = base64.b64encode(encrypted_result).decode('utf-8')
    
    # Ensure the base64 string meets password requirements
    password = ensure_password_requirements(base64_encoded)
    
    # Print the final password
    print("Generated password:", password)

if __name__ == "__main__":
    main()