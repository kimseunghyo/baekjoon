n = int(input())
n_sum = n
cycle = 0

while True:
    ln = n_sum // 10
    rn = n_sum % 10

    n_sum = (rn * 10) + ((ln + rn) % 10)

    cycle += 1

    if n_sum == n:
        print(cycle)
        break