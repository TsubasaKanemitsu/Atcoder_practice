from sys import stdin
word = input()
sentence = []

while True:
    input_word = input().split()
    if "END_OF_TEXT" in input_word:
        break
    else:
        input_word = list(map(lambda x: x.lower(), input_word))
        sentence.extend(input_word)

print(sentence.count(word))