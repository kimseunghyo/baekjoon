from collections import deque

n, m = list(map(int, input().split()))
position = deque(list(map(int, input().split())))

q = deque([i for i in range(1, n + 1)])

cnt = 0

while m != 0:
    if q[0] == position[0]:
        q.popleft()
        position.popleft()
        m -= 1

    else:
        move2 = abs(-q.index(position[0]))
        move3 = len(q) - q.index(position[0])

        if move2 <= move3:
            for i in range(move2):
                q.append(q[0])
                q.popleft()
                cnt += 1
        else:
            for i in range(move3):
                q.appendleft(q[-1])
                q.pop()
                cnt += 1

print(cnt)