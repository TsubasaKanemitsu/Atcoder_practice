# 貪欲法
# nがng数であることに注意

n = int(input())

ng = [int(input()) for _ in range(3)]
if n in ng:
    print("NO")
    exit()
cnt = 100
while cnt > 0:
    if n - 3 not in ng:
        n -= 3
    elif n - 2 not in ng:
        n -= 2
    elif n - 1 not in ng:
        n -= 1
    else:
        print("NO")
        exit()
    cnt -= 1
if n <= 0:
    print("YES")
else:
    print("NO")