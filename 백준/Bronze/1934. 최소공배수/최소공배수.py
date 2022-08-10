import math

t = int(input())

for _ in range(t):
    x, y = list(map(int, input().split()))

    print(x * y // math.gcd(x, y))