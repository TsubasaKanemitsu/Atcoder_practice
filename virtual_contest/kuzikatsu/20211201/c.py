import math
n = int(input())

ans = 0
for a in range(1, n + 1):
    if a * a * a > n:
        break
    for b in range(a, n + 1):
        if a * b * b > n:
            break
        # if not a <= n / b ** 2:
        #     continue
        ans += (math.floor(n / (a * b)) - b) + 1
print(ans)

# ans = 0
# for a in range(1, pow(n, 1 / 3)):
#     for b in range(a, pow(n / a, 1 / 2)):
#         for c in range(b, n / (a * b)):
#             if a * b * c <= n:
#                 ans += 1
# print(ans)