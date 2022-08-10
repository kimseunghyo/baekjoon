n = int(input())

time = []
room = []

for i in range(n):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x: (x[1], x[0]))

room.append(time[0])

for i in range(1, n):
    if time[i][0] >= room[-1][1]:
        room.append(time[i])

print(len(room))