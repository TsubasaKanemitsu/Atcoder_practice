N = int(input())
T, A = list(map(int, input().split()))

H = list(map(int, input().split()))

diff = 10 ** 100
for i, h in enumerate(H):
    temp_diff = abs(T - h * 0.006 - A)
    if temp_diff < diff:
        ans = i + 1
        diff = temp_diff
print(ans)