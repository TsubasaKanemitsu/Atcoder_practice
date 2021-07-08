# 7分
# もっといい実装あるはず

# キーワード
# 一番大きい値とそれ以外
# 一番大きい値が2つあるとき

n = int(input())
A = [int(input()) for _ in range(n)]

# 元の実装
# cp_A = A.copy()
# cp_A.sort(reverse=True)

# max_a = cp_A[0]
# second_a = cp_A[1]

# cnt = A.count(max_a)

# for a in A:
#     if a == max_a:
#         if cnt == 2:
#             print(a)
#         else:
#             print(second_a)
#     else:
#         print(max_a)

lft = [A[0]]
rft = [A[n - 1]]

for i in range(1, n):
    lft.append(max(lft[i - 1], A[i]))

for i in range(1, n):
    rft.append(max(rft[i - 1], A[n - (i + 1)]))
# print(lft, rft)
for i in range(n):
    if i == 0:
        print(rft[n - (i + 2)])
    elif i == n - 1:
        print(lft[n - 2])
    else:
        print(max(lft[i - 1], rft[n - i - 2]))
    