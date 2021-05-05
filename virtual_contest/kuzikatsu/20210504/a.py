k, x = list(map(int, input().split()))

st_x = x - k + 1
end_x = x + k

for i in range(st_x, end_x):
    print(i, end=' ')