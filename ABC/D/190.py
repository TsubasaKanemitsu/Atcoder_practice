N = int(input())

i = 1
cnt = 0
while i * i <= 2 * N:
    if 2 * N % i == 0:
        if i % 2 != 2 * N // i % 2:
            cnt += 1
    i += 1
print(2 * cnt)