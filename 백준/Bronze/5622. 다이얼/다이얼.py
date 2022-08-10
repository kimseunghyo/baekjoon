word = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for i in range(len(word)):
    for di in dial:
        if word[i] in di:
            time += dial.index(di) + 3
print(time)