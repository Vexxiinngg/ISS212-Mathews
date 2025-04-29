'''
Jmoody
ISS 212
4.2025 Wk 12 Tool Development 8 - de-txt.py
NOTE: USE AES KEY IN **TXT** FILE TO DECRYPT FILE: sup3rs3cr37.txt.enc
'''

from Crypto.Cipher import AES

#The function to decrypt a file that was encrypted using AES
def decrypt_file_aes(encrypted_file_path, key):
    #Opens the encrypted file in binary mode
    with open(encrypted_file_path, 'rb') as encrypted_file:
        #Reads the first 16 bytes the nonce
        nonce = encrypted_file.read(16)
        #Reads next 16 bytes the tag
        tag = encrypted_file.read(16)
        #Reads rest of encrypted content
        ciphertext = encrypted_file.read()

    #Creates new AES cypher
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    #Decrypts and verifies the cyphertext using the tag
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    #Writes decrypted content to new file
    with open(encrypted_file_path[:-4] + '_decrypted.txt', 'wb') as decrypted_file:
        decrypted_file.write(plaintext)


if __name__ == "__main__":
    #Prompts user to enter AES key
    aes_key = bytes.fromhex(input("Enter the AES key (hexadecimal format): "))

    #Prompts user to enter filename
    file_to_decrypt = input("Enter the name of the file to decrypt: ")
    #Calls decryption function
    decrypt_file_aes(file_to_decrypt, aes_key)
    #Notifies user when it is decrypted
    print(f'File "{file_to_decrypt}" decrypted.')
