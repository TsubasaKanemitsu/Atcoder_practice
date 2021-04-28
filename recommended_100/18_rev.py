# 値の一致を見るので，探索範囲は左から右へ全走査する
# 一致した場合は, 1を返し，それ以外は0を返すことでカウントを行う
# 値と添え字を利用した二分探索

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))


def binary_search(n):
    left = 0
    right = len(S) - 1
    while right - left >= 0:
        mid = (left + right) // 2
        if n == S[mid]:
            return 1
        elif n > S[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return 0

cnt = 0
for i in range(q):
    cnt += binary_search(T[i])

print(cnt)