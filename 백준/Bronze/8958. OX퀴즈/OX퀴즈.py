n = int(input())

for i in range(n):
    score = 0
    sum_score = 0

    result_list = list(input())

    for result in result_list:
        if result == "O":
            score += 1
            sum_score += score
        else:
            score = 0

    print(sum_score)