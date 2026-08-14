def text_to_bin(text):
    return ''.join(format(ord(i), '08b') for i in text)

def bin_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

def xor(a, b):
    return ''.join('0' if i == j else '1' for i, j in zip(a, b))

def encrypt(plain_text, key):
    pt_bin = text_to_bin(plain_text)
    key_bin = text_to_bin(key)
    key_bin = (key_bin * (len(pt_bin)//len(key_bin) + 1))[:len(pt_bin)]
    cipher_bin = xor(pt_bin, key_bin)
    return cipher_bin

def decrypt(cipher_bin, key):
    key_bin = text_to_bin(key)
    key_bin = (key_bin * (len(cipher_bin)//len(key_bin) + 1))[:len(cipher_bin)]
    plain_bin = xor(cipher_bin, key_bin)
    return bin_to_text(plain_bin)

message = "HELLO"
key = "KEY"

print("Original:", message)
print("Key:", key)

encrypted = encrypt(message, key)
print("Encrypted (binary):", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)
