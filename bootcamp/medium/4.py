# 7分半
import math
s = input()

for i in range(len(s) - 3, - 1, - 2):
    front = s[0:math.ceil(i / 2)]
    back = s[math.ceil(i / 2):i + 1]
    if front == back:
        print(i + 1)
        exit()