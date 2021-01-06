n, m, t = list(map(int, input().split()))
battery = n
st = []
end = [0]
for i in range(m):
    a, b = list(map(int, input().split()))
    st.append(a)
    end.append(b)

for i in range(m):
    diff = end[i] - st[i]
    n = n - diff
    if n <= 0:
        break
    else:
        add = b - a
        n = n + add
        if n > battery:
            n = battery

