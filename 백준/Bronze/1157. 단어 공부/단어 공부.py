words = input().upper()
word_list = list(set(words))
cnt_list = list()

for w in word_list:
    cnt = words.count(w)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    print(word_list[max_index])