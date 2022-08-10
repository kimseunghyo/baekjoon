n = input()
num = list()

num.append(list(map(int, n)))
num[0].sort(reverse=True)

for i in num:
    for j in i:
        print(j, end="")