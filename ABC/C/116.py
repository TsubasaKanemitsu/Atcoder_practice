n = int(input())
h = list(map(int, input().split()))

# count = 0
# for i in range(len(h) - 1):
#     if h[i] >= h[i + 1]:
#         count += h[i] - h[i + 1]
# count += h[-1]
# print(count)
cnt = 0
while True:
    if max(h) == 0:
        break
    
    i = 0
    while i < n:
        # 0の箇所がきたら飛ばして，次の区間へ移る
        if h[i] == 0:
            i += 1
        else:
            cnt += 1
            # 高さが0以上の区間に水やり
            while i < n and h[i] > 0:
                h[i] -= 1
                i += 1
print(cnt)