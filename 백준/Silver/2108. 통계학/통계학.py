import sys
from collections import Counter

n = int(input())
num_list = list()

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

# 첫째 줄 산술평균
n_average = sum(num_list) / n
print(round(n_average))

# 둘째 줄 중앙값
num_list.sort()
n_median = num_list[int(n / 2)]
print(n_median)

# 셋째 줄 최빈값. 단 여러개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력
n_mode = Counter(num_list).most_common()

if len(n_mode) > 1 and n_mode[0][1] == n_mode[1][1]:
    print(n_mode[1][0])
else:
    print(n_mode[0][0])

# 넷째 줄 범위
n_range = max(num_list) - min(num_list)
print(n_range)