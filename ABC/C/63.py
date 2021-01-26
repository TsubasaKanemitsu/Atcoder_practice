# 最初に書いていたコード(WA)
# n = int(input())

# s = [int(input()) for _ in range(n)]

# s.sort()
# print(s)
# cum_sum = [s[0]]

# for i in range(1, n):
#     cum_sum.append(cum_sum[i - 1] + s[i])
# print(cum_sum)

# cum_sum.sort(reverse=True)

# for i in range(len(cum_sum)):
#     if cum_sum[i] % 10 != 0:
#         print(cum_sum[i])
#         exit()
# print(0)

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