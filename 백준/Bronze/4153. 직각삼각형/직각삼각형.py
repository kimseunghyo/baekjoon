while True:
    rec = list(map(int, input().split()))
    rec.sort()

    if rec[0] == 0 and rec[1] == 0 and rec[2] == 0:
        break

    if (rec[0] ** 2) + (rec[1] ** 2) == rec[2] ** 2:
        print("right")
    else:
        print("wrong")