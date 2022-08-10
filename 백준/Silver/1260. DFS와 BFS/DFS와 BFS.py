import sys
from collections import deque

n, m, v = list(map(int, sys.stdin.readline().split()))

graph = [[0 for i in range(n + 1)] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    visited[v] = 1

    print(v, end=' ')

    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque([v])
    visited[v] = 0

    while q:
        v = q.popleft()

        print(v, end=' ')

        for i in range(1, n + 1):
            if visited[i] == 1 and graph[v][i] == 1:
                q.append(i)
                visited[i] = 0

dfs(v)
print()
bfs(v)