# 15分
N, x = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()

ans = []
for a in A:
    x -= a
    if x >= 0:
        ans.append(0)
    else:
        ans.append(a)
ans = ans.count(0)
if x > 0:
    ans -= 1
print(ans)
