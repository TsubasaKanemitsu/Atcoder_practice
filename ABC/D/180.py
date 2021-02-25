# 解けなかった
# 貪欲法
# やりたいことの方向性は同じだった
# 計算量の考え方がまだ直感的でない
# log関係が特に...
x, y, a, b = map(int, input().split())
ans = 0
while a * x <= x + b and a * x < y:
    x *= a
    ans += 1
print(ans + (y - 1 - x) // b)

# 自分の解答
# x, y, a, b = list(map(int, input().split()))

# exp = 0

# if a * x < b:
#     exp = 0
#     i = 0
#     res = 0
#     while res < b:
#         res = a ** i * x * (a - 1)
#         i += 1
#         if res > b:
#             i -= 1
#     exp = i
#     x = a ** i * x
    
#     diff = y - x
    
#     if diff % b == 0:
#         exp = diff // b + exp - 1
#     else:
#         exp = diff // b + exp
    
# else:
#     diff = y - x
#     if diff % b == 0:
#         exp = diff // b - 1
#     else:
#         exp = diff // b + exp
# print(exp)