n, m = map(int, input().split())
cards = list(map(int, input().split()))
card_sum = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if card_sum <= cards[i] + cards[j] + cards[k] <= m:
                card_sum = cards[i] + cards[j] + cards[k]

print(card_sum)