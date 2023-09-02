#!/usr/bin/python env

from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

def encrypt_text(text, key):
    # Ensure the key is 16 bytes (Triple DES key size)
    if len(key) != 16:
        raise ValueError("Key must be 16 bytes long.")

    # Generate a random IV (Initialization Vector)
    iv = get_random_bytes(8)

    # Create a Triple DES cipher object in CBC mode
    cipher = DES3.new(key, DES3.MODE_CBC, iv)

    # Pad the plaintext to be a multiple of 8 bytes (DES block size)
    plaintext_padded = text + (8 - len(text) % 8) * chr(8 - len(text) % 8)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext_padded.encode('utf-8'))

    # Combine the IV and ciphertext, and encode it as base64
    result = b64encode(iv + ciphertext).decode('utf-8')

    return result

# Input text and encryption key
input_text = "h33l_up_th1ng5"
encryption_key = b"mysecretpassword"  # 16 bytes key

# Encrypt the text
encrypted_text = encrypt_text(input_text, encryption_key)

print("Encrypted Text:", encrypted_text)



# from Crypto.Util.number import bytes_to_long as bf

# ssh_key = """hello"""

# # Convert the multiline string to binary data
# multiline_string_bytes = ssh_key.encode('utf-8')

# # Convert bytes to an integer
# integer_value = bf(multiline_string_bytes)

# # Convert the integer back to bytes
# restored_bytes = bf(integer_value)

# # Convert bytes back to a string
# restored_multiline_string = restored_bytes.decode('utf-8')

# print("Original Multiline String:")
# print(ssh_key)

# print("\nMultiline String as Binary Data:")
# print(multiline_string_bytes)

# print("\nInteger Value:")
# print(integer_value)

# print("\nRestored Multiline String:")
# print(restored_multiline_string)



