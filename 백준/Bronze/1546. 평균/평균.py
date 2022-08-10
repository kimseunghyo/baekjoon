n = int(input())
score = list(map(int, input().split()))
new_score = list()

for i in range(n):
    new_score.append(score[i] / max(score) * 100)

average_score = sum(new_score) / n
print(average_score)