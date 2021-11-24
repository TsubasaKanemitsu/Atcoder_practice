from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

# 自分の位置より後ろにある自分の数だけ組み合わせ数が減る
ans = 0
cnt = defaultdict(int)
for i in range(n):
    ans += n - (i + 1)
    ans -= cnt[A[i]]
    cnt[A[i]] += 1
print(ans)