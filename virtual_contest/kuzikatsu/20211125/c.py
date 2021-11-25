# 40min
# 貯めれない、～までという条件を見逃していた

n, w = list(map(int, input().split()))

# imos法
time = [0] * (2 * 10 ** 5 + 1)
# time[0] = 0

for _ in range(n):
    s, t, p = list(map(int, input().split()))
    time[s - 1] -= p
    time[t - 1] += p

for i in range(len(time)):
    time[i] += time[i - 1]

for i in range(len(time)):
    if abs(time[i]) > w:
        print("No")
        exit()
print("Yes")