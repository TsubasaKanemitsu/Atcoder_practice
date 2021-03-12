# keyに対して複数の選択肢が存在することを意識する．
# WAが出る4
from collections import defaultdict
n, m = list(map(int, input().split()))

teiki_bin = defaultdict(list)

x_val = []
x_key = []
for _ in range(m):
    st, end = list(map(int, input().split()))
    if st == 1:
        x_val.append(end)
    
    if end == n:
        x_key.append(st)

ans = set(x_val) & set(x_key)

if len(ans) >= 1:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
