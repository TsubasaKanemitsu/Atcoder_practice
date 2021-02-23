# 7分
x = int(input())

a = [i + 1 for i in range(5 * 10 ** 4 + 1)]

dis = 0
for i in range(len(a)):
    dis += a[i]
    if dis >= x:
        print(i + 1)
        break
