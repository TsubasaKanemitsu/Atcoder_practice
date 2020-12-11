n = int(input())

count = 1

while 1000 * count < n:
    count += 1

print(count * 1000 - n)