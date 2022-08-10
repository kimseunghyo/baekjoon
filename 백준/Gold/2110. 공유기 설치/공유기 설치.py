import sys

n, c = list(map(int, sys.stdin.readline().split()))
house = [int(sys.stdin.readline()) for _ in range(n)]

house.sort()

min = 1
max = house[n - 1] - house[0]

result = 0

while min <= max:
    middle = (min + max) // 2
    distance = 0
    start = house[0]
    total = 1

    for i in range(1, n):
        distance = house[i] - start
        if distance >= middle:
            total += 1
            start = house[i]

    if total >= c:
        min = middle + 1
        result = middle
    else:
        max = middle - 1


print(result)