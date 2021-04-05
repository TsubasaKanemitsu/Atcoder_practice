n, m, x = list(map(int, input().split()))
A = list(map(int, input().split()))

cnt = [0] * n
for a in A:
    cnt[a] += 1

left = sum(cnt[0:x + 1])
right = sum(cnt[x:])

print(min(left, right))