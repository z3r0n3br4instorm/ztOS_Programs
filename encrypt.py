import os
from cryptography.fernet import Fernet
def is_encrypted(file_path):
    # Get the file extension
    _, extension = os.path.splitext(file_path)

    # List of encrypted file extensions
    encrypted_extensions = ['.enc', '.crypt', '.locked']  # Add your encrypted file extensions here

    # Check if the file extension matches any encrypted extension
    return extension in encrypted_extensions
def encrypt_folder(folder_path, key):
    # Generate a cipher using the provided key
    print("Initializing Encryption..")
    cipher = Fernet(key)

    # Iterate over all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Check if the file was already encrypted
            if is_encrypted(file_path):
                print(f"Skipping encryption for file: {file_path}")
                continue
            
            # Print the file name that is currently being encrypted
            print(f"Encrypting file: {file_path}")
            
            # Read the contents of the file
            with open(file_path, 'rb') as f:
                plaintext = f.read()
            
            # Encrypt the contents
            ciphertext = cipher.encrypt(plaintext)
            with open(file_path, 'wb') as f:
                f.write(ciphertext)




def generate_key():
    get_input = Fernet.generate_key()
    print("Cypher :"+str(get_input))
    return get_input
# Example usage
if __name__ == "__main__":
    print("z t O S - Upsilon")
    print("Zerone Laboratories //SysLock encryption v1.3")
    folder_path = '/home/zerone/Personal_stuff/'
    encryption_key = generate_key()
    encrypt_folder(folder_path, encryption_key)
    print("Program Complete...")