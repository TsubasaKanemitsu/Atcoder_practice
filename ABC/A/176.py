n, x, t = list(map(int, input().split()))
mins = 0

while x * mins < n:
    mins += 1
print(mins * t) 