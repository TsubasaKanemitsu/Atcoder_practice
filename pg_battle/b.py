t = int(input())
ans = []
for i in range(t):
    n, m = list(map(int, input().split()))

    if m == 0:
        ans.append((n, n))
    else:
        # 連結成分最大パターン
        if n <= m:
            min_val = 1
            max_val = 1
        else:
            min_val = 2 * (n - m) - 1
            max_val = n / m
            if max_val.is_integer():
                max_val = int(max_val)
            else:
                max_val = int(max_val) + 1
        ans.append((min_val, max_val))

for min, max in ans:
    print(min, max)