# 6分
n = int(input())
diff = 0
AB = []
for i in range(n):
    a, b = list(map(int, input().split()))
    AB.append([a, b])
    diff += (b - a)

st = 10 ** 99
end = 10 ** 99
for i in range(n):
    temp_st = 0
    temp_end = 0
    A = AB[i][0]
    B = AB[i][1]
    for j in range(n):
        if i != j:
            a, b = AB[j]
            temp_st += abs(A - a)
            temp_end += abs(B - b)
    st = min(st, temp_st)
    end = min(end, temp_end)

print(st + diff + end)