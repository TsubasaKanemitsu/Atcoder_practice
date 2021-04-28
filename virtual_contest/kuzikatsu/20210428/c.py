# 復習
# 1時間
h, w, K = list(map(int, input().split()))
c = [list(input()) for _ in range(h)]

ans = 0

for bit_h in range(1 << h):
    s_h = set()
    for i in range(h):
        if bit_h & (1 << i):
            s_h.add(i)
    for bit_w in range(1 << w):
        s_w = set()
        for j in range(w):
            if bit_w & (1 << j):
                s_w.add(j)
        cnt = 0
        for k in range(h):
            for l in range(w):
                if k not in s_h and l not in s_w and c[k][l] == '#':
                    cnt += 1
        if cnt == K:
            ans += 1
print(ans)