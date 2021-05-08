N, D, H = list(map(int, input().split()))
DH = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    d, h = DH[i]
    temp_ans = h - d * (H - h) / (D - d)
    ans = max(ans, temp_ans)
print(ans)