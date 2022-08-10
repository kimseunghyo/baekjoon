import sys
from collections import deque

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                q.append((nx, ny))
                tomato[nx][ny] = tomato[x][y] + 1


m, n = list(map(int, sys.stdin.readline().split()))

tomato = []
q = deque([])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split())))

    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])

bfs()

result = 0

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit(0)
        else:
            if tomato[i][j] > result:
                result = tomato[i][j]

print(result - 1)