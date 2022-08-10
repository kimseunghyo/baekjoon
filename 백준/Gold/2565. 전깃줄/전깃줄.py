n = int(input())

dp = [1] * (n + 1)
lope = []

for _ in range(n):
    lope.append(list(map(int, input().split())))

lope.sort()

for i in range(n):
    for j in range(i):
        if lope[i][1] > lope[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))