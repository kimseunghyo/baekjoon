import sys
from collections import deque

def bfs(x, y):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        if x == goal_x and y == goal_y:
            return chess[goal_x][goal_y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and chess[nx][ny] == 0:
                q.append((nx, ny))
                chess[nx][ny] = chess[x][y] + 1


t = int(sys.stdin.readline())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, 2, 1, -1, -2]

for _ in range(t):
    l = int(sys.stdin.readline())
    x, y = list(map(int, sys.stdin.readline().split()))
    goal_x, goal_y = list(map(int, sys.stdin.readline().split()))

    chess = [[0 for _ in range(l)] for _ in range(l)]


    print(bfs(x, y))