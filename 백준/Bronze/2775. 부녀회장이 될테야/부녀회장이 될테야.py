t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

    room = [x for x in range(1, n + 1)]

    for kn in range(k):
        for nn in range(1, n):
            room[nn] += room[nn - 1]

    print(room[-1])