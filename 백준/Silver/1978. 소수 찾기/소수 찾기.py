n = int(input())
number = list(map(int, input().split()))
prime_number = 0

for num in number:
    cnt = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                cnt += 1
        if cnt == 0:
            prime_number += 1

print(prime_number)