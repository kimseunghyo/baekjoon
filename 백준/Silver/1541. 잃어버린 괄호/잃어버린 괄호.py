math = input().split('-')
sum_n = 0

for i in math[0].split('+'):
    sum_n += int(i)

for i in math[1:]:
    for j in i.split('+'):
        sum_n -= int(j)


print(sum_n)