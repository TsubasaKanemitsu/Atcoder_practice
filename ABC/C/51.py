sx, sy, tx, ty = list(map(int, input().split()))

f = 'L' + (abs(sy - ty) + 1) * 'U' + (abs(sx - tx) + 1) * 'R' + 'D'
s = abs(sx - tx) * 'L' + abs(sy - ty) * 'D'
t = abs(sx - tx) * 'R' + abs(sy - ty) * 'U'
ff = 'R' + (abs(sy - ty) + 1) * 'D' + (abs(sx - tx) + 1) * 'L' + 'U'

ans = f + s + t + ff
print(ans)