def generate_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    used = set()
    for char in key:
        if char not in used and char.isalpha():
            matrix.append(char)
            used.add(char)
    for i in range(65, 91):
        if chr(i) not in used and chr(i) != 'J':
            matrix.append(chr(i))
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
            
# Same matrix and find_pos functions used

def playfair_decrypt(cipher, key):
    cipher = cipher.upper().replace('J', 'I')
    matrix = generate_matrix(key)
    pairs = [cipher[i:i+2] for i in range(0, len(cipher), 2)]
    plaintext = ""
    for a, b in pairs:
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)
        if r1 == r2:
            plaintext += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            plaintext += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            plaintext += matrix[r1][c2] + matrix[r2][c1]
    return plaintext

# --- Input
cipher = input("Enter ciphertext: ")
key = input("Enter key: ")
print("Decrypted:", playfair_decrypt(cipher, key))
