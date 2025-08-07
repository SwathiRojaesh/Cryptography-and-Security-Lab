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

def playfair_encrypt(text, key):
    text = text.upper().replace('J', 'I').replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    matrix = generate_matrix(key)
    cipher = ""
    for a, b in pairs:
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)
        if r1 == r2:
            cipher += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            cipher += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            cipher += matrix[r1][c2] + matrix[r2][c1]
    return cipher

# --- Input
text = input("Enter plaintext: ")
key = input("Enter key: ")
print("Encrypted:", playfair_encrypt(text, key))
