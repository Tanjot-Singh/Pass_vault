#passstore.py
import os
import pickle

from cryptography.fernet import Fernet



VAULT_FILE = "vault.pkl"
KEY_FILE = "key.key"




with open(KEY_FILE,"rb") as kf :
   key = kf.read()
   fernet = Fernet(key)

def encrypt_password(password):
    if isinstance(password, bytes):  # already encrypted
        return password
    return fernet.encrypt(password.encode())


def decrypt_password(token):
      return fernet.decrypt(token).decode()

   

def load_vault():
    if os.path.exists(VAULT_FILE):
        with open(VAULT_FILE,'rb') as file :
            vault = pickle.load(file)
        for service in vault :
            vault[service]['pass'] = decrypt_password( vault[service]['pass'])
            return vault 
    return{}    

def save_vault(vault):
    vault_to_save = {}
    for service , creds in vault.items():
        vault_to_save[service] = {
            "user" : creds["user"] ,
            "pass" : encrypt_password(creds["pass"])
        }

    with open(VAULT_FILE,'wb') as file :
     pickle.dump(vault_to_save,file)
     print("Vault saved successfully.")

