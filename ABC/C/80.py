# 24分
# bit全探索

N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = - 10 ** 20
for bit in range(1 << 10):
    if bit == 0:
        continue
    temp_ans = 0
    for i in range(N):
        cnt = 0
        for j in range(len(F[i])):
            if bit & (F[i][j] << j):
                cnt += 1
        
        temp_ans += P[i][cnt]
    ans = max(ans, temp_ans)
print(ans)