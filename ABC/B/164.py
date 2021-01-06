a, b, c, d = list(map(int, input().split()))
count = 0
while True:
    if count % 2 == 1:
        a -= d
        if a <= 0:
            result = "No"
            break
    else:
        c -= b
        if c <= 0:
            result = "Yes"
            break
    
    count += 1
print(result)