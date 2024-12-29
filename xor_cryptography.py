# xor_cryptography.py

def xor_encrypt_decrypt(input_string, key):
    output = []
    for i in range(len(input_string)):
        xor_byte = chr(ord(input_string[i]) ^ ord(key[i % len(key)]))
        output.append(xor_byte)
    return ''.join(output)

