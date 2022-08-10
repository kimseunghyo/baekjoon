n = int(input())
point_list = []

for _ in range(n):
    point_list.append(list(map(int, input().split())))

point_list.sort()

for point in point_list:
    print(point[0], point[1])