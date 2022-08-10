n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]
result = []

def make_paper(x, y, n):
    color = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                make_paper(x, y, n // 2)
                make_paper(x, y + n // 2, n // 2)
                make_paper(x + n // 2, y, n // 2)
                make_paper(x + n // 2, y + n // 2, n // 2)
                
                return

    if color == 0:
        result.append(color)
    else:
        result.append(color)

make_paper(0,0,n)

print(result.count(0))
print(result.count(1))