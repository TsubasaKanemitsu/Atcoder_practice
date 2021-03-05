# 区間切り出し
# whileで条件下の間，区間を進める
# iがnより下であるという条件は重要，配列の添え字ミスをなくす

n = int(input())
a = list(map(int, input().split()))

i = 0
cnt = 0
while i < n:
    
    while i + 1 < n and a[i] == a[i + 1]:
        i += 1

    if i + 1 < n and a[i] < a[i + 1]:
        while i + 1 < n and a[i] <= a[i + 1]:
            i += 1
        
    elif i + 1 < n and a[i] > a[i + 1]:
        while i + 1 < n and a[i] >= a[i + 1]:
            i += 1

    cnt += 1
    i += 1
print(cnt)