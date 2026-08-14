plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"   # key (you can change)
def encrypt(text):
    result = ""
    for char in text.upper():
        if char in plain:
            index = plain.index(char)
            result += cipher[index]
        else:
            result += char
    return result
def decrypt(text):
    result = ""
    for char in text.upper():
        if char in cipher:
            index = cipher.index(char)
            result += plain[index]
        else:
            result += char
    return result
message = "HELLO"
encrypted = encrypt(message)
decrypted = decrypt(encrypted)
print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)