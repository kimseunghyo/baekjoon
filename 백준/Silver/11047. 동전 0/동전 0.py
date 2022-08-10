n, k = list(map(int, input().split()))
a = []

for _ in range(n):
    a.append(int(input()))

a = a[::-1]
result = 0

for i in range(n):
    if k == 0:
        break

    if a[i] <= k:
        result += k // a[i]
        k = k % a[i]

print(result)