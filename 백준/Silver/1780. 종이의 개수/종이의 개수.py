n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]
result = []

def make_paper(x, y, n):
    num = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if num != paper[i][j]:
                make_paper(x, y, n // 3)
                make_paper(x, y + n // 3, n // 3)
                make_paper(x, y + (n * 2) // 3, n // 3)

                make_paper(x + n // 3, y, n // 3)
                make_paper(x + n // 3, y + n // 3, n // 3)
                make_paper(x + n // 3, y + (n * 2) // 3, n // 3)

                make_paper(x + (n * 2) // 3, y, n // 3)
                make_paper(x + (n * 2) // 3, y + n // 3, n // 3)
                make_paper(x + (n * 2) // 3, y + (n * 2) // 3, n // 3)

                return

    result.append(num)

make_paper(0, 0, n)

print(result.count(-1))
print(result.count(0))
print(result.count(1))