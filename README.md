
🛡️ AI-VaultGuard
Developed by AHMED ZARAI | 2026

Machine Learning–Enhanced Password Manager (Local-First, AES-256 Secured)

A security-focused password manager that integrates machine learning–based phishing detection with industry-standard encryption, built using a local-first architecture.

Demonstrates applied ML, cryptographic implementation, and secure software design in Python.
Engineering AI-driven security systems that anticipate threats, not just react to them.

⚡ Core Capabilities

• Phishing Detection Engine
Random Forest classifier trained on engineered URL features (structure, entropy, keyword patterns) for real-time risk assessment.
• AES-256 Encrypted Vault
Credentials encrypted using Fernet (AES-256) derived from a Master Password.
No plaintext storage. No cloud dependency.
• Strength Meter (Real-Time Password Analysis)
Entropy-aware complexity scoring before vault insertion.
• Local Secure Storage
SQLite3-backed encrypted database (vault.db).

🏗 Architecture

URL Input ──► Feature Engineering ──► Random Forest ──► Risk Score
Password ───► Strength Analysis ────► AES-256 Encryption ─► SQLite Vault

Clear separation between:

• Training pipeline (train_sentinel.py)
• Inference engine (sentinel.py)
• Application layer (main.py)

🧠 Machine Learning

• Algorithm: Random Forest (scikit-learn)
• Custom URL feature extraction
• Shannon entropy analysis
• Structural + lexical phishing indicators
• Serialized model for production inference

🔐 Security Highlights

• Random persistent salt + PBKDF2 (200,000 iterations) for master key derivation
• Master-password verification token (fail-fast login)
• AES-256 encryption (Fernet) for all secrets
• Parameterized SQL queries to prevent injection
• Local-only storage (no cloud dependency)
• Zero plaintext credentials

## 🚀 Run Locally

```bash
git clone https://github.com/ahmedxzarai/AI-VaultGuard.git
cd AI-VaultGuard
pip install -r requirements.txt
```

📂 Preparing the Training Data

The dataset is too large to host on GitHub. To set up the AI model, follow these steps:
Visit the Kaggle dataset page: Malicious URLs Dataset: [https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset]
Click Download and extract the zip file.
Rename the extracted CSV file to urldata.csv and place it in the project directory.
Train the AI model by running:

```bash
python train_sentinel.py
python main.py
```
After training, the AI Sentinel will be ready for real-time phishing detection in the vault.

🛠 Tech Stack

Python • scikit-learn • cryptography • SQLite3 • Feature Engineering • Cybersecurity ML

🎯 Engineering Value

• Applied machine learning in cybersecurity context
• Secure cryptographic implementation
• Modular and extensible design
• Clear separation of ML training vs inference
• Production-minded local-first architecture

🎯 Future Improvements

• Argon2 or scrypt key derivation
• Memory wipe for decrypted passwords
• Auto-lock / session timeout
• GUI (Tkinter / PyQt / Web)
• Browser extension integration
• Unit and integration tests




📜 License \& Copyright
Copyright © 2026 AHMED ZARAI. Distributed under the MIT License. See LICENSE for more information.




