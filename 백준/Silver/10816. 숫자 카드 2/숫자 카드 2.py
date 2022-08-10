import sys
from collections import Counter

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

count = Counter(a)

a.sort()
result = []

for i in range(m):
    cnt = count.get(b[i])

    if not cnt:
        cnt = 0
    result.append(cnt)

print(*result)