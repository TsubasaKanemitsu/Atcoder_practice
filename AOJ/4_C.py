result = 1
while result > 0:
    a, op, b = list(input().split())
    a = int(a)
    b = int(b)
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '/':
        print(int(a / b))
    elif op == '*':
        print(a * b)
    else:
        break
