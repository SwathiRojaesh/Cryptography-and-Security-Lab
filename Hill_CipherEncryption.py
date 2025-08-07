import numpy as np

def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'
    key_matrix = np.array(key).reshape(2,2)
    cipher = ""
    for i in range(0, len(text), 2):
        block = [ord(text[i])-65, ord(text[i+1])-65]
        res = np.dot(key_matrix, block) % 26
        cipher += chr(res[0]+65) + chr(res[1]+65)
    return cipher

# --- Input
text = input("Enter plaintext: ")
key = list(map(int, input("Enter 4 integers for 2x2 key matrix: ").split()))
print("Encrypted:", hill_encrypt(text, key))
