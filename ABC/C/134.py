n = int(input())
A = []
for i in range(n):
    A.append(int(input()))

# 最初に0を入れないと1回目の
# 自分より左の最大値の管理
left = [0]
# 自分より右の最大値の管理
right = [0]

for a in A:
    left.append(max(a, left[-1]))

for a in reversed(A):
    right.append(max(a, right[-1]))

for i in range(n):
    print(max(left[i], right[n - i - 1]))