# ABC 165C
# 28min
# 重複順列全探索
import itertools
n, m, q = list(map(int, input().split()))

abcd = [list(map(int, input().split())) for _ in range(q)]

ans = 0
for A in itertools.combinations_with_replacement([i for i in range(1, m + 1)], n):
    continue_flag = False
    for i in range(n - 1):
        if A[i + 1] < A[i]:
            continue_flag = True
    
    if continue_flag:
        continue
    
    temp_ans = 0
    for i in range(q):
        a, b, c, d = abcd[i]
        a -= 1
        b -= 1
        if A[b] - A[a] == c:
            temp_ans += d
    # print(A)
    ans = max(temp_ans, ans)
print(ans)