from collections import defaultdict, deque

n = int(input())
path = defaultdict(list)
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    path[a].append(b)
    path[b].append(a)


def bfs(start):
    dist = [0] * (n + 1)
    Q = deque()
    Q.append(start)
    dist[start] = 0

    while len(Q) > 0:
        pos = Q.popleft()
        for i in path[pos]:
            if dist[i] == 0:
                dist[i] = dist[pos] + 1
                Q.append(i)

    return dist


dist_list = bfs(1)
second_start = 0
dist2 = 0
for i in range(n):
    if dist2 < dist_list[i]:
        dist2 = dist_list[i]
        second_start = i + 1

dist2_list = bfs(second_start)

print(max(dist2_list) + 1)

