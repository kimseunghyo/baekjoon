from collections import deque
import sys

n = int(input())
q = deque()

for _ in range(n):
    command = list(map(str, sys.stdin.readline().split()))

    if command[0] == 'push_front':
        q.appendleft(command[1])
    
    if command[0] == 'push_back':
        q.append(command[1])
    
    if command[0] == 'pop_front':
        if not q:
            print(-1)
        else:
            print(q[0])
            q.popleft()
    
    if command[0] == 'pop_back':
        if not q:
            print(-1)
        else:
            print(q[-1])
            q.pop()
    
    if command[0] == 'size':
        print(len(q))
    
    if command[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    
    if command[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    
    if command[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])