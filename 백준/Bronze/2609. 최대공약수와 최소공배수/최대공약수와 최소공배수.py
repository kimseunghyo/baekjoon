import math

x, y = list(map(int, input().split()))

num = math.gcd(x, y)

print(num)
print(x * y // num)