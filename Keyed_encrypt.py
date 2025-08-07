def keyed_transposition_encrypt(text, key):
    text = text.replace(" ", "").upper()
    key = key.upper()
    col = len(key)
    row = -(-len(text) // col)  # ceiling division

    grid = [['' for _ in range(col)] for _ in range(row)]
    index = 0
    for r in range(row):
        for c in range(col):
            if index < len(text):
                grid[r][c] = text[index]
                index += 1

    order = sorted(list(enumerate(key)), key=lambda x: x[1])
    cipher = ''
    for i, _ in order:
        for r in range(row):
            cipher += grid[r][i]
    return cipher

# --- Input
text = input("Enter plaintext: ")
key = input("Enter keyword: ")
print("Encrypted:", keyed_transposition_encrypt(text, key))
