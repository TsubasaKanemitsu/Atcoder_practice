# ABC 186C
# 進数
n = int(input())

x = ''

def n_to_eight(n, x):
    if n // 8 > 0:
        x += str(n % 8)
        n = n // 8
        return n_to_eight(n, x)
    return x + str(n % 8)


ans = 0
for i in range(1, n + 1):
    num = n_to_eight(i, x)
    if num.count('7') == 0 and str(i).count('7') == 0:
        ans += 1
    
print(ans)