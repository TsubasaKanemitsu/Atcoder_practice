from collections import Counter, defaultdict
n = int(input())
S = [input() for _ in range(n)]

# cnt = defaultdict(int)
# for s in S:
#     cnt[s] += 1
cnt = Counter(S)
ans = list(cnt.items())
ans.sort(key=lambda x:x[1], reverse=True)
print(ans[0][0])