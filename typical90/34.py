from collections import deque
import random

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

# n = random.randint(1, 10 ** 5)
# k = random.randint(1, n)
# A = [random.randint(1, 10 ** 9) for _ in range(n)]

rm_num = set()
unique_num = set()
ans = deque()

# ans = 0
# for i in range(n):
#     for j in range(i + 1, n + 1):
#         num_kind = len(set(A[i:j]))
#         if num_kind <= k:
#             ans = max(ans, len(A[i:j]))
# print(ans)

length = 0
for i in range(n):
    unique_num.add(A[i])
    ans.append(A[i])
    if len(unique_num) > k:
        rm_n = ans.popleft()
        unique_num.remove(rm_num)
        # try:
        #     rm_num = ans.popleft()
        #     unique_num.remove(rm_num)
        # except Exception as e:
        #     print("err:", e)
        #     print("rm", rm_num)
        while ans[0] == rm_num:
            ans.popleft()
    length = max(length, len(ans))
print(length)
    