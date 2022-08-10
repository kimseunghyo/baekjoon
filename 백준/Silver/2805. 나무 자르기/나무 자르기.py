import sys

n, m = list(map(int, sys.stdin.readline().split()))
tree = list(map(int, sys.stdin.readline().split()))

left = 1
right = max(tree)

result = 0

while left <= right:
    middle = (left + right) // 2
    total = 0

    for t in tree:
        if t > middle:
            total += t - middle

    if total >= m:
        left = middle + 1
        result = middle
    else:
        right = middle - 1

print(result)