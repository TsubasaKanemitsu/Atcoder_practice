a, b = list(map(int, input().split()))

if a == 1:
    a = 14

if b == 1:
    b = 14

if a == b:
    print("Draw")
elif a > b:
    print("Alice")
else:
    print("Bob")