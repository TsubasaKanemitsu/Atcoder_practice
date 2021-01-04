# 4分45秒
s = input()

word_l = 0
temp_word_l = 0
for w in s:
    if not w in ['A', 'C', 'G', 'T']:
        temp_word_l = 0
    else:
        temp_word_l += 1
        word_l = max(word_l, temp_word_l)
print(word_l) 