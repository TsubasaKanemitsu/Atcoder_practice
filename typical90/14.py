# 5分30秒
# ソートして貪欲法
# 制約
# 全員を別々の学校に通わせる
# 家から近い学校になるようにする．学校から家までの距離の総和が小さくなるようにする
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
diff = 0

for i in range(n):
    diff += abs(A[i] - B[i])
print(diff)