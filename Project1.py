alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

# Caeser Cipher


def CaeserCipher(caeserPlaintext, caeserKeys):
    caeserCiphertext = ""
    caeserKey = int(caeserKeys)
    for i in range(len(caeserPlaintext)):
        char = caeserPlaintext[i]
        if char.isupper():
            caeserCiphertext += chr((ord(char) + caeserKey - 65) % 26 + 65)
        else:
            caeserCiphertext += chr((ord(char) + caeserKey - 97) % 26 + 97)
    return caeserCiphertext


# PlayFair Cipher
def convert(s):
    new = ""
    for x in s:
        new += x
    return new


def generatematrix(key):
    matrix = []
    for e in key.upper():
        if e not in matrix:
            matrix.append(e)

    for e in alphabet:
        if e not in matrix:
            matrix.append(e)

    # initialize a new list. Is there any elegant way to do that?
    matrix_group = []
    for e in range(5):
        matrix_group.append('')

    # Break it into 5*5
    matrix_group[0] = matrix[0:5]
    matrix_group[1] = matrix[5:10]
    matrix_group[2] = matrix[10:15]
    matrix_group[3] = matrix[15:20]
    matrix_group[4] = matrix[20:25]
    return matrix_group


def MapDiagraph(Plaintext):
    plain = []
    for char in Plaintext:
        if char == 'J':
            char = 'I'
        if char in alphabet:
            plain.append(char)
    for char in plain:
        if " " in plain:
            plain.remove(" ")
    i = 0
    for j in range(int(len(plain)/2)):
        if plain[i] == plain[i+1]:
            plain.insert(i+1, 'X')
        i = i+2
    if len(plain) % 2 == 1:
        plain.append("X")
    digraphed = []
    x = 0
    for t in range(1, int(len(plain)/2+1)):
        digraphed.append(plain[x:x+2])
        x = x+2
    return digraphed


def Letter_coordinates(key_matrix, character):
    x = y = 0
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == character:
                x = i
                y = j

    return x, y


def encrypt(message, key):
    message = MapDiagraph(message)
    key_matrix = generatematrix(key)
    cipher = []
    for e in message:
        p1, q1 = Letter_coordinates(key_matrix, e[0])
        p2, q2 = Letter_coordinates(key_matrix, e[1])
        if p1 == p2:
            if q1 == 4:
                q1 = -1
            if q2 == 4:
                q2 = -1
            cipher.append(key_matrix[p1][q1+1])
            cipher.append(key_matrix[p1][q2+1])
        elif q1 == q2:
            if p1 == 4:
                p1 = -1
            if p2 == 4:
                p2 = -1
            cipher.append(key_matrix[p1+1][q1])
            cipher.append(key_matrix[p2+1][q2])
        else:
            cipher.append(key_matrix[p1][q2])
            cipher.append(key_matrix[p2][q1])
    return cipher


L = []
file1 = open("caesar_out.txt", "w")
L.append("****** Key=3 *******")
L.append('\n')
for line in open('caesar_plain.txt'):
    if line[-1] == '\n':
        linemodified = CaeserCipher(line, 3)
        L.append(linemodified[:len(linemodified)-1])
        L.append('\n')
    else:
        L.append(CaeserCipher(line, 3))
        L.append('\n')
L.append('\n')
L.append("****** Key=6 *******")
L.append('\n')
for line in open('caesar_plain.txt'):
    if line[-1] == '\n':
        linemodified = CaeserCipher(line, 6)
        L.append(linemodified[:len(linemodified)-1])
        L.append('\n')
    else:
        L.append(CaeserCipher(line, 6))
        L.append('\n')
L.append('\n')
L.append("****** Key=12 *******")
L.append('\n')
for line in open('caesar_plain.txt'):
    if line[-1] == '\n':
        linemodified = CaeserCipher(line, 12)
        L.append(linemodified[:len(linemodified)-1])
        L.append('\n')
    else:
        L.append(CaeserCipher(line, 12))
        L.append('\n')
file1.writelines(L)
file1.close()
Key = input("Enter Key of playfair: ")
file2 = open("playfair_out.txt", "w")
t = []
for line in open('playfair_plain.txt'):
    t.append(convert(encrypt(line.upper(), Key)))
    t.append('\n')
file2.writelines(t)
file2.close
