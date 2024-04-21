# Secure Messaging System using RSA Encryption

This Python script provides a secure messaging system using RSA encryption. It allows users to generate RSA key pairs, encrypt and decrypt messages, and exchange messages securely.

## Features

- **Key Pair Generation**: Users can generate RSA key pairs consisting of a public key and a private key.
- **Message Encryption and Decryption**: Messages can be encrypted using the recipient's public key and decrypted using the recipient's private key.
- **Message Saving and Reading**: Encrypted messages can be saved to files and decrypted messages can be read from files.
- **User Interaction**: The script provides a simple command-line interface for users to read and send messages.
- **Exception Handling**: Comprehensive error handling ensures smooth execution even in the presence of errors.

## Usage

1. **Generate Key Pair**:
   - Run the script and provide a username to generate an RSA key pair.
   - The generated keys will be stored in a folder named `{username}_folder` in the current directory.

2. **Read Messages**:
   - Enter 'read' when prompted to check for messages.
   - Encrypted messages will be read from the `read.txt` file in the user's folder, decrypted, and displayed.

3. **Send Messages**:
   - Enter 'send' when prompted to send a message.
   - Input the message to send when prompted.
   - The message will be encrypted using the recipient's public key and saved to a file named `send.txt` in the recipient's folder.

4. **Exit**:
   - Enter 'exit' to quit the program.

## Requirements

- Python 3.x
- `cryptography` library

## Installation

1. Clone this repository:
- `https://github.com/shehan774690541/end-to-endcription-python.git`
2. Install the required dependencies:
- `pip install cryptography`
3. Run the script:
- `Python user_n.py`  # user_n <- n for change your user name

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

[Dev_Shehan](https://github.com/shehan774690541)


