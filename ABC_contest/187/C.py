n = int(input())

_S = []
S = []

for i in range(n):
    word = input()
    if word.startswith('!'):
        _S.append(word)
    else:
        S.append(word)
_S = set(_S)
S = set(S)

result ='satisfiable'
for s in S:
    if '!' + s in _S:
        result = s
        break
print(result)