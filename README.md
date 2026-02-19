<div align="center">
  <h1>🛡️ AI-VaultGuard</h1>
  <p><b>Machine Learning–Enhanced Password Manager | Local-First AES-256 Security</b></p>

  ![Python](https://img.shields.io/badge/python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
  ![Security](https://img.shields.io/badge/Encryption-AES--256-red?style=for-the-badge)
  ![Architecture](https://img.shields.io/badge/Logic-Local--First-9cf?style=for-the-badge)

  <p><i>Engineering AI-driven security systems that anticipate threats, not just react to them.</i></p>
</div>

---

### 🧠 Sentinel AI Model Details
The system utilizes an integrated intelligence layer designed to detect phishing attempts before credentials are even entered.

* *Algorithm:* Random Forest Classifier (via Scikit-Learn).
* *Feature Engineering:* Custom extraction of URL metadata including:
    * *Shannon Entropy:* Quantifying the randomness of the domain string to identify algorithmically generated domains.
    * *Lexical Analysis:* Identifying malicious keyword patterns and structural anomalies.
    * *Tld/Path Ratios:* Analyzing domain hierarchy for redirection tactics.
* *Architecture:* Separation of concerns between the training pipeline (train_sentinel.py) and high-speed production inference (sentinel.py).
* *Performance:* Serialized model for near-instant validation during runtime.

---

### 🔐 Security Highlights
AI-VaultGuard is built on a "Trust-No-One" local-first architecture.

| Security Layer | Implementation Detail |
| :--- | :--- |
| *Master Key Derivation* | PBKDF2 with 200,000 iterations + Random Persistent Salt |
| *Data Encryption* | Fernet (Authenticated AES-256 in CBC mode) |
| *Vault Storage* | SQLite3 with strict Parameterized Queries (SQLi Defense) |
| *Authentication* | Master-password verification token (Safe fail-fast login) |
| *Zero-Cloud Policy* | 100% Offline execution; no plaintext data ever touches the disk |
| *Strength Analysis* | Real-time entropy-based complexity scoring for new entries |

---

### 📦 Project Structure
```text
AI-VaultGuard/
├── train_sentinel.py      # ML Model Training & Feature Engineering
├── sentinel.py            # Real-time AI Inference Engine
├── main.py                # Main Application Entry Point
├── requirements.txt       # Environment Dependencies
└── vault.db               # AES-256 Encrypted SQLite Vault
```
---

### 🖥 Installation & Initialization

<details>
<summary><b>1. Environment Setup (Click to Expand)</b></summary>

```bash
git clone https://github.com/ahmedxzarai/AI-VaultGuard.git
cd AI-VaultGuard
pip install -r requirements.txt
```
</details>
<details>
<summary><b>2. 📂 AI Sentinel Training (Required)</b></summary>

The dataset is hosted externally due to size constraints. Follow this protocol:

  1. Download Dataset: Obtain the [Malicious URLs Dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset) from Kaggle.
  2. Dataset Placement: Extract and place the CSV in the root directory. Rename it to urldata.csv.
  3. Execute Training: Run the training pipeline to generate the serialized model:
```bash
python train_sentinel.py
```
</details>
<details open>
<summary><b>3. Run Application</b></summary>

```bash
python main.py
```
</details>

---

### 🎯 Engineering Value
* **Applied ML:** Real-world application of Random Forest in a cybersecurity context.
* **Modular Design:** Separation of concerns between ML training, inference, and UI.
* **Cryptographic Rigor:** Implementation of industry-standard security protocols.

---

### 🚀 Future Roadmap
* [ ] Upgrade to Argon2id for password hashing.
* [ ] Implement memory-wiping for decrypted secrets.
* [ ] Develop a PyQt6 Modern Dashboard UI.

---

### 👤 Author
**AHMED ZARAI**<br>
*AI Systems & Biometric Intelligence Developer*<br><br><br>

<div align="center">
<p>Copyright © 2026 AHMED ZARAI. Distributed under the MIT License.</p>
</div>