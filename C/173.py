import itertools
h, w, k = list(map(int, input().split()))

c = [list(input()) for _ in range(h)]
    
ans = 0

for row_bit in range(1 << h):
    for col_bit in range(1 << w):
        black = 0
        for i in range(h):
            for j in range(w):
                if row_bit & (1 << i) == 0 and col_bit & (1 << j) == 0 and c[i][j] == '#':
                    black += 1

        if black == k:
            ans += 1
print(ans)
