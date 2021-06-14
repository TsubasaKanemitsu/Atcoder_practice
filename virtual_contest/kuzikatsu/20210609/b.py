t = int(input())

ans = []
for i in range(t):
    n = int(input())
    if n % 2 == 1:
        ans.append("Odd")
    elif n % 2 == 0 and n // 2 % 2 == 1:
        ans.append("Same")
    # 2以外の全ての偶数
    else:
        ans.append("Even")

for a in ans:
    print(a)

