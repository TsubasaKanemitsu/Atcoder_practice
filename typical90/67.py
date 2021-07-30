import sys
sys.setrecursionlimit(10 ** 7)

N, K = input().split()

def Base_10_to_n(n, b):
    if n // b:
        return Base_10_to_n(n // b, b) + str(n % b)
    return str(n % b)


num = N
ten = 0
for i in range(int(K)):
    base_10 = int(num, 8)
    # 9進数
    base_9 = str(Base_10_to_n(base_10, 9))
    num = ""
    for j in range(len(base_9)):
        if base_9[j] == "8":
            num += "5"
        else:
            num += base_9[j]

print(num)