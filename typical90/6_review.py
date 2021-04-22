# 辞書順最小は前から貪欲法

n, k = list(map(int, input().split()))
s = list(input())

cnt = [[-1] * (len(s) + 1) for _ in range(26)]

# ある位置より右側に存在する各アルファベットの位置を数え上げる
for i in range(len(s) - 1, -1, -1):
    for j in range(26):
        # 文字が一致したとき
        # 場所の値を入れる
        if ord(s[i]) - ord('a') == j:
            cnt[j][i] = i
        # 一致しない場合，以前に出現した場所と同じ
        else:
            cnt[j][i] = cnt[j][i + 1]

now_pos = 0
ans = ''
for i in range(1, k + 1):
    for j in range(26):
        next_pos = cnt[j][now_pos]
        max_length = len(s) - (next_pos + 1) + i
        if max_length >= k and next_pos != -1:
            ans += chr(ord('a') + j)
            now_pos = next_pos + 1

            break
print(ans)
