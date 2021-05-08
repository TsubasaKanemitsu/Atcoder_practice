n = int(input())
S = [input().split() for _ in range(n)]

left = []
right = []
center = []
extra = ''

for s in S:
    s = s[0]
    if s[0] == 'B' and s[-1] == 'A':
        center.append(s)
    elif s[0] == 'B' and s[-1] != 'A':
        right.append(s)
    elif s[0] != 'B' and s[-1] == 'A':
        left.append(s)
    else:
        extra += s

ans = ''
if len(left) > 0:
    ans += left.pop()
while len(center) > 0:
    ans += center.pop()
if len(right) > 0:
    ans += right.pop()
while True:
    if len(left) > 0:
        ans += left.pop()
    if len(right) > 0:
        ans += right.pop()
    if len(left) == len(right) == 0:
        break
print(ans.count('AB') + extra.count('AB'))
