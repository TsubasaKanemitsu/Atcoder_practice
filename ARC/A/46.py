# 7分30秒
# 全探索

n = int(input())

ans = []
i = 1
while len(ans) < n:
    num = str(i)
    cnt = num.count(num[0])
    if len(num) == cnt:
        ans.append(i)
    i += 1
print(ans[n - 1])