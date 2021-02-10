n = int(input())

A = list(map(int, input().split()))

color = []

for a in A:
    if 1 <= a <= 399:
        color.append('gray')
    elif 400 <= a <= 799:
        color.append('brown')
    elif 800 <= a <= 1199:
        color.append('green')
    elif 1200 <= a <= 1599:
        color.append('skyblue')
    elif 1600 <= a <= 1999:
        color.append('blue')
    elif 2000 <= a <= 2399:
        color.append('yellow')
    elif 2400 <= a <= 2799:
        color.append('daidai')
    elif 2800 <= a <= 3199:
        color.append('red')
    else:
        color.append('free')

free = color.count('free')
_color = [c for c in color if c != 'free']
num = len(list(set(_color)))

if free == 0:
    ans_min = num
    ans_max = num
else:
    if num == 0:
        ans_min = 1
        ans_max = free
    else:
        ans_min = num
        ans_max = num + free
print(ans_min, ans_max)