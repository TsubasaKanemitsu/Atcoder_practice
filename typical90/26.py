from collections import defaultdict, deque
n = int(input())

tree = defaultdict(list)

for i in range(n - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)
print(tree)
def bfs(st):
    Q = deque()
    visited = [False] * n
    dist = [0] * n

    Q.append(st)

    while len(Q) > 0:
        x = Q.popleft()
        pos = tree[x]
        for p in pos:
            if visited[p]:
                continue
            visited[p] = True
            dist[p] = dist[x] + 1
            Q.append(p)
    return dist

for i in range(n):
    print(bfs(i))
        
