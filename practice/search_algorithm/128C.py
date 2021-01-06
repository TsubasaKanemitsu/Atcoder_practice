N, M = list(map(int, input().split()))

k = []
s = []

for i in range(M):
    temp = list(map(int, input().split()))
    k.append(temp[0])
    s.append(temp[1:])
p = list(map(int, input().split()))

ans = 0
for switch in range(1 << N):
    count = 0
    for m in range(M):
        on_switch = 0
        for i in range(N):
            # スイッチの数カウント
            if switch & (1 << i) and i + 1 in s[m]:
                on_switch += 1
        if on_switch % 2 == p[m]:
            count += 1
    if count == M:
        ans += 1
print(ans)