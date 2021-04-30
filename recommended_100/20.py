n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()


def bs_a(A, b):
    ok = -1
    ng = n
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if b > A[mid]:
            ok = mid
        else:
            ng = mid
    return ok

def bs_b(C, b): 
    ok = n
    ng = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if b < C[mid]:
            ok = mid
        else:
            ng = mid
    return ok

ans = 0
for b in B:
    a_i = bs_a(A, b) + 1
    c_i = n - bs_b(C, b)
    print("ac", a_i, c_i)
    ans += a_i * c_i
print(ans)