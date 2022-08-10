n = int(input())

array = list(map(int, input().split()))
rev_array = array[::-1]

increase_dp = [1 for i in range(n)]
decrease_dp = [1 for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)
        if rev_array[i] > rev_array[j]:
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j] + 1)


decrease_dp = decrease_dp[::-1]
result = 0

for i in range(n):
    if result < increase_dp[i] + decrease_dp[i]:
        result = increase_dp[i] + decrease_dp[i]

print(result - 1)