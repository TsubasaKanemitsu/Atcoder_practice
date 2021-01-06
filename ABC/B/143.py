import itertools
n = int(input())
d = list(map(int, input().split()))

takoyaki_select = list(itertools.combinations(d, 2))
ans = 0
for takoyaki in takoyaki_select:
    ans += takoyaki[0] * takoyaki[1]

print(ans)