n, k = list(map(int, input().split()))
p = 1000000007

factorial = [1 for _ in range(n + 1)]

for i in range(2, n + 1):
    factorial[i] = factorial[i - 1] * i % p

a = factorial[n] % p
b = factorial[k] * factorial[n - k]% p

def power(a, b):
    if b == 1:
        return a % p

    else:
        x = power(a, b // 2)

        if b % 2 == 0:
            return x * x % p
        else:
            return x * x * a % p

print((a % p) * (power(b, p - 2) % p) % p)