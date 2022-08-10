word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in croatia:
    word = word.replace(c, 'C')

print(len(word))