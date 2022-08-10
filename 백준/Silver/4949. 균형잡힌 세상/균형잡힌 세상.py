while True:
    array = input()
    stack = []
    temp = True

    if array[0] == '.':
        break

    for a in array:
        if a == '(' or a == '[':
            stack.append(a)
        elif a == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                temp = False
                break
        elif a == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                temp = False
                break

    if len(stack) == 0 and temp == True:
        print("yes")
    else:
        print("no")