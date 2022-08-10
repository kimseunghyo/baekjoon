t = int(input())

for i in range(t):
    r, s = list(input().split())
    for j in s:
        print(j * int(r), end="")
    print()