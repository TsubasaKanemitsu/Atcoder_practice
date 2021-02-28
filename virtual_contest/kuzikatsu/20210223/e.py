# 1時間
n, m = list(map(int, input().split()))

place = []
for i in range(m):
    _a, _b = list(map(int, input().split()))
    place.append((_a, _b))
place.sort()
st = place[0][0]
ed = place[0][1]
cnt = 1
for i in range(1, m):
    a = place[i][0]
    b = place[i][1]
    if st <= a <= ed and ed > b:
        ed = b
    elif ed <= a:
        st = a
        ed = b
        cnt += 1
print(cnt)
