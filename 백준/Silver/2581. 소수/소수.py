m = int(input())
n = int(input())
prime_number = list()

for num in range(m, n + 1):
    cnt = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                cnt += 1
                break
        if cnt == 0:
            prime_number.append(num)

if len(prime_number) == 0:
    print(-1)
else:
    print(sum(prime_number))
    print(min(prime_number))