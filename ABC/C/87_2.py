n = int(input())

a = [list(map(int, input().split())) for _ in range(2)]

ame = 0
for i in range(n):
    temp_ame = sum(a[0][0:i + 1]) + sum(a[1][i:n])
    ame = max(ame, temp_ame)
print(ame)
