# 2分探索
a, b, x = list(map(int, input().split()))

def check_ok(n, x):
    if a * n + b * len(str(n)) <= x:
        return True
    else:
        return False



def binary_search(X):
    ok = 0
    ng = 10 ** 9 + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if check_ok(mid, X):
            ok = mid
        else:
            ng = mid
    return ok

print(binary_search(x))