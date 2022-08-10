import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

left = 1
right = k
result = 0

while left <= right:
    middle = (left + right) // 2
    total = 0

    for i in range(1, n + 1):
        x = middle // i

        if x > n:
            x = n

        total += x

    if total >= k:
        right = middle - 1
        result = middle
    else:
        left = middle + 1

print(result)