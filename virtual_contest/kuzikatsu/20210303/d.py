s = int(input())
c, a, b, d = 1, 10 ** 9, 1 + s // (10 ** 9), 10 ** 9 - s % (10 ** 9)
if s % (10 ** 9):
    print(0, 0, c, a, b, d)
else:
    print(0, 0, c, a, b - 1, 0)