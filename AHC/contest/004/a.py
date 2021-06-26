from collections import defaultdict
n, m = list(map(int, input().split()))
S = [input() for _ in range(m)]
A = [['.'] * n for _ in range(n)]
# print(S)
S.sort()
# 文字列が長いもの順にする
S_and_length = []
for s in S:
    S_and_length.append((s, len(s)))
S_and_length.sort(key=lambda x:x[1], reverse=True)
print(S_and_length)
# トーラス上になっているので，最初の一行目と一列目は固定でいいのではないか?
# 先頭の文字毎の部分文字列リストを作成
# initial = defaultdict(list)
# for s in S:
#     initial[s[0]].append(s)
# print(S)

# ここに部分文字列をはめ込んでいく
for a in A:
    print(''.join(a))
