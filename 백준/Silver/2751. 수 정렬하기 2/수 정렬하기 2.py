def ascending(num_list):
    num_list.sort()

    for num in num_list:
        print(num)


n = int(input())
num_list = list()

for _ in range(n):
    num_list.append(int(input()))

ascending(num_list)