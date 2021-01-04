import sys
sentence = []

for e in sys.stdin:
    sentence.extend(e.lower().rstrip('\r\n'))

key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', \
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_count_dict = {}
for k in key:
    word_count_dict.setdefault(k, 0)

for k in key:
    count = sentence.count(k)
    word_count_dict[k] = int(count)

for k, value in word_count_dict.items():
    print(f'{k} : {value}')
