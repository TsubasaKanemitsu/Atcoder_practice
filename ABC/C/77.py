# bisect (二分探索)
import bisect

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
lc = len(C)

ans = 0
for b in B:
    a = bisect.bisect_left(A, b)
    c = bisect.bisect_right(C, b)
    ans += a * (lc - c)
print(ans)