n = int(input())

s = [int(input()) for _ in range(n)]

s.sort()
ans = sum(s)

if ans % 10 != 0:
    print(ans)

else:
    for i in range(n):
        if (ans - s[i]) % 10 != 0:
            ans -= s[i]
            print(ans)
            exit()
    print(0)