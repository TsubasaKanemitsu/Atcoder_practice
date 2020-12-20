# 累積和 & 全探索では時間内で処理が終了しない問題

n = int(input())
a = list(map(int, input().split()))

i = 0
ans = 0

a.sort()
s = [0 for i in range(0, n)]
for i in range(0, n - 1):
    s[i + 1] = s[i] + a[i]
# print(s)
for i in range(1, n):
    ans += a[i] * i - s[i]
print(ans)

# https://drken1215.hatenablog.com/entry/2020/12/19/231000