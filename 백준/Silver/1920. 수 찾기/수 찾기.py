import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

a.sort()

for b in B:
    start = 0
    end = n - 1
    middle = (end + start) // 2
    temp = False

    while end - start >= 0:
        if b == a[middle]:
            temp = True
            break

        elif b < a[middle]:
            end = middle - 1

        else:
            start = middle + 1

        middle = (end + start) // 2

    if temp:
        print(1)
    else:
        print(0)