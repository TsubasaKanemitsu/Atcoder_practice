# 13分
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

st = 10 ** 99
end = 10 ** 99
st_pos = 0
end_pos = 0
for i in range(n):
    diff_st = 0
    diff_end = 0
    for j in range(n):
        if i != j:
            a1, b1 = ab[i]
            a2, b2 = ab[j]
            diff_st += abs(a1 - a2)
            diff_end += abs(b1 - b2)
    if diff_st < st:
        st_pos = a1
        st = diff_st
    if diff_end < end:
        end_pos = b1
        end = diff_end

ans = 0
for i in range(n):
    a, b = ab[i]
    ans += abs(st_pos - a) + (b - a) + abs(end_pos - b)
print(ans)