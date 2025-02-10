# xor_cryptography.py

def xor_encrypt_decrypt(input_string, key):
    output = []
    for i in range(len(input_string)):
        xor_byte = chr(ord(input_string[i]) ^ ord(key[i % len(key)]))
        output.append(xor_byte)
    return ''.join(output)

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")
    ciphertext = xor_encrypt_decrypt(plaintext, key)
    print(f"Ciphertext: {ciphertext}")
    decrypted_text = xor_encrypt_decrypt(ciphertext, key)
    print(f"Decrypted Text: {decrypted_text}")
