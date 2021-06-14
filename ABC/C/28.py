# 5分
num = list(map(int, input().split()))

ans = []
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            ans.append(num[i] + num[j] + num[k])
ans.sort(reverse=True)
print(ans[2])