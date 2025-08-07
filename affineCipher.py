def mod_inverse(a, m):
    """Find modular inverse of a under modulo m"""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Inverse doesn't exist. 'a' must be coprime with 26.")

def encrypt(text, a, b):
    """Encrypts the plaintext using the Affine Cipher"""
    result = ''
    for char in text.upper():
        if char.isalpha():
            x = ord(char) - ord('A')
            encrypted = (a * x + b) % 26
            result += chr(encrypted + ord('A'))
        else:
            result += char
    return result

def decrypt(cipher, a, b):
    """Decrypts the ciphertext using the Affine Cipher"""
    a_inv = mod_inverse(a, 26)
    result = ''
    for char in cipher:
        if char.isalpha():
            y = ord(char) - ord('A')
            decrypted = (a_inv * (y - b + 26)) % 26
            result += chr(decrypted + ord('A'))
        else:
            result += char
    return result

# Example usage
if __name__ == "__main__":
    plaintext = "AFFINE CIPHER"
    a, b = 5, 8  # a must be coprime with 26

    encrypted_text = encrypt(plaintext, a, b)
    decrypted_text = decrypt(encrypted_text, a, b)

    print("Plaintext :", plaintext)
    print("Encrypted :", encrypted_text)
    print("Decrypted :", decrypted_text)
