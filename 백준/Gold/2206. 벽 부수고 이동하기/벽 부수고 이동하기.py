import sys
from collections import deque

def bfs(x, y, cnt):
    q = deque([(x, y, cnt)])
    visited[x][y][cnt] = 1

    while q:
        x, y, cnt = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][cnt]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and cnt == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))

                elif graph[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    q.append((nx, ny, cnt))

    return -1


n, m = list(map(int, sys.stdin.readline().split()))

graph = []
visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

print(bfs(0, 0, 0))