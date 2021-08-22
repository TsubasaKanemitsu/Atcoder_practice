# ABC 196 C
# 復習
n = int(input())
# 桁数

for i in range(1, 10 ** 6 + 1):
    x = int(str(i) * 2)
    if x > n:
        print(i - 1)
        exit()
