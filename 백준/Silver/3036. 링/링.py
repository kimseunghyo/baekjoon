import math

n = int(input())
r = list(map(int, input().split()))

for i in range(1, n):
    gcd_n = math.gcd(r[0], r[i])
    a = r[0] // gcd_n
    b = r[i] // gcd_n
    print('%d/%d' % (a, b))