# Fibonacci using Dynamic Programming
def fib(n):
    d = [0] * (n + 2)
    d[1] = 1

    for i in range(2, n + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[n]


# Longest Common Subsequence
def lcs(a, b):
    d = [
        [0] * (len(b) + 1)
        for _ in range(len(a) + 1)
    ]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):

            if a[i - 1] == b[j - 1]:
                d[i][j] = d[i - 1][j - 1] + 1
            else:
                d[i][j] = max(
                    d[i - 1][j],
                    d[i][j - 1]
                )

    return d[-1][-1]


# N-Queens using Backtracking
def queens(n):
    col = [-1] * n

    def place(r):
        if r == n:
            return True

        for c in range(n):

            if all(
                col[i] != c and
                abs(col[i] - c) != r - i
                for i in range(r)
            ):
                col[r] = c

                if place(r + 1):
                    return True

        return False

    place(0)
    return col


# Subset Sum using Backtracking
def subset(a, target, i=0):

    if target == 0:
        return True

    if i == len(a) or target < 0:
        return False

    return (
        subset(a, target - a[i], i + 1)
        or
        subset(a, target, i + 1)
    )


# Execute programs
print("Fib(10):", fib(10))

print(
    "LCS length:",
    lcs("FORENSIC", "SCIENCE")
)

print(
    "4-Queens columns:",
    *queens(4)
)

print(
    "Subset 9:",
    subset([3, 34, 4, 12, 5, 2], 9)
)