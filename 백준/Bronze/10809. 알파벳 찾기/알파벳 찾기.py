s = list(input())

for i in range(97, 123):
    cnt = 0
    
    for j in s:
        if chr(i) == j:
            cnt += 1
            break

    if cnt == 1:
        print(s.index(j), end=" ")
    else:
        print(-1, end=" ")