n = int(input())
a = int(input())

money = n - n // 500 * 500

if money <= 0:
    print("Yes")
else:
    if money <= a:
        print("Yes")
    else:
        print("No")