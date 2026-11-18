key = "QWERTYUIOPASDFGHJKLZXCVBNM"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cipher = ""

for ch in text:
    if ch in alphabet:
        cipher += key[alphabet.index(ch)]
    else:
        cipher += ch

print("Encrypted message:", cipher)