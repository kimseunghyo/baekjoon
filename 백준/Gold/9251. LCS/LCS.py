letter1 = '0' + input()
letter2 = '0' + input()

dp = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(1, len(letter1)):
    for j in range(1, len(letter2)):
        if letter1[i] == letter2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


print(max(max(dp)))