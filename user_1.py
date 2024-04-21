import os
import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def generate_key_pair(username):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    user_folder = f"{username}_folder"
    try:
        os.makedirs(user_folder, exist_ok=True)  # Create folder if not exists
        with open(os.path.join(user_folder, f'{username}_keys.json'), 'w') as file:
            json.dump({
                "username": username,
                "public_key": public_key_pem.decode(),
                "private_key": private_key_pem.decode()
            }, file)
    except Exception as e:
        print(f"Error occurred while generating keys: {e}")

def load_keys(username):
    user_folder = f"{username}_folder"
    try:
        with open(os.path.join(user_folder, f'{username}_keys.json'), 'r') as file:
            keys = json.load(file)
            return keys["public_key"], keys["private_key"]
    except FileNotFoundError:
        return None, None
    except Exception as e:
        print(f"Error occurred while loading keys: {e}")
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
    return decrypted

def save_message(username, message, filename):
    user_folder = f"{username}_folder"
    try:
        with open(os.path.join(user_folder, filename), 'wb') as file:  # Open file in binary mode
            file.write(message)  # Write bytes directly
    except Exception as e:
        print(f"Error occurred while saving message: {e}")

def main():
    username = "User-A"
    generate_key_pair(username)
    public_key, private_key = load_keys(username)
    
    while True:
        action = input("Enter 'read' to check for messages or 'send' to send a message (type 'exit' to quit): ").lower()
        
        if action == 'read':
            try:
                user_folder = f"{username}_folder"
                with open(os.path.join(user_folder, 'read.txt'), 'rb') as file:  # Open file in binary mode
                    encrypted_message = file.read()  # Read bytes directly
                decrypted_message = decrypt_message(encrypted_message, private_key)
                print("Decrypted message:", decrypted_message.decode())  # Decode bytes to string
            except Exception as e:
                print(f"Error occurred while reading message: {e}")
        elif action == 'send':
            try:
                message = input("Enter the message to send: ")
                encrypted_message = encrypt_message(message, public_key)
                save_message(username, encrypted_message, 'send.txt')
                print("Encryption successful. Message sent.")
            except Exception as e:
                print(f"Error occurred while sending message: {e}")
        elif action == 'exit':
            print("Exiting...")
            break
        else:
            print("Invalid action. Please enter 'read', 'send', or 'exit'.")

if __name__ == "__main__":
    main()
