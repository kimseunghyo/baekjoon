n = int(input())
word_set = set()
word_list = []

for _ in range(n):
    word_set.add(input())

word_list = list(word_set)
word_list.sort(key=lambda x: (len(x), x))

for word in word_list:
    print(word)