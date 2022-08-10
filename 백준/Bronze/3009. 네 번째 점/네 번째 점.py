x_num = list()
y_num = list()

for i in range(3):
    x, y = list(map(int, input().split()))
    x_num.append(x)
    y_num.append(y)

for i in range(3):
    if x_num.count(x_num[i]) == 1:
        x_num4 = x_num[i]
    if y_num.count(y_num[i]) == 1:
        y_num4 = y_num[i]

print(x_num4, y_num4)