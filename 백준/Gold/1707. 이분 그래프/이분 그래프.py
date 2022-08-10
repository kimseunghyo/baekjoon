import sys
from collections import deque

sys.setrecursionlimit(1000000)

def dfs(start, group):
    visited[start] = group

    for i in graph[start]:
        if not visited[i]:
            a = dfs(i, -group)
            if not a:
                return False
        elif visited[i] == visited[start]:
            return False

    return True


K = int(sys.stdin.readline())

for _ in range(K):
    V, E = list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)

    for _ in range(E):
        u, v = list(map(int, sys.stdin.readline().split()))
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V + 1):
        if not visited[i]:
            result = dfs(i, 1)
            if not result:
                break

    print("YES" if result else "NO")