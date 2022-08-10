import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

memo = [0]

for i in range(n):
    if memo[-1] < a[i]:
        memo.append(a[i])
    else:
        left = 0
        right = len(memo)

        while left < right:
            middle = (left + right) // 2

            if memo[middle] < a[i]:
                left = middle + 1
            else:
                right = middle

        memo[right] = a[i]

print(len(memo) - 1)
