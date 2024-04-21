import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def load_keys(username):
    try:
        with open(f'{username}_keys.json', 'r') as file:
            keys = json.load(file)
            return keys["public_key"], keys["private_key"]
    except FileNotFoundError:
        return None, None

def encrypt_message(message, public_key):
    public_key = serialization.load_pem_public_key(
        public_key.encode(),
        backend=default_backend()
    )
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

def decrypt_message(encrypted_message, private_key):
    private_key = serialization.load_pem_private_key(
        private_key.encode(),
        password=None,
        backend=default_backend()
    )
    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()

def main():
    username = "User-B"
    public_key, private_key = load_keys(username)
    if not public_key or not private_key:
        print("No keys found. Exiting...")
        return
    
    while True:
        action = input("Enter 'read' to check for messages or 'send' to send a message (type 'exit' to quit): ").lower()
        
        if action == 'read':
            # Check for incoming messages
            # Decrypt and print the message
            pass
        elif action == 'send':
            message = input("Enter the message to send: ")
            encrypted_message = encrypt_message(message, public_key)
            print(f"Encrypted message: {encrypted_message}")
            # Send encrypted_message to User-A
        elif action == 'exit':
            print("Exiting...")
            break
        else:
            print("Invalid action. Please enter 'read', 'send', or 'exit'.")

if __name__ == "__main__":
    main()
