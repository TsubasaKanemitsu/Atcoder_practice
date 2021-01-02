n, m = list(map(int, input().split()))

count_true = [False for i in range(n)]
count_false = [0 for i in range(n)]
for _ in range(m):
    p, s = list(input().split())
    p = int(p)
    if s == 'WA':
        if count_true[p - 1] == False:
            count_false[p - 1] += 1
    else:
        count_true[p - 1] = True

sum_false = 0
for i in range(n):
    if count_true[i] == True:
        sum_false += count_false[i]
print(count_true.count(True), sum_false)    