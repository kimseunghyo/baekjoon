import sys
from collections import deque

def bfs():
    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and tomato[nz][nx][ny] == 0:
                q.append((nz, nx, ny))
                tomato[nz][nx][ny] = tomato[z][x][y] + 1



m, n, h = list(map(int, sys.stdin.readline().split()))

tomato = []
q = deque([])

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(h):
    temp = []

    for j in range(n):
        temp.append(list(map(int, sys.stdin.readline().split())))

        for k in range(m):
            if temp[j][k] == 1:
                q.append([i, j, k])

    tomato.append(temp)

bfs()

result = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1)
                exit()
                
            if tomato[i][j][k] > result:
                result = tomato[i][j][k]

print(result - 1)