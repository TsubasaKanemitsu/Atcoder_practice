# ABC 162D RGB Triplets
from operator import add

n = int(input())
s = input()

comb = []
RGB = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    if s[i] == 'R':
        RGB[i][0] = 1
    elif s[i] == 'G':
        RGB[i][1] += 1
    else:
        RGB[i][2] += 1

cum_RGB = [RGB[0]]
for i in range(1, n):
    cum_RGB.append(list(map(add, cum_RGB[i - 1], RGB[i])))

ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        # Si == Sjの場合
        if s[i] == s[j]:
            # print(i, j)
            continue
        
        color_diff = list({'R', 'G', 'B'} - {s[i], s[j]})[0]
        # 累積和じゃなくてもRGBのそれぞれの総和でもよかった
        if color_diff == 'R':
            ans += cum_RGB[-1][0] - cum_RGB[j][0]
        elif color_diff == 'G':
            ans += cum_RGB[-1][1] - cum_RGB[j][1]
        else:
            ans += cum_RGB[-1][2] - cum_RGB[j][2]

        diff = j - i
        if j + diff < n:
            if s[j + diff] == color_diff:
                ans -= 1

print(ans)
        
        