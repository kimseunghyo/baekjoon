import sys
from collections import deque

def bfs(x, time):
    q = deque([(x, time)])
    visited = [0] * 100001

    while x <= 100000:
        for i in range(len(q)):
            x, time = q.popleft()

            if x == k:
                print(time)
                exit()

            nx = x - 1
            ntime = time + 1
            if 0 <= nx and visited[nx] == 0:
                q.append((nx, ntime))
                visited[nx] = 1

            nx = x + 1
            ntime = time + 1
            if nx <= 100000 and visited[nx] == 0:
                q.append((nx, ntime))
                visited[nx] = 1

            nx = 2 * x
            ntime = time + 1
            if nx <= 100000 and visited[nx] == 0:
                q.append((nx, ntime))
                visited[nx] = 1


n, k = list(map(int, sys.stdin.readline().split()))

bfs(n, 0)