t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    if n % h == 0:
        room_h = h
        room_num = n // h
    else:
        room_h = n % h
        room_num = (n // h) + 1

    print(room_h * 100 + room_num)