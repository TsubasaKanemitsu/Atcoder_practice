# 29分
# 1WA
n, q = list(map(int, input().split()))
s = input()

t = [0 for _ in range(n + 1)]
for i in range(n):
    t[i + 1] = t[i] + (1 if s[i:i + 2] == 'AC' else 0)
for i in range(q):
    l, r = list(map(int, input().split()))
    print(t[r - 1] - t[l - 1])

"""
範囲内の部分文字列 AC を数えよと問われていますが、その代わりに「右隣が C であるような A」を数えた
方が単純です。文字列中のこのような A を a に置き換えると、問 i は「li 文字目から ri − 1 文字目までの a
を数えよ」となります (右端が 1 左に動いたことに注意してください。ri 文字目が a であってもその右隣の
C が範囲からはみ出てしまうためです)。
"""