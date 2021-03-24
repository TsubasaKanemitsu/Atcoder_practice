n = input()
ans = 0
if len(n) % 2 == 1:
    print(0)
else:
    # if len(n) == 2:
    #     ans = int(n) // 11
    # if len(n) == 4:
    #     # ans += 9
    #     ans += (int(n) - 10 ** 2) // 101
    # if len(n) >= 6:
    #     ans += 9
    #     ans += 99
    #     ans += (int(n) - 10 ** 3) // 1001
    # if len(n) >= 8:
    #     ans += 9
    #     ans += 99
    #     ans += 999
    #     ans += (int(n) - 10 ** 4) // 1001
    # if len(n) >= 10:
    #     ans += 9
    #     ans += 99
    #     ans += 999
    #     ans += 9999
    #     ans += (int(n) - 10 ** 5) // 10001
    # if len(n) >= 12:
    #     ans += 9
    #     ans += 99
    #     ans += 999
    #     ans += 9999
    #     ans += 99999
    #     ans += (int(n) - 10 ** 6) // 100001

print(ans)