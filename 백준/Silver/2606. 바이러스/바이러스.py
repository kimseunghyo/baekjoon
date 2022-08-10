import sys
from collections import deque

n = int(sys.stdin.readline())
connect_n = int(sys.stdin.readline())

graph = [[0 for i in range(n + 1)] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(connect_n):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a][b] = graph[b][a] = 1

def bfs(v):
    q = deque([v])
    visited[v] = 1
    cnt = 0

    while q:
        v = q.popleft()

        for i in range(1, n + 1):
            if visited[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited[i] = 1
                cnt += 1
    print(cnt)

bfs(1)