# オーバーフローを起こさないようにfor文の終端をしっかり決める必要があった．
n = int(input())

for a in range(1, 38):
    for b in range(1, 26):
        if pow(3, a) + pow(5, b) == n:
            print(a, b)
            exit()
print(-1)