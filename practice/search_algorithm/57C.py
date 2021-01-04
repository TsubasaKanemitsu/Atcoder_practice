# 4分40秒
n = int(input())

min_f = 11
i = 1
while i * i <= n:
    if n % i == 0:
        a = i
        b = n // i
        temp_f = max(len(str(a)), len(str(b)))
        min_f = min(min_f, temp_f)
    i += 1
print(min_f)
        