n = int(input())
house_n = 1
cnt = 1

while True:
    if n == 1:
        print(1)
        break
    else:
        house_n += cnt * 6
        if n <= house_n:
            print(cnt + 1)
            break
        else:
            cnt += 1