# 解説記事
# https://drken1215.hatenablog.com/entry/2019/12/22/224100

n = int(input())

if n % 2 == 1:
    print(0)
else:
    m = n // 2
    ans = 0
    while m > 0:
        m = m // 5
        ans += m
    print(ans)