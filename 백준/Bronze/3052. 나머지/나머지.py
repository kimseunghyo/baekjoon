n = list()
sum_n = list()

for i in range(10):
    n.append(int(input()))
    sum_n.append(int(n[i]) % 42)

print(len(set(sum_n)))