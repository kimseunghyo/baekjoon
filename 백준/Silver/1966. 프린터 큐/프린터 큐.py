from collections import deque

t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    q = deque(list(map(int, input().split())))
    index = deque([i for i in range(n)])

    cnt = 0

    while q:
        if q[0] == max(q):
            cnt += 1

            if index[0] == m:
                break

            q.popleft()
            index.popleft()

        else:
            q.append(q[0])
            q.popleft()

            index.append(index[0])
            index.popleft()

    print(cnt)