x = int(input())
line = 1

while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    ln = x
    rn = line - x + 1
else:
    ln = line - x + 1
    rn = x

print(ln, rn, sep="/")