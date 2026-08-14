import sys
def matrix_chain_order(p):
    n = len(p) - 1  
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < dp[i][j]:
                    dp[i][j] = q
                    s[i][j] = k
    return dp, s
def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")
p = list(map(int, input("Enter dimensions array : ").split()))
dp, s = matrix_chain_order(p)
n = len(p) - 1
print("\n--- Matrix Chain Multiplication Process ---")
print("Minimum number of multiplications:", dp[1][n])
print("Optimal Parenthesization: ", end="")
print_optimal_parens(s, 1, n)
print()