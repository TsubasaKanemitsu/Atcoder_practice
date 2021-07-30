# ABC 179 C
# 詰まった
# ループの削減

N = int(input())

ans = 0

for a in range(1, N):
    b_cnt = (N - 1) // a
    ans += b_cnt
print(ans)