

# ---------------------------------------------------------------------------
# Project: AI-VaultGuard | Machine Learning–Enhanced Password Manager
# File:    main.py
# Author:  AHMED ZARAI
#
# Copyright (c) 2026 Ahmed Zarai. All rights reserved.
# ---------------------------------------------------------------------------


import sqlite3
import hashlib
import re
import base64
import os
from sentinel import AISentinel
from cryptography.fernet import Fernet, InvalidToken

DB_NAME = "vault.db"
SALT_FILE = "salt.bin"
KDF_ITERATIONS = 200_000


# ===============================
# DATABASE SETUP
# ===============================

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS secrets (
            id INTEGER PRIMARY KEY,
            site TEXT NOT NULL,
            user TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ===============================
# SALT MANAGEMENT
# ===============================

def get_or_create_salt():
    if not os.path.exists(SALT_FILE):
        with open(SALT_FILE, "wb") as f:
            f.write(os.urandom(16))
    with open(SALT_FILE, "rb") as f:
        return f.read()


# ===============================
# KEY DERIVATION
# ===============================

def generate_key(master_password, salt):
    kdf = hashlib.pbkdf2_hmac(
        "sha256",
        master_password.encode(),
        salt,
        KDF_ITERATIONS
    )
    return base64.urlsafe_b64encode(kdf)


# ===============================
# ENCRYPTION / DECRYPTION
# ===============================

def encrypt_data(data, key):
    return Fernet(key).encrypt(data.encode()).decode()


def decrypt_data(data, key):
    return Fernet(key).decrypt(data.encode()).decode()


# ===============================
# MASTER PASSWORD VALIDATION
# ===============================

def setup_master_verification(key):
    """
    Stores a verification token encrypted with the master key.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT value FROM metadata WHERE key='verification'")
    row = cursor.fetchone()

    if row is None:
        token = encrypt_data("vault_verified", key)
        cursor.execute(
            "INSERT INTO metadata (key, value) VALUES (?, ?)",
            ("verification", token)
        )
        conn.commit()
        conn.close()
        return True

    conn.close()
    return True


def verify_master_password(key):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT value FROM metadata WHERE key='verification'")
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return False

    try:
        decrypted = decrypt_data(row[0], key)
        return decrypted == "vault_verified"
    except InvalidToken:
        return False


# ===============================
# PASSWORD STRENGTH CHECK
# ===============================

def check_password_strength(password):
    score = 0
    tips = []

    if len(password) >= 14:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        tips.append("❌ Too short (min 8 chars)")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        tips.append("❌ Mix upper and lower case")

    if re.search(r"\d", password):
        score += 1
    else:
        tips.append("❌ Add at least one number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        tips.append("❌ Add a special character")

    return score, tips


# ===============================
# VAULT OPERATIONS
# ===============================

def save_secret(site, user, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO secrets (site, user, password) VALUES (?, ?, ?)",
        (site, user, password)
    )
    conn.commit()
    conn.close()


def get_secrets():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT site, user, password FROM secrets")
    rows = cursor.fetchall()
    conn.close()
    return rows


# ===============================
# MAIN APPLICATION
# ===============================

def main():
    init_db()
    salt = get_or_create_salt()
    sentinel = AISentinel()

    print("\n" + "=" * 45)
    print("      🛡️  AI-VAULTGUARD SYSTEM ACTIVE")
    print("=" * 45 + "\n")

    master_pw = input("🔐 Enter Master Password: ")
    key = generate_key(master_pw, salt)

    # First-time setup or verification
    setup_master_verification(key)

    if not verify_master_password(key):
        print("❌ Incorrect Master Password. Access denied.")
        return

    print("✅ Vault unlocked successfully.\n")

    while True:
        print("\n--- 📂 VAULT MENU ---")
        print("1. Add Secret  2. View Secrets  3. Exit")
        choice = input("Select action: ")

        if choice == "1":
            site = input("🌐 Website URL: ")

            # AI Risk Analysis
            risk_score = sentinel.analyze_url(site)
            print(f"🔍 AI Risk Assessment: {risk_score*100:.1f}%")

            if risk_score >= 0.7:
                print("🛑 HIGH PHISHING RISK DETECTED.")
                if input("Discard entry? (y/n): ").lower() != "n":
                    continue
            elif risk_score >= 0.35:
                print("⚠️  Moderate risk. Verify URL authenticity.")

            user = input("👤 Username: ")

            # Password Strength Check
            while True:
                password = input("🔑 Enter Password: ")
                score, tips = check_password_strength(password)

                if score >= 4:
                    print("✅ Strong password.")
                    break
                else:
                    print("⚠️  Weak password:")
                    for tip in tips:
                        print(" ", tip)
                    if input("Save anyway? (y/n): ").lower() == "y":
                        break

            encrypted_pw = encrypt_data(password, key)
            save_secret(site, user, encrypted_pw)
            print("✨ Secret securely stored.")

        elif choice == "2":
            print("\n--- 🔓 SECURE RETRIEVAL ---")
            secrets = get_secrets()

            if not secrets:
                print("Vault is empty.")
            else:
                for site, user, enc_pw in secrets:
                    try:
                        decrypted = decrypt_data(enc_pw, key)
                        print(f"URL: {site} | User: {user} | Pass: {decrypted}")
                    except InvalidToken:
                        print(f"URL: {site} | ❌ Decryption failed.")

        elif choice == "3":
            print("🔒 Vault closed. Stay secure.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
