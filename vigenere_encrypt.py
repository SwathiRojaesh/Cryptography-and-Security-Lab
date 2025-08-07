def vigenere_encrypt(text, key):
    text = text.upper().replace(" ", "")
    key = key.upper()
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    cipher = ""
    for t, k in zip(text, key):
        c = (ord(t) + ord(k) - 2*65) % 26
        cipher += chr(c + 65)
    return cipher

# --- Input
text = input("Enter plaintext: ")
key = input("Enter key: ")
print("Encrypted:", vigenere_encrypt(text, key))
