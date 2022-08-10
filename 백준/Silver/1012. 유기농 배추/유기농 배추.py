import sys
from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    cnt = 0

    while q:
        x, y = q.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and field[nx][ny] == 1:
                q.append((nx, ny))
                field[nx][ny] += 1
                cnt += 1

    count.append(cnt)

t = int(sys.stdin.readline())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(t):
    m, n, k = list(map(int, sys.stdin.readline().split()))

    field = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[0 for _ in range(n)] for _ in range(m)]
    count = []

    for i in range(k):
        x, y = list(map(int, sys.stdin.readline().split()))
        field[x][y] = 1

    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0 and field[i][j] == 1:
                bfs(i, j)

    print(len(count))