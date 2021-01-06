n = int(input())
a = list(map(int, input().split()))

a = [[i + 1, num] for i, num in enumerate(a)]

a = sorted(a, reverse=False, key=lambda x: x[1])

for i in range(len(a)):
    print(a[i][0], '', end='')
print()

