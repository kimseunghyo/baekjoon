import sys

k, n = list(map(int, sys.stdin.readline().split()))

line = [int(sys.stdin.readline()) for _ in range(k)]

left = 1
right = max(line)
result = 0

while left <= right:
    middle = (left + right) // 2
    total = 0

    for l in line:
        total += l // middle

    if total >= n:
        left = middle + 1
        result = middle
    else:
        right = middle - 1

print(result)