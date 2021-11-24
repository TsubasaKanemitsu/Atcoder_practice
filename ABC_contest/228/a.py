s, t, x = list(map(int, input().split()))

# if s == 0:
#     s = 24
# if t == 0:
#     t = 24
# if x == 0:
#     x = 24

if s <= x < t:
    print("Yes")
    exit()
if t < s:
    num = set([i for i in range(s, 24)]) | set([i for i in range(0, t)])
    if x in num:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
print("No")