# 6分
a, b = list(map(int, input().split()))

# num = [1]

# for i in range(1, 499501):
#     num.append(num[i - 1] + i + 1)

# for i in range(len(num) - 1):
#     if num[i + 1] - num[i] == b - a:
#         ans = num[i] - a
#         print(ans)

n = b - a
print(n * (n - 1) // 2 - a)