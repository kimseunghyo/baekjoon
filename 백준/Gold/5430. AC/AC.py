from collections import deque
import sys

t = int(input())

for _ in range(t):
    p = sys.stdin.readline()
    n = int(input())

    q = deque(sys.stdin.readline().strip()[1:-1].split(','))

    if n == 0:
        q = deque([])

    temp = True
    r = 0

    for x in p:
        if x == 'R':
            r += 1

        elif x == 'D':
            if not q:
                print('error')
                temp = False
                break

            else:
                if r % 2 == 0:
                    q.popleft()
                else:
                    q.pop()


    if temp == True:
        if r % 2 == 0:
            print('[' + ','.join(q) + ']')
        else:
            q.reverse()
            print('[' + ','.join(q) + ']')