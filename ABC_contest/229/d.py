s = input()
k = int(input())

# Xの間に存在する.をXに置き換えたときに、
# Xの連続する個数を最大化できる配置を考える

# 尺取り法
# left = 0
# right = ? 進ませる
# Xの連続数を格納する変数



left = 0
right = 0

# 連続するXの数
x_num = 0

# Xにできる.の数
k_log = 0

ans = 0

for i in range(len(s)):
    while right < len(s) and not (s[right] == '.' and k_log + 1 > k):
        if s[right] == 'X':
            x_num += 1
        else:
            k_log += 1
            x_num += 1
        right += 1
    
    ans = max(ans, x_num)
    
    if s[left] == 'X':
        x_num -= 1
    else:
        x_num -= 1
        k_log -= 1
    left += 1
print(ans)