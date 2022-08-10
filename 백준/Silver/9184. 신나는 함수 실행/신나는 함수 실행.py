memo = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]


def recursive(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return recursive(20, 20, 20)

    if memo[a][b][c] != 0:
        return memo[a][b][c]

    if a < b < c:
        memo[a][b][c] = recursive(a, b, c - 1) + recursive(a, b - 1, c - 1) - recursive(a, b - 1, c)
        return memo[a][b][c]

    memo[a][b][c] = recursive(a - 1, b, c) + recursive(a - 1, b - 1, c) \
        + recursive(a - 1, b, c - 1) - recursive(a - 1, b - 1, c - 1)

    return memo[a][b][c]


while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    print("w(%d, %d, %d)" % (a, b, c), "=", recursive(a, b, c))
