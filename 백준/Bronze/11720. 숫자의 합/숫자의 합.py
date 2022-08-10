n = int(input())
nums = list(map(int, input()))
n_sum = 0

for i in range(n):
    n_sum += int(nums[i])

print(n_sum)