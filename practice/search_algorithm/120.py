a, b, k = list(map(int, input().split()))


count = 0
i = min(a, b)

while i > 0:
    if a % i == 0 and b % i == 0:
        count += 1
    if count == k:
        break
    i -= 1
print(i)