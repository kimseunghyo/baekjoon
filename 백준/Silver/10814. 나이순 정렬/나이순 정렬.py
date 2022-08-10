n = int(input())
member_list = []

for _ in range(n):
    member_list.append(list(map(str, input().split())))

member_list.sort(key=lambda x: int(x[0]))

for member in member_list:
    print(member[0], member[1])