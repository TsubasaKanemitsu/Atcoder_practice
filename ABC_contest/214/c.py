n = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
S.extend(S)
T.extend(T)

# 高橋からすねけiがに初めて宝石を受け取る時刻
# すぬけ -> すねけの受け渡しよりこちらの受け渡しの方が早ければ、値を更新する
first_rec = T
time = T[0]
# pre_time = 0
ans = []
for i in range(2 * n):
    if i == 0:
        time = T[0]
        ans.append(time)
    elif i == 1:
        time = min(T[0] + S[0], T[i])
        ans.append(time)
    else:
        time = min(T[i - 1], time) + S[i - 1]
        ans.append(min(T[i], time))

for p in ans[n:]:
    print(p)