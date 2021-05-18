# 偶奇の性質
from collections import defaultdict
n = int(input())
v = list(map(int, input().split()))

# n = random.randint(10, 20)
# v = [random.randint(1, 30) for _ in range(n)]
# print(n, v)
# 全て同じ要素の場合
if len(set(v)) == 1:
    print(n // 2)
    exit()

odd_cnt = defaultdict(int)
even_cnt = defaultdict(int)

for i in range(n):
    if i % 2 == 0:
        odd_cnt[v[i]] += 1
    else:
        even_cnt[v[i]] += 1

odd = []
even = []

for k, v in odd_cnt.items():
    odd.append([k, v])
odd.sort(key=lambda x:x[1], reverse=True)

for k, v in even_cnt.items():
    even.append([k, v])
even.sort(key=lambda x:x[1], reverse=True)

if odd[0][0] == even[0][0]:
    if len(set(odd_cnt)) == 1 and len(set(even_cnt)) >= 2:
        ans = n - odd[0][1] - even[1][1]
        print(ans)
    elif len(set(odd_cnt)) >= 2 and len(set(even_cnt)) == 1:
        ans = n - odd[1][1] - even[0][1]
        print(ans)
    else:
        ans = n - max(odd[0][1], even[0][1]) - max(odd[1][1], even[1][1])
        print(ans)
else:
    ans = n - odd[0][1] - even[0][1]
    print(ans)