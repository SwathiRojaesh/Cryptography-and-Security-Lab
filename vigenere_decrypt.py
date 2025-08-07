def vigenere_decrypt(cipher, key):
    cipher = cipher.upper().replace(" ", "")
    key = key.upper()
    key = (key * (len(cipher) // len(key) + 1))[:len(cipher)]
    plain = ""
    for c, k in zip(cipher, key):
        p = (ord(c) - ord(k) + 26) % 26
        plain += chr(p + 65)
    return plain

# --- Input
cipher = input("Enter ciphertext: ")
key = input("Enter key: ")
print("Decrypted:", vigenere_decrypt(cipher, key))
