n = int(input())

juice = [0] * 10001
dp = [0] * 10001

for i in range(1, n + 1):
    juice[i] = int(input())

dp[1] = juice[1]
dp[2] = dp[1] + juice[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + juice[i], dp[i - 3] + juice[i - 1] + juice[i])

print(dp[n])