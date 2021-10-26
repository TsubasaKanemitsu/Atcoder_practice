from collections import deque
n = int(input())
A = list(map(int, input().split()))

# 順位と人
memo = list()
for idx, a in enumerate(A):
    memo.append([idx + 1, a])

memo.sort(key=lambda x:x[1], reverse=True)

memo = deque(memo)

front = []
for i in range(len(memo)):
    idx1, a1 = memo.popleft()
    idx2, a2 = memo.pop()

    if i % 2 == 0:
        front.append(idx1)