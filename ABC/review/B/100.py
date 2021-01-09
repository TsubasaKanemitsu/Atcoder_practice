d, n = list(map(int, input().split()))

def divide(num):
    count = 0
    while num // 100 > 0:
        if num % 100 == 0:
            num = num // 100
            count += 1
        else:
            break
    return count

match_num = []
i = 1
while len(match_num) < n:
    if divide(i) == d:
        match_num.append(i)
    i += 1

print(match_num[n - 1])