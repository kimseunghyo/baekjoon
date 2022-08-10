import math

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

    # 1. 동심원일 때 -1
    if distance == 0 and r1 == r2:
        print(-1)
    # 2. 내접이거나 외접일 때 1
    elif distance == abs(r1 - r2) or distance == r1 + r2:
        print(1)
    # 3. 두 점에 접할 때 2
    elif abs(r1 - r2) < distance < r1 + r2:
        print(2)
    # 4. 그 외는 0
    else:
        print(0)