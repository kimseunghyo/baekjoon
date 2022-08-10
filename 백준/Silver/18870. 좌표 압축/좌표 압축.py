n = int(input())
x_list = list(map(int, input().split()))
x_list_sort = sorted(set(x_list))

x_dict = {x_list_sort[i]: i for i in range(len(x_list_sort))}

for x in x_list:
    print(x_dict[x], end=" ")