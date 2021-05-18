# 解説
# https://drken1215.hatenablog.com/entry/2021/03/22/175100
# 決めてから整合性を確認


# A1 ~ Anは1列目のみを見れば一意に決まる
# B1 = Bnは1行目を見れば一意に決まる
# AやBの相対的な値の関係がわかる

# A, Bともに最小値が0となるように，差をとる
# (その差分はA + B = Cとするためのそれぞれの片割れと考える)
# 足りない分はC - (A + B)を行い，一律にA or Bのどちらかに足し合わせる(ここでA, Bは最小値が0のためC - (A + B)がマイナスになることはない)
# そうすることでC = A + Bになるようにできる
#(この状況でA + B = Cにならない要素があれば，それはC = A + Bにすることができないということである)

n = int(input())
C = [list(map(int, input().split())) for _ in range(n)]

mix = C[0][0]
miy = C[0][0]


for i in range(n):
    mix = min(mix, C[i][0])
    miy = min(miy, C[0][i])

X = []
Y = []
for i in range(n):
    X.append(C[i][0] - mix)
    Y.append(C[0][i] - miy)

# 差分を一律に足す(X + Y = Cにするために必要な差分を埋め合わせている)
diff = C[0][0] - X[0] - Y[0]

for i in range(n):
    X[i] += diff

for i in range(n):
    for j in range(n):
        if X[i] + Y[j] != C[i][j]:
            print("No")
            exit()
print("Yes")
for i in range(n):
    print(X[i], end=" ")
print()
for i in range(n):
    print(Y[i], end=" ")