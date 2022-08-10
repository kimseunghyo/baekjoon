from collections import deque

n, k = list(map(int, input().split()))
queue = deque([i for i in range(1, n + 1)])
array = []
x = 0

while queue:
    x += k - 1

    if x >= len(queue):
        x %= len(queue)

    array.append(queue[x])
    queue.remove(queue[x])

print('<%d' %array[0], end='')

for i in range(1, n):
    print(', %d' %array[i], end='')

print('>')