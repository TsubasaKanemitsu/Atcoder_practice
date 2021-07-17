## https://qiita.com/u2dayo/items/5f9dfee2ec0145402d75
n = int(input())

cnt = 0
under = 1
while under <= n:
    under += 26 ** (cnt + 1)
    cnt += 1

# for i in range(1, cnt):
#     n -= 26 ** i
# print(n)
ans = ''
for _ in range(cnt):
    mod = n % 26
    n = n // 26
    if mod == 0:
        ans += 'z'
        n -= 1
    else:
        ans += chr(96 + mod)

ans = ''.join(list(ans)[::-1])
print(ans)