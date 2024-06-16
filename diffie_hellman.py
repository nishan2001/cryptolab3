from math import gcd


def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

def diffie_hellman():
    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter a base (g) smaller than p: "))

    a = int(input("Enter Alice's private key (a): "))
    b = int(input("Enter Bob's private key (b): "))

    A = mod_exp(g, a, p)  # Public key for Alice
    B = mod_exp(g, b, p)  # Public key for Bob
    secret_key_A = mod_exp(B, a, p)  # Alice computes the shared secret key
    secret_key_B = mod_exp(A, b, p)  # Bob computes the shared secret key

    # Both should have the same shared secret key
    if secret_key_A == secret_key_B:
        print(f"Shared secret key: {secret_key_A}")
    else:
        print("Error: Shared secret keys do not match.")
diffie_hellman()
