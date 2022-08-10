import sys
from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    cnt = 1

    while q:
        x, y = q.popleft()

        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and house[nx][ny] == 1:
                q.append((nx, ny))
                house[nx][ny] += 1
                cnt += 1

    count.append(cnt)

n = int(sys.stdin.readline())

visited = [[0 for _ in range(n)] for _ in range(n)]
house = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count = []

for _ in range(n):
    house.append(list(map(int, sys.stdin.readline().rstrip())))

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and house[i][j] == 1:
            bfs(i, j)

print(len(count))
count.sort()

for c in count:
    print(c)