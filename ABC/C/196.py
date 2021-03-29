# 17分
# 実際に値を書き出して，法則性を見つける

n = input()

ans = 0
if len(n) >= 2:
    ans += min(int(n), 99) // 11
if len(n) >= 4:
    ans += min(int(n), 9999) // 101 - 9
if len(n) >= 6:
    ans += min(int(n), 999999) // 1001 - 99
if len(n) >= 8:
    ans += min(int(n), 99999999) // 10001 - 999
if len(n) >= 10:
    ans += min(int(n), 9999999999) // 100001 - 9999
if len(n) >= 12:
    ans += min(int(n), 999999999999) // 1000001 - 99999


print(ans)