
# ---------------------------------------------------------------------------
# Project: AI-VaultGuard | Machine Learning–Enhanced Password Manager
# File:    database_manager.py
# Author:  AHMED ZARAI
#
# Copyright (c) 2026 Ahmed Zarai. All rights reserved.
# ---------------------------------------------------------------------------

import sqlite3

def init_db():
    conn = sqlite3.connect("vault.db")
    cursor = conn.cursor()
    # We store the salt because we need it to recreate the key later
    cursor.execute('''CREATE TABLE IF NOT EXISTS config (id INTEGER PRIMARY KEY, salt BLOB)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS secrets 
                      (id INTEGER PRIMARY KEY, site TEXT, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def save_secret(site, user, encrypted_pw):
    conn = sqlite3.connect("vault.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO secrets (site, username, password) VALUES (?, ?, ?)", 
                   (site, user, encrypted_pw))
    conn.commit()
    conn.close()