while True:
    x, y = list(map(int, input().split()))

    if x == 0 and y == 0:
        break

    if (y // x) * x == y :
        print("factor")
    elif (x // y) * y == x:
        print("multiple")
    else:
        print("neither")