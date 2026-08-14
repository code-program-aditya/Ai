def strassen_matrix_mult(A, B):
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
    e, f, g, h = B[0][0], B[0][1], B[1][0], B[1][1]
    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)
    C11 = p5 + p4 - p2 + p6
    C12 = p1 + p2
    C21 = p3 + p4
    C22 = p1 + p5 - p3 - p7
    return [[C11, C12], [C21, C22]]
def standard_matrix_mult(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result
print("Enter elements of first 2x2 matrix (row-wise):")
A = [list(map(int, input().split())) for _ in range(2)]
print("Enter elements of second 2x2 matrix (row-wise):")
B = [list(map(int, input().split())) for _ in range(2)]
strassen_result = strassen_matrix_mult(A, B)
standard_result = standard_matrix_mult(A, B)
print("\nMatrix A:", A)
print("Matrix B:", B)
print("\nResult using Strassen’s Algorithm:", strassen_result)
print("Result using Standard Multiplication:", standard_result)