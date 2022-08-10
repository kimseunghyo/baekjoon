n = int(input())

for i in range(n):
    average = 0
    average_student = 0
    average_ratio = 0

    score_list = list(map(int, input().split()))
    average = (sum(score_list) - score_list[0]) / score_list[0]

    for score in score_list[1:]:
        if score > average:
            average_student += 1

    average_ratio = average_student / score_list[0] * 100
    print("{:.3f}%".format(round(average_ratio, 3)))
