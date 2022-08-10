n_set = set(range(1, 10001))
remove_set = set()

for i in n_set:
    for j in str(i):
        i += int(j)
    remove_set.add(i)

self_num = n_set - remove_set

for num in sorted(self_num):
    print(num)