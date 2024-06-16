import math

def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp

# Function to compute modular exponentiation (a^b) % c efficiently
def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd, multiply base with result
            result = (result * base) % mod
        base = (base * base) % mod  # Square the base
        exp //= 2  # Divide exp by 2
    return result

# Function to find modular inverse of a under modulo m
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Convert text to numerical representation (A=0, B=1, ..., Z=25)
def text_to_numbers(text):
    numbers = []
    for char in text:
        if char.isalpha():
            number = ord(char.upper()) - ord('A')  # A=0, B=1, ..., Z=25
            numbers.append(number)
    return numbers

# Convert numerical representation back to text (0=A, 1=B, ..., 25=Z)
def numbers_to_text(numbers):
    text = ""
    for num in numbers:
        char = chr(num + ord('A'))  # 0 -> 'A', 1 -> 'B', ..., 25 -> 'Z'
        text += char
    return text

# Get input from user
p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))
text = input("Enter a message to encrypt: ")

# Calculate n, phi(n), and e
n = p * q
phi = (p - 1) * (q - 1)
e = 2

while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e += 1

# Calculate d, the modular inverse of e modulo phi
d = mod_inverse(e, phi)

# Display public and private keys
print("\nPublic Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# Convert text to numerical representation
plaintext_numbers = text_to_numbers(text)
print("\nPlaintext (numerical representation):", plaintext_numbers)

# Encryption: c = (msg ^ e) % n
ciphertext_numbers = [mod_exp(num, e, n) for num in plaintext_numbers]
print("Encrypted data (ciphertext):", ciphertext_numbers)

# Decryption: m = (c ^ d) % n
decrypted_numbers = [mod_exp(num, d, n) for num in ciphertext_numbers]
print("Decrypted Message (numerical representation):", decrypted_numbers)

# Convert numerical representation back to text
decrypted_text = numbers_to_text(decrypted_numbers)
print("Decrypted Message (text):", decrypted_text)

