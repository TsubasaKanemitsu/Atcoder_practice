R, C = list(map(int, input().split()))

sheet = []

for r in range(R):
    sheet.extend([list(map(int, input().split()))])

col_sum = [0 for i in range(C)]

for r in range(R):
    c_sum = 0
    sm = sum(sheet[r])
    sheet[r].append(sm)
    result = list(map(lambda x: str(x), sheet[r]))
    for c in range(C):
        col_sum[c] += sheet[r][c]    

    print(' '.join(result))
last_sum = sum(col_sum)
col_sum.append(last_sum)
result = list(map(lambda x: str(x), col_sum))
print(' '.join(result))
