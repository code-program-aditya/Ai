from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Key must be 16, 24, or 32 bytes long
key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_ECB)

message = b'HELLO WORLD!!!'   # Must be padded to block size
encrypted = cipher.encrypt(pad(message, AES.block_size))
decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)

print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
