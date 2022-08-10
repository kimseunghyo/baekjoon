n = int(input())

image = [list(map(int, input())) for _ in range(n)]

def quadTree(x, y, n):
    color = image[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != image[i][j]:
                print('(', end='')
                quadTree(x, y, n // 2)
                quadTree(x, y + n // 2, n // 2)
                quadTree(x + n // 2, y, n // 2)
                quadTree(x + n // 2, y + n // 2, n // 2)
                
                print(')', end='')

                return

    print(color, end='')

quadTree(0,0,n)