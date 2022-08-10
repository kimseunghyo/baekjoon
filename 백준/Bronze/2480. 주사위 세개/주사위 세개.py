dice_list = list(map(int, input().split()))

reward = 0

for i in dice_list:
    if dice_list.count(i) == 3:
        reward = 10000 + i * 1000
        break
    elif dice_list.count(i) == 2:
        reward = 1000 + i * 100
        break
    else:
        reward = max(dice_list) * 100

print(reward)