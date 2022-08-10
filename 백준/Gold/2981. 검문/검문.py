import math
import sys

n = int(input())
num = []
m = []
minus_num = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

for i in range(1, n):
    minus_num.append(num[i] - num[i - 1])

gcd_num = minus_num[0]

for i in range(1, len(minus_num)):
    gcd_num = math.gcd(gcd_num, minus_num[i])

for i in range(2, int(math.sqrt(gcd_num)) + 1):
    if gcd_num % i == 0:
        m.append(i)
        m.append(gcd_num // i)

m.append(gcd_num)
m_list = list(set(m))
m_list.sort()
print(*m_list)