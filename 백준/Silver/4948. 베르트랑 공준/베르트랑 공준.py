def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


prime_list = list()

for i in range(1, 123456 * 2 + 1):
    if isPrime(i):
        prime_list.append(i)

while True:
    n = int(input())
    cnt = 0

    if n == 0:
        break

    for i in prime_list:
        if n < i <= 2 * n:
            cnt += 1
    print(cnt)