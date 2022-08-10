n, m = map(int, input().split())

visit = [0] * (n + 1)
num_array = [0] * (m + 1)


def duplicate_check(num):
    if visit[num] == 0:
        return True
    else:
        return False


def sequence(x):
    if x > m:
        for i in range(1, m + 1):
            print(num_array[i], end=" ")
        print()
    else:
        for i in range(1, n + 1):
            if duplicate_check(i):
                visit[i] = 1
                num_array[x] = i
                sequence(x + 1)
                visit[i] = 0
                num_array[x] = 0


sequence(1)