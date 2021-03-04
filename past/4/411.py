from collections import Counter
s = input()

val = 0
s_cnt = Counter(s)
for k, v in s_cnt.items():
    
    if v > val:
        ans = k
        val = v
print(ans)