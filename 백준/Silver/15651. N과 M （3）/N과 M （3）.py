n, m = map(int, input().split())

num_array = [0] * (m + 1)


def sequence(x):
    if x > m:
        for i in range(1, m + 1):
            print(num_array[i], end=" ")
        print()
    else:
        for i in range(1, n + 1):
            num_array[x] = i
            sequence(x + 1)
            num_array[x] = 0


sequence(1)
