from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
f = Fernet(key)

# Encrypt a message
message = b"MySecretPassword123"
token = f.encrypt(message)
print("Encrypted:", token )

# Decrypt it back
decrypted = f.decrypt(token)
print("Decrypted:", decrypted.decode())
