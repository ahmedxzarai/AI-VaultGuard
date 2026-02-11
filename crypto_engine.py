

# ---------------------------------------------------------------------------
# Project: AI-VaultGuard | Machine Learning–Enhanced Password Manager
# File:    crypto_engine.py
# Author:  AHMED ZARAI
#
# Copyright (c) 2026 Ahmed Zarai. All rights reserved.
# ---------------------------------------------------------------------------


import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def generate_key(master_password: str, salt: bytes):
    """Derives a 256-bit key from the master password."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000, # High iteration count to resist brute force
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key

def encrypt_data(data: str, key: bytes) -> str:
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def decrypt_data(token: str, key: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(token.encode()).decode()