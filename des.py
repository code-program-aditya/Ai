from Crypto.Cipher import DES

# Key must be 8 bytes (64 bits, but only 56 used)
key = b'8bytekey'
cipher = DES.new(key, DES.MODE_ECB)

message = b'HELLO123'   # Must be 8 bytes
encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)

print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
