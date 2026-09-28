def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

# Key generation
p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17  # chosen public exponent
d = mod_inverse(e, phi)

print("Public Key: (n =", n, ", e =", e, ")")
print("Private Key: (n =", n, ", d =", d, ")")

# Encryption
message = 65  # numeric representation of plaintext
cipher = pow(message, e, n)
print("Encrypted:", cipher)

# Decryption
decrypted = pow(cipher, d, n)
print("Decrypted:", decrypted)
