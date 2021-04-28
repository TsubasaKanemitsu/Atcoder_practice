n, k = list(map(int, input().split()))
A = list(map(int, input().split()))


def binary_search(K):
    ok = n
    ng = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        
        if A[mid] >= K:
            ok = mid
        else:
            ng = mid
        
    return ok

def binary_search(K):
    left = 0
    right = n - 1
    while abs(right - left) > 1:
        mid = (right + left) // 2
        
        if A[mid] < K:
            left = mid
        else:
            right = mid
        
    return right


right = binary_search(k)

if right == n - 1:
    print(-1)
else:
    print(right)