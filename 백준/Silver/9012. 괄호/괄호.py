n = int(input())

for _ in range(n):
    array = input()
    stack = []

    for a in array:
        if a == '(':
            stack.append('(')
        elif a == ')' and '(' in stack:
            stack.pop()
        else:
            stack.append(-1)

    if len(stack) == 0 and -1 not in stack:
        print("YES")
    else:
        print("NO")