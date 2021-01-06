N = int(input())
result = "Yes"
end_word = []
word_list = []

def has_duplicates(word):
    return len(word) != len(set(word))

for i in range(N):
    w = input()
    word_list.append(w)
    if i > 0:
        if w[0] != end_word[i - 1]:
            result = "No"
    end_word.append(w[-1])
if has_duplicates(word_list):
    result = "No"

print(result)