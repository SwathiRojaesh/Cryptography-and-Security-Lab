def keyless_transposition_encrypt(text, cols):
    text = text.replace(" ", "").upper()
    rows = -(-len(text) // cols)
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    
    index = 0
    for r in range(rows):
        for c in range(cols):
            if index < len(text):
                grid[r][c] = text[index]
                index += 1

    cipher = ''
    for c in range(cols):
        for r in range(rows):
            cipher += grid[r][c]
    return cipher

# --- Input
text = input("Enter plaintext: ")
cols = int(input("Enter number of columns: "))
print("Encrypted:", keyless_transposition_encrypt(text, cols))
