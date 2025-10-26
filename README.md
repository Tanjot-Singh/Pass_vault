# PassVault v2.0 – Secure CLI Password Manager

PassVault is a **command-line password manager** built in Python, designed to securely store, manage, and generate credentials. This project emphasizes **cybersecurity principles** like encryption, authentication, logging, and input validation, making it a practical tool for real-world use and a strong showcase for recruiters.

---

## 🔹 Features

### 1. Secure Password Storage
- Passwords are encrypted using **Fernet (AES symmetric encryption)** from the `cryptography` library.
- Encrypted passwords are saved in a local file `vault.pkl`.

### 2. Master Password Authentication
- Access to the vault is protected using a **SHA-256 hashed master password** stored in `master.hash`.
- Only users who provide the correct master password can access or modify the vault.

### 3. CRUD Operations
- Add, view, modify, and delete service credentials.
- Input validation ensures service names are **alphanumeric, underscores, or hyphens** with max 30 characters.

### 4. Strong Password Generator
- Generate cryptographically secure passwords using the `secrets` module.
- Option to include symbols and specify password length (min 12 characters).
- Auto-copy generated password to clipboard with `pyperclip`.

### 5. Secure Logging
- All actions (add, modify, delete) are logged using Python's `logging` module.
- **Passwords are never logged**, only metadata like service names and operations.

### 6. Rate-Limiting
- Limits failed master password attempts to 3.
- On failure, the program waits **10 seconds** before exiting to prevent brute-force attacks.

---

## 🔹 Tech Stack

- Python 3.12+
- Libraries:
  - `cryptography` – encryption & decryption
  - `pickle` – persistent storage
  - `getpass` – secure password input
  - `logging` – activity logs
  - `secrets` – secure password generation
  - `pyperclip` – clipboard copy
  - `re` – input validation

---

## 🔹 Installation

1. Clone the repo:
git clone <YOUR_REPO_LINK>

2. Install required libraries:
pip install cryptography pyperclip

3. Run the password manager:
python passmanager.py

🔹 Usage

1. First run: Set up your master password.
2. Subsequent runs: Enter your master password to unlock the vault.
3. Use the menu to:

->Add a new service and credentials

->View saved services and credentials

->Modify passwords

->Delete services

->Generate strong passwords


🔹 Security Highlights

->Passwords encrypted before saving.

->Master password hashed (SHA-256) for secure authentication.

->Rate-limiting prevents brute-force attacks.

->Input validation ensures only safe service names.

->Secure logging without storing sensitive data.

🔹Future Improvements

->Option for a GUI version.

->Multi-user support.

->Integration with cloud storage for encrypted vault backups.