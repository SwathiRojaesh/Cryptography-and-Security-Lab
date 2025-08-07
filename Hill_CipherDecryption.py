import numpy as np
def modinv(a, m):
    for i in range(1, m):
        if (a*i)%m == 1:
            return i
    return None

def hill_decrypt(cipher, key):
    key_matrix = np.array(key).reshape(2,2)
    det = int(np.round(np.linalg.det(key_matrix))) % 26
    inv_det = modinv(det, 26)
    if inv_det is None:
        return "Inverse not possible!"

    adj = np.array([[key_matrix[1][1], -key_matrix[0][1]],
                    [-key_matrix[1][0], key_matrix[0][0]]]) % 26
    inv_matrix = (inv_det * adj) % 26
    plain = ""
    for i in range(0, len(cipher), 2):
        block = [ord(cipher[i])-65, ord(cipher[i+1])-65]
        res = np.dot(inv_matrix, block) % 26
        plain += chr(res[0]+65) + chr(res[1]+65)
    return plain

# --- Input
cipher = input("Enter ciphertext: ")
key = list(map(int, input("Enter 4 integers for 2x2 key matrix: ").split()))
print("Decrypted:", hill_decrypt(cipher, key))
