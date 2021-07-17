n = int(input())
P = list(map(int, input().split()))

num = set()
now = 0

# for p in P:
#     num.add(p)
#     if now not in num:
#         print(now)
#     else:
#         now += 1
#         while now in num:
#             now += 1
#         print(now)

for p in P:
    num.add(p)
    while now in num:
        now += 1
    print(now)
