import sys

n_list = [0] * 10001

n = int(input())

for _ in range(n):
    num = int(sys.stdin.readline())
    n_list[num] = n_list[num] + 1

for i in range(10001):
    if n_list[i] != 0:
        for j in range(n_list[i]):
            print(i)