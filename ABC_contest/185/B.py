n, m, t = list(map(int, input().split()))
battery = n
ed = [0]

for i in range(m):
    a, b = list(map(int, input().split()))
    ed.append(b)
    
    diff = a - ed[i]
    n = n - diff
    
    if n <= 0:
        break

    if n != battery:
        add = b - a
        n = n + add
    if n > battery:
        n = battery
    
if n > 0:
    diff = t - ed[m]
    n = n - diff
    
if n <= 0:
    n = 0

if n > 0:
    print("Yes")
else:
    print("No")