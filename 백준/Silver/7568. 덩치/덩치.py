n = int(input())
body = list()

for _ in range(n):
    weight, height = map(int, input().split())
    body.append((weight, height))

for i in body:
    k = 1
    for j in body:
        if i[0] < j[0] and i[1] < j[1]:
            k += 1

    print(k, end=" ")