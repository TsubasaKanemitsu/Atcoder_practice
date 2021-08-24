# ABC 18 B
# 文字列操作

s = input()
n = int(input())

for i in range(n):
    l, r = list(map(int, input().split()))
    l -= 1
    s = s[0:l] + s[l:r][::-1] + s[r:]
print(s)