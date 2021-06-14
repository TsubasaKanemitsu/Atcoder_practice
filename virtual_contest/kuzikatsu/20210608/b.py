n = int(input())
A = list(map(int, input().split()))

multiple_a = 1
for a in A:
    multiple_a *= a

numerator = 0
for a in A:
    numerator += multiple_a // a

ans = multiple_a / numerator
print(ans)