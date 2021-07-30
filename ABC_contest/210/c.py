from collections import deque, defaultdict
n, k = list(map(int, input().split()))
c = list(map(int, input().split()))


cnt = defaultdict(int)
for i in range(k):
    cnt[c[i]] += 1
num = len(set(c[0:k]))
max_ = num

left = 0
for i in range(k, n):
    right = i
    if c[left] == c[right]:
        left += 1
        continue

    if cnt[c[left]] >= 1:
        if cnt[c[left]] == 1:
            num -= 1
        cnt[c[left]] -= 1
    
    if cnt[c[right]] >= 0:
        if cnt[c[right]] == 0:
            num += 1
        cnt[c[right]] += 1
    max_ = max(num, max_)
    left += 1
print(max_)