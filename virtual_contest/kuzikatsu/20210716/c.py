# https://drken1215.hatenablog.com/entry/2019/05/13/125000
k, a, b = list(map(int, input().split()))


if a >= b:
    print(k + 1)
else:
    k -= (a - 1)
    if k % 2 == 0:
        ans = max((b - a) * (k // 2 - 1) + b, a + k)
    else:
        ans = max((b - a) * (k // 2 - 1) + b + 1, a + k)
    print(ans)