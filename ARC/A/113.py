# 2WA
# 調和級数
import math
k = int(input())

ans = 0
for i in range(1, 2 * 10 ** 5 + 1):
    for j in range(1, 2 * 10 ** 5 + 1):
        ans += math.floor(k / (i * j))
        if i * j > k:
            break

print(ans)

# k = int(input())
# ans = 0
# for a in range(1, k + 1):
#     for b in range(1, k // a + 1):
#         ans += k // (a * b)
# print(ans)
