import math


n = int(input())
ans = []
for i in range(n):
    terms = int(input())
    arr = list(map(int, input().split()))
    gcd = arr[0]
    flag_odd = True

    # 奇数側のチェック
    for j in range(0, terms, 2):
        gcd = math.gcd(gcd, arr[j])
    for j in range(1, terms, 2):
        if arr[j] % gcd == 0:
            flag_odd = False

    if flag_odd:
        ans.append(gcd)
        continue

    flag_even = True
    gcd = arr[1]
    for j in range(1, terms, 2):
        gcd = math.gcd(gcd, arr[j])
    for j in range(0, terms, 2):
        if arr[j] % gcd == 0:
            flag_even = False
    
    if flag_even:
        ans.append(gcd)
        continue
    ans.append(0)

for a in ans:
    print(a)
