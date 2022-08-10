import heapq
import sys

n = int(sys.stdin.readline())
max_hq = []
min_hq = []
num = []

for i in range(n):
    x = int(sys.stdin.readline())

    if len(max_hq) == len(min_hq):
        heapq.heappush(max_hq, (-x, x))
    else:
        heapq.heappush(min_hq, (x, x))

    if min_hq and max_hq[0][1] > min_hq[0][1]:
        heapq.heappush(max_hq, (-min_hq[0][1], heapq.heappop(min_hq)[1]))
        heapq.heappush(min_hq, (max_hq[0][1], heapq.heappop(max_hq)[1]))

    num.append(max_hq[0][1])

for n in num:
    print(n)