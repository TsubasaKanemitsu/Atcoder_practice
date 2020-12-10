word_list = list(input())

answer_list = ['A', 'C', 'G', 'T']
count = 0
for i in range(len(word_list)):
    temp_count = 0
    for j in range(i, len(word_list)):
        if word_list[j] in answer_list:
            temp_count += 1
        else:
            break
    if count < temp_count:
        count = temp_count
print(count)

# 終了条件を勘違いしていた
# やり直し?