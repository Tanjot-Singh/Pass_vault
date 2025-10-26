# masterauth.py
import hashlib
import os
import getpass
import time

HASH_FILE = "master.hash"

def hash_password(password):
    """Generate SHA-256 hash for the given password"""
    return hashlib.sha256(password.encode()).hexdigest()

def setup_master_password():
    """Run once — creates a new master password"""
    print("\n--- Master Password Setup ---")
    pwd = getpass.getpass("Create master password: ")
    confirm = getpass.getpass("Confirm master password: ")

    if pwd != confirm:
        print("Passwords do not match. Try again.")
        return setup_master_password()

    with open(HASH_FILE, "w") as f:
        f.write(hash_password(pwd))
    print("Master password set successfully!")

def verify_master():
    """Verify the entered master password against the stored hash with lockout"""
    if not os.path.exists(HASH_FILE):
        setup_master_password()
        return True  # skip verification first time

    with open(HASH_FILE, "r") as f:
        stored_hash = f.read().strip()

    attempts = 0
    while attempts < 3:
        pwd = getpass.getpass("Enter master password: ")
        if hash_password(pwd) == stored_hash:
            print("Access granted.")
            return True
        else:
            attempts += 1
            print(f"Incorrect password. {3 - attempts} attempts left.")

    # Lockout
    print("Too many failed attempts. Waiting 10 seconds...")
    time.sleep(10)
    print("Exiting...")
    return False
