n = int(input())
a = list(map(int, input().split()))

a.insert(0, 0)
a.append(0)

sum_a = 0

for i in range(1, len(a)):
    sum_a += abs(a[i] - a[i - 1])

for i in range(1, len(a) - 1):
    diff = (abs(a[i] - a[i - 1]) + abs(a[i + 1] - a[i])) - abs(a[i - 1] - a[i + 1])
    print(sum_a - diff)