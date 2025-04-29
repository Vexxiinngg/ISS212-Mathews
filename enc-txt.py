'''
Jmoody
ISS 212
4.2025 Wk 12 Tool Development 8 - enc-txt.py
NOTE: REMEMBER TO SAVE AES KEY IN **TXT** FILE TO USE FOR DECRYPTION!
'''

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#The function to generate a random AES key of a given size
def generate_aes_key(key_size):
    #Converts bits to bytes
    return get_random_bytes(key_size // 8)

#The function to encrypt a file using AES
def encrypt_file_aes(file_path, key):
    #Creates a new AES cypher using EAX mode
    cipher = AES.new(key, AES.MODE_EAX)
    #Reads the contents of the file in binary
    with open(file_path, 'rb') as file:
        plaintext = file.read()

        #Encrpyts the data
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    #Write encrypted data to new file with enc ext.
    with open(file_path + '.enc', 'wb') as encrypted_file:
        #Stores nonce, tag and cipher text
        encrypted_file.write(cipher.nonce)
        encrypted_file.write(tag)
        encrypted_file.write(ciphertext)

# Example usage
if __name__ == "__main__":
    aes_key = generate_aes_key(256)

    #Asks user for file to encrypt
    file_to_encrypt = input("Enter the name of the file to encrypt: ")
    #Calls function
    encrypt_file_aes(file_to_encrypt, aes_key)
    # Informs user file has been encrypted
    print(f'File "{file_to_encrypt}" encrypted.')

    #Prints in hexadecimal format
    print(f'AES Key (Hex): {aes_key.hex()}')