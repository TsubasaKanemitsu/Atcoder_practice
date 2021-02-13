# 20分
# https://img.atcoder.jp/arc099/editorial.pdf
# (k - 1) * x + k >= n
import math
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort()
min_val = min(a)
new_a = [i for i in a if i != min_val]
l_a = len(new_a) + 1
ans = math.ceil((l_a - k) / (k - 1)) + 1
print(ans)