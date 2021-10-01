x, y = input().split('.')
x = int(x)
y = int(y)
if 0 <= y <= 2:
    print(str(x) + '-')
elif 3 <= y <= 6:
    print(x)
else:
    print(str(x) + '+')