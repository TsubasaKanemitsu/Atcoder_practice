k = int(input())

cnt = 0
ans = []

def dfs(digit, val, ans):
    
    ans.append(val)

    if digit == 10:
        return
    
    for j in range(-1, 2):
        add = val % 10 + j
        if 0 <= add <= 9:
            dfs(digit + 1, val * 10 + add, ans)

for i in range(1, 10):
    dfs(1, i, ans)

ans.sort()
print(ans[k - 1])

