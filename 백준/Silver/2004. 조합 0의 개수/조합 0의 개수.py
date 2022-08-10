n, m  = list(map(int, input().split()))

def num_count(num, x):
    cnt = 0

    while num != 0:
        num = num // x
        cnt += num

    return cnt


two_num = num_count(n, 2) - num_count(m, 2) - num_count(n - m, 2)
five_num = num_count(n, 5) - num_count(m, 5) - num_count(n - m, 5)

print(min(two_num, five_num))