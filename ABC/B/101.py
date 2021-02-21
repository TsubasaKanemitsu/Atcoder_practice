n = input()

def S(n):
    num = list(map(int, n))
    return sum(num)

if int(n) % S(n) == 0:
    print("Yes")
else:
    print("No")