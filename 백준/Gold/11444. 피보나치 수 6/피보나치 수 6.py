n = int(input())
p = 1000000007

# 행렬 곱셈을 응용해 피보나치 수를 구하는 문제

def multiple(x1, x2):
    b = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                b[i][j] += (x1[i][k] * x2[k][j]) % p

    return b

a = [[1, 1], [1, 0]]

def power(a, n):
    if n == 1:
        return a

    else:
        x = power(a, n // 2)

        if n % 2 == 0:
            return multiple(x, x)
        else:
            return multiple(multiple(x, x), a)

result = power(a, n)

print(result[0][1] % p)