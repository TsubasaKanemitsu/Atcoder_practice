from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

tree = defaultdict(list)
for _ in range(n - 2):
    a, b, c = list(map(int, input().split()))
    tree[a].append([b, c])
    tree[b].append([a, c])

Q, K = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(Q)]

print(tree)
print(XY)