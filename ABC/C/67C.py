n = int(input())
a = list(map(int, input().split()))

sum_a = sum(a)

min_val = 100 ** 30
x = 0
for i in range(n):
    x += a[i]
    if i + 1 < n:
        min_val = min(min_val, abs(2 * x - sum_a))

print(min_val)
