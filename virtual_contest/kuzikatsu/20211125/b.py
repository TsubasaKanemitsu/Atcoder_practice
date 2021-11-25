n = int(input())
X = list(map(int, input().split()))

ans = 10 ** 18
for p in range(-200, 201):
    temp_ans = 0
    for x in X:
        temp_ans += (x - p) ** 2
    ans = min(ans, temp_ans)
print(ans)