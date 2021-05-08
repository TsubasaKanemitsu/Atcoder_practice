import math
a, b, c, d = list(map(int, input().split()))

attack_a = math.ceil(c / b)
attack_b = math.ceil(a / d)

if attack_a > attack_b:
    print("No")
else:
    print("Yes")
    