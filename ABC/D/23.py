n = int(input())
HS = [list(map(int, input().split())) for _ in range(n)]


def is_ok(x, h):
    if x >= h:
        return True
    else:
        False


def binary_search():
    ok = 10 ** 30
    ng = 0
    
    while abs(ok - ng) > 1:
        t = [0] * n
        mid = (ok + ng) // 2
        flag = True
        
        for i in range(n):
            h, s = HS[i]
            if is_ok(mid, h):
                # 各風船がXに到達するのに掛かる時間
                t[i] = (mid - h) / s
            else:
                flag = False
        
        # 制限時間が短い順にソート
        t.sort()

        for i in range(n):
            if t[i] < i:
                flag = False
        if flag:
            ok = mid
        else:
            ng = mid
    return ok
        

print(binary_search())