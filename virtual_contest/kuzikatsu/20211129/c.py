s = input()
k = int(input())

# Xを.に置き換えて連続にXにできる最大数を求める

# 考察ステップ
# 1. O(N^2)ではTLEとなるので、2重ループで全探索はできない。
# 2. 左から順番にXを.に置き換えていき、最大まで置き換えたうえで
# Xが続く部分までの文字列をカウントする
# 3. 文字列のカウントができなくなれば、左端と右端を1つずつ動かす。
# 4. 尺取り法で求められる。

# Xを.に置き換えることができる数がK個以下である区間の最大を求める

right = 0
x_replace_cnt = 0
ans = 0
temp_ans = 0
for i in range(len(s)):
    left = i
    while right < len(s) and not (x_replace_cnt == k and s[right] == '.'):
        if s[right] == '.':
            x_replace_cnt += 1
        right += 1
        temp_ans += 1
        
    ans = max(ans, temp_ans)

    if s[left] == '.':
        x_replace_cnt -= 1
    temp_ans -= 1
print(ans)