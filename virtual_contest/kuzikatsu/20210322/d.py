# 制約条件が重要
# 辞書順でK番目に小さいものということは，
# 文字列長がKとなるまでの部分文字列を全探索して
# ソートすることで求めることができる．
# よって計算量は，O(len(s) * K* log(NK))となり，間に合う
s = input()
k = int(input())

substring = set()

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        if j > i + k:
            break
        substring.add(s[i:j])

substring = list(substring)
substring.sort()
print(substring[k - 1])
