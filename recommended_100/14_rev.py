# 復習必要
# 解説読む

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = 10 ** 99
for bit in range(1 << n):
    cnt = 0
    pos = set()
    for i in range(n):
        if bit & (1 << i):
            # 見たい物件数のカウント
            cnt += 1
            pos.add(i)

    # 見たい物件数がK物件になっているとき
    if cnt == k:
        diff = 0
        left_max = a[0]
        
        for j in range(n - 1):
        # for j in range(len(pos) - 1):
            if j in pos:
                # 見たい物件が左端の建物より低い場合
                if left_max >= a[j + 1]:
                    temp_diff = abs(left_max - a[j + 1]) + 1
                    diff += temp_diff
                    left_max = a[j + 1] + temp_diff
                else:
                    left_max = a[j + 1]
            else:
                left_max = max(left_max, a[j + 1])
                
        ans = min(ans, diff)
print(ans)
