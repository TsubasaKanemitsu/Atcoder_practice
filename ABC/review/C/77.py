# 13分
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