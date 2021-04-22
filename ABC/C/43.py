# 7分
# 全探索
n = int(input())
a = list(map(int, input().split()))

ans = 10 ** 99
for i in range(-100, 101):
    temp_ans = 0
    for j in range(n):
        temp_ans += (a[j] - i) ** 2
    ans = min(temp_ans, ans)
print(ans)