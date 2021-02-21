# 解けなかった
# 10 ** 18乗となりえる最小値の場合のコーナーケースを考えれていなかった

x = input()
x_val = int(x)
m = int(input())

d = max(map(int, list(x))) + 1
l = len(x)

if l == 1:
    print(int(int(x_val) <= m))
    exit()

cnt = 0
# 種類
def Base_10_to_n(x, n):
    ans = 0
    l = len(x)
    for i in range(1, l + 1):
        ans += int(x[- i]) * (n ** (i - 1))
    return ans

left = d
right = 10 ** 18 + 1

def binary_serach(left, right):
    while left <= right:
        mid = (right + left) // 2
        if Base_10_to_n(x, mid) <= m:
            left = mid + 1
        else:
            right = mid - 1
    return right
r = binary_serach(left, right)
print(r - (d - 1))
