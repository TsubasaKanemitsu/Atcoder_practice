# やるだけ
# 実装手こずった
# シミュレーション
# 11分

n = int(input())
H = list(map(int, input().split()))

for i in range(n - 1):
    if H[i + 1] - H[i] >= 1:
        H[i + 1] -= 1

for i in range(n - 1):
    if H[i] > H[i + 1]:
        print("No")
        exit()
print("Yes")