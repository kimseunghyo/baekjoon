num = list(map(int, input().split()))
num.append(0)
rec = list()

rec.append(num[0] - num[4])
rec.append(num[1] - num[4])
rec.append(num[2] - num[0])
rec.append(num[3] - num[1])
print(min(rec))