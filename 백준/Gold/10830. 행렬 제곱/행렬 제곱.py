n, b = list(map(int, input().split()))
a = []
c = [[0 for _ in range(n)] for _ in range(n)]
p = 1000

for _ in range(n):
    a.append(list(map(int, input().split())))

def multiple(x1, x2):
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = 0
            for u in range(n):
                c[i][j] += (x1[i][u] * x2[u][j]) % p

    return c


def power(a, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= p

        return a

    else:
        po = power(a, b // 2)

        if b % 2 == 0:
            return multiple(po, po)

        else:
            return multiple(multiple(po, po), a)

result = power(a, b)

for i in range(n):
    for j in range(n):
        print(result[i][j] % p, end=' ')
    print()