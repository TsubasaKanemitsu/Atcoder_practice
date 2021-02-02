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
            for k in range(len(s)):
                if i <= k and k <= j:
                    continue
                else:
                    t += s[k]

            if t == target:
                print("YES")
                exit()
    print("NO")