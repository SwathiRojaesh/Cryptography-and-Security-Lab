def keyless_transposition_decrypt(cipher, cols):
    cipher = cipher.replace(" ", "").upper()
    rows = -(-len(cipher) // cols)
    grid = [['' for _ in range(cols)] for _ in range(rows)]

    index = 0
    for c in range(cols):
        for r in range(rows):
            if index < len(cipher):
                grid[r][c] = cipher[index]
                index += 1

    plain = ''
    for r in range(rows):
        for c in range(cols):
            plain += grid[r][c]
    return plain

# --- Input
cipher = input("Enter ciphertext: ")
cols = int(input("Enter number of columns: "))
print("Decrypted:", keyless_transposition_decrypt(cipher, cols))
