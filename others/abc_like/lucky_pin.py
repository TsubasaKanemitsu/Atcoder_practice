# 15分(全探索)
# DPの方法もある
n = int(input())
S = input()

ans = 0
for i in range(1000):
    num = str(i).zfill(3)
    cnt = 0
    k = 0
    for j in range(len(S)):
        if S[j] == num[k]:
            cnt += 1
            k += 1
            if k == 3:
                ans += 1
                break
print(ans)