from collections import Counter
n = int(input())
D = list(map(int, input().split()))
m = int(input())
T = list(map(int, input().split()))

# 問題案より問題数が多いと無理
if m > n:
    print("NO")
    exit()


# 問題案
cnt_d = Counter(D)
# 問題
cnt_t = Counter(T)

# 各難易度の問題数分の問題案があるかどうか
for diff, cnt in cnt_t.items():
    if cnt_d[diff] < cnt:
        print("NO")
        exit()
print("YES")