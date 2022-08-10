import sys
from collections import deque

def bfs(x, y):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))

    return maze[n - 1][m - 1]

n, m = list(map(int, sys.stdin.readline().split()))

maze = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))

print(bfs(0, 0))