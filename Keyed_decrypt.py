def keyed_transposition_decrypt(cipher, key):
    key = key.upper()
    col = len(key)
    row = -(-len(cipher) // col)
    order = sorted(list(enumerate(key)), key=lambda x: x[1])

    grid = [['' for _ in range(col)] for _ in range(row)]
    index = 0
    for i, _ in order:
        for r in range(row):
            if index < len(cipher):
                grid[r][i] = cipher[index]
                index += 1

    plain = ''
    for r in range(row):
        for c in range(col):
            plain += grid[r][c]
    return plain.strip()

# --- Input
cipher = input("Enter ciphertext: ")
key = input("Enter keyword: ")
print("Decrypted:", keyed_transposition_decrypt(cipher, key))
