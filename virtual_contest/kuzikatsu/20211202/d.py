import bisect

n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()

ans = 0
for i in range(n):
    b = B[i]
    a_num = bisect.bisect_left(A, b)
    c_num = bisect.bisect_right(C, b)
    ans += a_num * (n - c_num)
print(ans)