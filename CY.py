def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()
    for char in key:
        if char not in used and char.isalpha():
            matrix.append(char)
            used.add(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j


def process_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    i = 0
    pairs = []

    while i < len(text):
        a = text[i]
        b = ''

        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2
        else:
            b = 'X'
            i += 1

        pairs.append((a, b))

    return pairs


def encrypt(matrix, pairs):
    result = ""

    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2: 
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]

        else: 
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result
key = "SECURITY"
text = "HELLO WORLD"

matrix = generate_matrix(key)
pairs = process_text(text)
cipher = encrypt(matrix, pairs)

print("Playfair Matrix:")
for row in matrix:
    print(row)

print("\nPairs:", pairs)
print("Cipher Text:", cipher)