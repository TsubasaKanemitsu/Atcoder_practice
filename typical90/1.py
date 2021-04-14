# 二分探索: 最小値の最大化
# 最小の幅がどれぐらいになるのかを二分探索で範囲を制限しながら探索する
# 類題 ABC023D　射撃王
N, L = list(map(int, input().split()))
K = int(input())
A = list(map(int, input().split()))
A.append(L)
diff = [A[0]]

for i in range(1, N + 1):
    diff.append(A[i] - A[i - 1])

left = 0
# 取り得る最大値は長さLを丁度K + 1個で割れる長さなので
# right = L // (K + 1)
right = L // (K + 1)

# 長さmid以上をK + 1個以上作れない場合，Trueそれ以外False
def check(mid):
    cnt = 0
    dif = 0
    result = False
    for i in range(N + 1):
        dif += diff[i]
        if dif > mid:
            cnt += 1
            dif = 0

    if cnt >= K + 1:
        result = True

    return result


while right - left > 1:
    mid = left + (right - left) // 2
    # 長さmid以上をK + 1個以上作成できない場合，1ピースあたりの長さの上限を下げる
    if check(mid) == False:
        right = mid
    else:
        left = mid

ans = right
print(ans)
