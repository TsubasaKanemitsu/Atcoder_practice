# 37分
import sys
sys.setrecursionlimit(10 ** 7)
k = int(input())

# step1
# 2進数化

ans = []
while k > 0:
    if k % 2 == 0:
        ans.append(0)
        k = k // 2
    else:
        k = k // 2
        ans.append(2)

ans = ans[::-1]

print(*ans, sep="")