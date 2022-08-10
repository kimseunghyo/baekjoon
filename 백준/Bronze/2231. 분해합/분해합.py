n = int(input())

for i in range(1, n + 1):
    sum_m = i + sum(map(int, str(i)))

    if sum_m == n:
        print(i)
        break
else:
    print(0)