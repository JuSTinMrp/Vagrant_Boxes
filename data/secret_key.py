#!/usr/bin/python env

import secrets

def generate_16_byte_key():
    # Generate a secure random key with 16 bytes (128 bits)
    key = secrets.token_bytes(16)
    return key

# Generate a 16-byte key
key = generate_16_byte_key()

# Print the generated key in hexadecimal format
print("Generated Key (Hexadecimal):", key.hex())
