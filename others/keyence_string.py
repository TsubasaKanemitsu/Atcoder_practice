import itertools

s = input()
target = 'keyence'
if s == target:
    print("YES")
    exit()
else:
    for i in range(len(s)):
        for j in range(i, len(s)):
            t = ''
            # 抜き出す部分文字列を決める部分
            # i ~ jの区間を抜き出す部分文字列とする
            for k in range(len(s)):
                if i <= k and k <= j:
                    continue
                else:
                    t += s[k]

            if t == target:
                print("YES")
                exit()
    print("NO")