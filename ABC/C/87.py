n = int(input())

A_1 = list(map(int, input().split()))
A_2 = list(map(int, input().split()))

ans = 0
for i in range(n):
    temp_ans = sum(A_1[0:i + 1]) + sum(A_2[i:])
    ans = max(ans, temp_ans)
print(ans)
