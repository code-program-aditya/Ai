def diffie_hellman(p, g, a, b):
    # Alice's public key
    A = pow(g, a, p)
    # Bob's public key
    B = pow(g, b, p)

    # Shared secret computed by Alice
    secret_alice = pow(B, a, p)
    # Shared secret computed by Bob
    secret_bob = pow(A, b, p)

    return A, B, secret_alice, secret_bob

# Example values
p = 23   # prime
g = 5    # primitive root
a = 6    # Alice's private key
b = 15   # Bob's private key

A, B, secret_alice, secret_bob = diffie_hellman(p, g, a, b)

print("Alice's Public Key:", A)
print("Bob's Public Key:", B)
print("Shared Secret (Alice):", secret_alice)
print("Shared Secret (Bob):", secret_bob)
