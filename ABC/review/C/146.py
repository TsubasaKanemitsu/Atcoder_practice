# https://drken1215.hatenablog.com/entry/2020/01/05/154700
a, b, x = list(map(int, input().split()))

n = 10 ** 9

# 桁数出力
def d(n):
    n = str(n)
    return len(n)

left = 1
right = n + 1

if a * left + b * d(left) > x:
    print(0)
    exit()

while right - left > 1:
    mid = (right + left) // 2
    if a * mid + b * d(mid) <= x:
        left = mid
    else:
        right = mid
print(left)