from math import factorial

n = int(input())

for _ in range(n):
    n, m = list(map(int, input().split()))

    print(factorial(m) // (factorial(n) * (factorial(m - n))))