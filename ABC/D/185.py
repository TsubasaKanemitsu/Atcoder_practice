import math
n, m = list(map(int, input().split()))
if m == 0:
    print(1)
    exit()
    
A = list(map(int, input().split()))
A.append(n + 1)
A.append(0)
A = list(set(A))
A.sort(reverse=True)

if n == m:
    print(0)
    exit()

diff = []
diff_min = 10 ** 99
for i in range(len(A) - 1):
    temp_diff = A[i] - A[i + 1] - 1
    if temp_diff != 0:
        diff.append(temp_diff)
diff_min = min(diff)

ans = 0
for i in range(len(diff)):
    # diff[i] // diff_min + diff[i] % diff_minでうまく行かなかった
    # 割ったときに小数点が入っている場合は切り上げという考え方をしなければならない(余りを足すわけではない)
    ans += math.ceil(diff[i] / diff_min)
print(ans)
