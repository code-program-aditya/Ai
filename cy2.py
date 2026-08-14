plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

text = input("Enter Plain Text: ").upper()
key = input("Enter Key: ").upper()

encrypted = ""
j = 0

for ch in text:
    if ch in plain:
        p = plain.index(ch)
        k = plain.index(key[j % len(key)])
        encrypted += plain[(p + k) % 26]
        j += 1
    else:
        encrypted += ch

print("Encrypted Text:", encrypted)

# decrypted

plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

text = input("Enter Cipher Text: ").upper()
key = input("Enter Key: ").upper()

decrypted = ""
j = 0

for ch in text:
    if ch in plain:
        c = plain.index(ch)
        k = plain.index(key[j % len(key)])
        decrypted += plain[(c - k) % 26]
        j += 1
    else:
        decrypted += ch

print("Decrypted Text:", decrypted)