from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

def combinations_count(n, r):
    import math
    return math.factorial(n) // ((math.factorial(n - r)) * math.factorial(r))


cnt = defaultdict(int)
for i in range(n):
    cnt[A[i] % 1000] += 1

ans = []
for k, v in cnt.items():
    ans.append([k, v])
count = 0
for i in range(len(ans)):
    a, b = ans[i]
    for j in range(i, len(ans)):
        c, d = ans[j]
        if a == c and b >= 2:
            count += combinations_count(b, 2)
        elif a == c and b == 1:
            pass
        else:
            if (a - c) % 200 == 0:
                count += b * d
print(count)