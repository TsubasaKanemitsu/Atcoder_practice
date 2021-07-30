# 典型90
# 78 ★2
# Easy Graph Problem

# 考察
# 自分より小さい値の頂点が1つの場合のみを知りたいので
# 連結状態を記録するときに、自分より頂点が小さい場合のときだけ
# 記録する
# 後は、1 ~ N番目までの頂点に紐づく辺の数をカウントすればいいだけ

from collections import defaultdict
n, m = list(map(int, input().split()))

graph = defaultdict(list)

for _ in range(m):
    a, b = list(map(int, input().split()))
    if a > b:
        graph[a].append(b)
    else:
        graph[b].append(a)

ans = 0
for i in range(1, n + 1):
    if len(graph[i]) == 1:
        ans += 1
print(ans)
        

