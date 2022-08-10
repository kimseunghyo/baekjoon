def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


t = int(input())

for _ in range(t):
    n = int(input())

    ln = n // 2
    rn = n // 2

    for i in range(n // 2):
        if isPrime(ln) and isPrime(rn):
            print(ln, rn)
            break
        else:
            ln = ln - 1
            rn = rn + 1