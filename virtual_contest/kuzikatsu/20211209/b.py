n = int(input())
A = list(map(int, input().split()))

# 座標圧縮して、カウント数 // 2すればいい

arr = []
x = 0
while x < n:
    word = A[x]
    cnt = 0
    for i in range(x, n):
        if word == A[i]:
            cnt += 1
        else:
            break
    arr.append((word, cnt))
    x = i
    if x == n - 1:
        break

ans = 0
for num, cnt in arr:
    ans += cnt // 2
print(ans)