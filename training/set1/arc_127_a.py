# https://miaoued.net/archives/2224
# 復習

n = int(input())

# Nが小さい値で考える
# 法則性を見つけ出す

digit = len(str(n))

ans = 0
for d in range(digit):
    low = 10 ** d
    high = 2 * low
    if high <= n:
        ans += int('1' * (d + 1))
        continue
    high = n
    ans += high - low + 1
    for i in range(1, len(str(low))):
        low = list(str(low))
        low[i] = '1'
        low = int(''.join(low))
        if low <= n:
            num = min(int(str(low)[0: i + 1] + '9' * (len(str(low)) - (i + 1))), n)
            ans += num - low + 1
            # print(low, num)
            continue
        break
    break
        
print(ans)