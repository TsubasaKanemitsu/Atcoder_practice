# 全探索
# 計算量を抑える
n = int(input())

def f(x, y, z):
    return x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x


ans = [0] * (n + 1)

for x in range(int(n ** 0.5) + 1):
    for y in range(int(n ** 0.5) + 1):
        for z in range(int(n ** 0.5) + 1):
            index = f(x, y, z)
            if index <= n and 1 <= x and 1 <= y and 1 <= z:
                ans[index] += 1

for i in range(1, n + 1):
    print(ans[i])