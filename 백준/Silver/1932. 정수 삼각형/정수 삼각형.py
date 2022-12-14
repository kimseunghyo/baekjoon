n = int(input())

num = []

for _ in range(n):
    num.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            num[i][j] = num[i][j] + num[i - 1][j]
        elif j == i:
            num[i][j] = num[i][j] + num[i - 1][j - 1]
        else:
            num[i][j] = num[i][j] + max(num[i - 1][j - 1], num[i - 1][j])

print(max(num[n - 1]))