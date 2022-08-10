n = int(input()) # 도시 갯수
km = list(map(int, input().split())) # 도로의 길이
won = list(map(int, input().split())) # 주유소의 리터당 가격

min_won = won[0]
money = won[0] * km[0]

for i in range(1, n - 1):
    if min_won > won[i]:
        min_won = won[i]
    money += min_won * km[i]

print(money)