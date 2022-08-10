from collections import deque

n = int(input())
queue = deque([i for i in range(1, n + 1)])

while True:
    if len(queue) == 1:
        print(queue[0])

        break

    queue.popleft()
    queue.append(queue[0])
    queue.popleft()