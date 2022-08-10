from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    wear = []

    for _ in range(n):
        cloth, type = list(map(str, input().split()))

        wear.append(type)

    counter = Counter(wear)
    result = 1

    for c in counter:
        result *= counter[c] + 1

    print(result - 1)