# Biより真に大きいパーツと真に小さいパーツが
# A, Cに何個ずつ存在するかの組み合わせの総和を考えればいい
# 真に大きい，小さいとはBiより-1, +1した値なので，
# それらの値が存在する場所を二分探索で見つければいい
# bisect_rightで真に小さいパーツの最大数を求める(上限)
# bisect_leftで真に大きいパーツの最大数を求める(上限)

import bisect
n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
ans = 0
for i in range(n):
    a = bisect.bisect_right(A, B[i] - 1)
    c = bisect.bisect_left(C, B[i] + 1)
    ans += a * (n - c)
print(ans)