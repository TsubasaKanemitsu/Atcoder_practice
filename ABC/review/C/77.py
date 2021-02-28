# 13分
# 3層構造の問題は真ん中を固定させるパターンがある
# データの単調性がある場合，二分探索で値の探索を行える可能性を考える
import bisect
n = int(input())

a = list(map(int, input().split()))
a.sort()
b = list(map(int, input().split()))
b.sort()
c = list(map(int, input().split()))
c.sort()

ans = 0
for i in range(n):
    a_num = bisect.bisect_left(a, b[i])
    c_num = bisect.bisect_left(c, b[i] + 1)
    c_num = n - c_num
    ans += a_num * c_num
print(ans)