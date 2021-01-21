h, w = list(map(int, input().split()))

word = []
for i in range(h):
    word.append(input())

word.insert(0, '#' * w)
word.append('#' * w)
for w in range(len(word)):
    print('#' + word[w] + '#')

