import numpy as np
c = []

for i in range(3):
    c.append(list(map(int, input().split())))

for i in range(101):
    a_1 = i
    b_1 = c[0][0] - a_1
    b_2 = c[0][1] - a_1
    b_3 = c[0][2] - a_1
    a_2 = c[1][0] - c[0][0] + a_1
    a_3 = c[2][0] - c[0][0] + a_1

    if a_1 + b_1 == c[0][0] and a_1 + b_2 == c[0][1] and a_1 + b_3 == c[0][2] and a_2 + b_1 == c[1][0] and a_2 + \
            b_2 == c[1][1] and a_2 + b_3 == c[1][2] and a_3 + b_1 == c[2][0] and a_3 + b_2 == c[2][1] and a_3 + b_3 == c[2][2]:
            print("Yes")
            exit()

print("No")